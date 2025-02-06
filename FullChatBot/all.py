from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
import json
#http://127.0.0.1:8000/ask/
#http://127.0.0.1:8000
# Initialize FastAPI app
app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Initialize OpenAI client
client = OpenAI()

# Assistant and Vector Store IDs
assistant_id = "asst_OGR2Am4XOYd8lqjxudrMIC7s"
vector_store_id = "vs_J1AUf3NNpcuvBynEiHSicBVo"

# Function to interact with the assistant
def ask_assistant(prompt):
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
                "attachments": [],
            }
        ]
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assistant_id
    )

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[index] {cited_file.filename}")

    return message_content.value, citations

# Define the root endpoint to serve the HTML file
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define the ask endpoint
@app.post("/ask/")
def ask(request: Request, prompt: str = Form(...)):
    response, citations = ask_assistant(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "response": response, "citations": citations})

# Example usage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
