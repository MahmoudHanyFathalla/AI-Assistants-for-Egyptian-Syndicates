import tkinter as tk
from tkinter import scrolledtext, messagebox
from openai import OpenAI, error

# Initialize OpenAI client with your API key
client = OpenAI()

# Assistant and vector store IDs
assistant_id = "asst_OGR2Am4XOYd8lqjxudrMIC7s"
vector_store_id = "vs_J1AUf3NNpcuvBynEiHSicBVo"

# Function to interact with the assistant
def ask_assistant(prompt):
    try:
        # Create a thread and attach the file to the message
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "attachments": [],
                }
            ]
        )

        # Use the create and poll SDK helper to create a run and poll the status of the run until it's in a terminal state.
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id, assistant_id=assistant_id
        )

        messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

        if messages:
            message_content = messages[0].content[0].text
            return message_content.value
        else:
            return "No response received"

    except error.OpenAIError as e:
        return f"Error: {str(e)}"

# Function to handle button click
def on_ask_button_click():
    prompt = prompt_entry.get("1.0", tk.END).strip()
    if prompt:
        response = ask_assistant(prompt)
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, response)
    else:
        messagebox.showwarning("Input Error", "Please enter a prompt.")

# Create the main window
root = tk.Tk()
root.title("AI Assistant")

# Create and place widgets
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack()

prompt_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
prompt_entry.pack()

ask_button = tk.Button(root, text="Ask", command=on_ask_button_click)
ask_button.pack()

response_label = tk.Label(root, text="Response:")
response_label.pack()

response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
response_text.pack()

# Run the main loop
root.mainloop()