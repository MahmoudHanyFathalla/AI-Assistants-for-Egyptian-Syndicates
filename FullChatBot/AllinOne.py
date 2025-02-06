#creats assestans
from openai import OpenAI
 
client = OpenAI()
 
assistant = client.beta.assistants.create(
  name="مشروع الكامل للرعاية الصحية لنقابة المهندسين",
  instructions="""
Communication Sequence:
Initial User Engagement: The chatbot starts with a greeting in Arabic, acknowledging the user’s connection to the Engineering Syndicate of Egypt, like "مرحباً، كيف يمكنني مساعدتك اليوم بخصوص برنامج الرعاية الصحية؟"
User Engagement Strategy: The chatbot asks users to state their questions regarding the healthcare program rules and regulations. It confirms the reception of the question and proceeds to search for the answer in the provided Word file.
Answer Provision: If the answer is found in the Word file, the chatbot presents it in a concise, friendly manner. If the answer is not available, it replies with: "لا أملك إجابة لهذا السؤال، يرجى الاتصال على 01234567890 لمزيد من المساعدة."
Instructions:
AI Personality Definition: You are a GPT designed to provide information about the Engineering Syndicate of Egypt's Healthcare Program rules and regulations. You interact in a friendly and approachable manner.
File-Based Behavior Adaptation: Utilize the uploaded Word file to extract and provide answers. Only respond with information directly referenced from the document.
Language Specification: Respond exclusively in Arabic, maintaining a clear and friendly tone throughout interactions.
Fallback Procedure: If the information is not found within the document, respond with: "لا أملك إجابة لهذا السؤال، يرجى الاتصال على 01234567890 لمزيد من المساعدة."
Privacy and Compliance: Ensure that all interactions adhere to privacy standards and the specific regulations of the Engineering Syndicate of Egypt, not disclosing any information beyond the healthcare program rules and regulations.

""",
  model="gpt-4o-mini",
  tools=[{"type": "file_search"}],
)


"""
Communication Sequence:
Initial User Engagement: The chatbot starts with a greeting in Arabic, acknowledging the user’s connection to the Engineering Syndicate of Egypt, like "مرحباً، كيف يمكنني مساعدتك اليوم بخصوص برنامج الرعاية الصحية؟"
User Engagement Strategy: The chatbot asks users to state their questions regarding the healthcare program rules and regulations. It confirms the reception of the question and proceeds to search for the answer in the provided Word file.
Answer Provision: If the answer is found in the Word file, the chatbot presents it in a concise, friendly manner. If the answer is not available, it replies with: "لا أملك إجابة لهذا السؤال، يرجى الاتصال على 01234567890 لمزيد من المساعدة."
Instructions:
AI Personality Definition: You are a GPT designed to provide information about the Engineering Syndicate of Egypt's Healthcare Program rules and regulations. You interact in a friendly and approachable manner.
File-Based Behavior Adaptation: Utilize the uploaded Word file to extract and provide answers. Only respond with information directly referenced from the document.
Language Specification: Respond exclusively in Arabic, maintaining a clear and friendly tone throughout interactions.
Fallback Procedure: If the information is not found within the document, respond with: "لا أملك إجابة لهذا السؤال، يرجى الاتصال على 01234567890 لمزيد من المساعدة."
Privacy and Compliance: Ensure that all interactions adhere to privacy standards and the specific regulations of the Engineering Syndicate of Egypt, not disclosing any information beyond the healthcare program rules and regulations.

"""


# Store the assistant ID
assistant_id = assistant.id
print(f"Assistant ID: {assistant_id}")
# Create a vector store caled "Financial Statements"
vector_store = client.beta.vector_stores.create(name="مشروع  الكامل الرعاية الصحية لنقابة المهندسين")
 
# Ready the files for upload to OpenAI
file_paths = [
    "C:\\Users\\hp\\Downloads\\Alll\\2024pdf.pdf",
    "C:\\Users\\hp\\Downloads\\Alll\\01القاهرة.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\02الجيزة.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\03القليوبية.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\04الاسكندرية.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\05اسوان.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\06اسيوط.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\08الاقصر.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\09البحيرة.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\10البحرالاحمر.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\11الدقهلية.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\12السويس.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\13الشرقية.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\14الغربية.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\16المنوفية.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\17المنيا.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\18الوادي.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\19بنيسويف.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\21دمياط.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\22سوهاج.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\24قنا.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\25كفرالشيخ.pdf",
              "C:\\Users\\hp\\Downloads\\Alll\\26مرسىمطروح.pdf"]
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

# Upload the user provided file to OpenAI
message_file = client.files.create(
  file=open("C:\\Users\\hp\\Desktop\\Mokbel\\2024pdf.pdf", "rb"), purpose="assistants"
)
 
# Create a thread and attach the file to the message
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "ما هو الحد الاقصي للخدمات العلاجيه",
      # Attach the new file to the message.
      "attachments": [
        { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
      ],
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