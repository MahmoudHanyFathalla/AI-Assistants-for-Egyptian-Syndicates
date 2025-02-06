#usage of assestans
from openai import OpenAI
import json

# Initialize OpenAI client
client = OpenAI()

# Function to load IDs from a file

assistant_id = "asst_5MZtR75SSmfwbHaf20cQlLmW"

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
ask_assistant("برنامج العلاج لنقابه المهندسين دا بقي ممكن يساعدني في ايه او هستفاد منه بايه و ازاي")

#"برنامج العلاج لنقابه المهندسين دا بقي ممكن يساعدني في ايه او هستفاد منه بايه و ازاي"
#"تعرف ايه عن الولاده"
#"ايه نظام الاشعه او تتعمل ازاي ومحتاجه ايه وكام"
#"ايه البيحصل لما نخرج من المستشفي"
#"انا اسه جديد هنا في النقابه ومش عارف اعمل ايه"
"""
األوراق المطلوبه لعمل عضويه النقابة ؟
كيفيه االشتراك في االبليكشن )نقابتي( وتسجيل الدخول
كيفيه االشتراك في المشروع العالجي بالنسبه للدفعات القديمه
"ما هي رسوم الاشتراك لمرافقه زوج"
"ما هي عناوين و ارقام تليفونات النقابه العامه و النقابات الفرعية ؟"
مواعيد عمل النقابة العامة
االرقام الخاصه بالنقابه لتحديث البيانات ؟
"""


"""
الأشخاص الذين لهم الحق في الاشتراك في البرنامج هم:

1. المهندسون (أعضاء أصيلين في النقابة).
2. الزوجة أو الزوج لأعضاء النقابة.
3. الأبناء حتى سن 26 سنة، أو حتى التخرج.
4. الآباء (مثل الوالدين) للأعضاء[0].

إذا كانت لديك أي استفسارات إضافية، فلا تتردد في السؤال!
[0] 2024pdf.pdf



الحق في الاشتراك في البرنامج الصحي يشمل:

1. **أعضاء نقابة المهندسين**: هذه تشمل المهندسين الذين يكونون أعضاء أصيلين في النقابة.
2. **أعضاء تابعين**: مثل الزوجات والأزواج، ومَن هم تحت سن 26 سنة أو الذين تخرجوا حديثاً.
3. **الأقرباء**: يمكن أن تشمل الأطفال تحت سن معينة كما هو موضح في التفاصيل الدقيقة.

إذا كنت بحاجة لمزيد من المعلومات حول الشروط والتفاصيل المحددة، يرجى إخباري بذلك![0].
[0] 2024pdf.pdf
"""