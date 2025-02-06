#usage of assestans
from openai import OpenAI
import json

# Initialize OpenAI client
client = OpenAI()

# Function to load IDs from a file

assistant_id = "asst_ySBUZf7UKaP6a88iftJdHOfd"

# Function to interact with the assistant
def ask_assistant(prompt):
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
        thread_id=thread.id, assistant_id=assistant_id,temperature=1
    )

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    print(message_content.value)
    print("\n".join(citations))

# Example usage
ask_assistant("انا لسه منزل الابليكيشن بتاعكو دا ومش فاهم حاجف فيه ولا في النقابه انا ممكن استفاد بايه و ازاي")

#"من لهم الحق في الاشتراك"
#"كيفيه الشتراك في االبليكشن"
#"ازاي اجدد اشتراك النقابه"
#"انا لسه منزل الابليكيشن بتاعكو دا ومش فاهم حاجف فيه ولا في النقابه انا ممكن استفاد بايه و ازاي"