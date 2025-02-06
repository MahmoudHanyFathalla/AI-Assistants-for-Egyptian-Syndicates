#usage of assestans
from openai import OpenAI
import json

# Initialize OpenAI client
client = OpenAI()

# Function to load IDs from a file

assistant_id = "asst_wI5om1NWZRlg76okYkw2VJTQ"


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
            citations.append(f"[{index}] {cited_file.filename}")

    print(message_content.value)
    print("\n".join(citations))

# Example usage
ask_assistant("عايز دكتور في شارع الهلالي")


#"اعاني من مشاكل جلديه و اريد دكتور"
# "طب لو في البحر الاحمر؟"
#"عايز دكتور جلديه"
#"عايز دكتور في شارع الهلالي"


"""
"انا ابني الصغير تعبان اوي في اي دكتور اطفال ممكن يساعدني؟"

يمكنك زيارة أحد الأطباء المتخصصين في طب الأطفال في أسوان. إليك بعض الأسماء والأماكن:

1. **دكتور إبراهيم حسن عبد العال** - أخصائي أطفال، عنوانه: أسوان - شارع كسر الحجر.
2. **دكتور فاطمة فوزي عطية** - استشاري أطفال، عنوانها: أسوان - شارع أبطال التحرير، رقم الهاتف: 2313190. 
3. **دكتور محى الدين راغب** - استشاري أطفال، عنوانه: أسوان - شارع أبطال التحرير، رقم الهاتف: 2315188[0].

يمكنك الاتصال بأي منهم لتحديد موعد.
[0] اسوان.pdf
"""