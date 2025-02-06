#creats assestans
from openai import OpenAI
 
client = OpenAI()
 
assistant = client.beta.assistants.create(
  name="مشروع الكامل للرعاية الصحية لنقابة المهندسين",
  instructions="""
answer the quistions from the given pdf using file search in arabic 
""",
  model="gpt-4o-mini",
  tools=[{"type": "file_search"}],
)



# Store the assistant ID
assistant_id = assistant.id
print(f"Assistant ID: {assistant_id}")
# Create a vector store caled "Financial Statements"
vector_store = client.beta.vector_stores.create(name="مشروع  الكامل الرعاية الصحية لنقابة المهندسين")
 
# Ready the files for upload to OpenAI
file_paths = ["C:\\Users\\hp\\Desktop\\Neqabty\\Codes\\hey\\DataSet\\2024pdf.pdf",
             ]
file_streams = [open(path, "rb") for path in file_paths]
 
# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)
 
# You can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)


# Create a thread and attach the file to the message
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "من لهم الحق في الاشتراك",
      # Attach the new file to the message.
     
    }
  ]
)
 
# The thread now has a vector store with that file in its tool resources.
print(thread.tool_resources.file_search)


# Use the create and poll SDK helper to create a run and poll the status of
# the run until it's in a terminal state.

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id, assistant_id=assistant.id
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