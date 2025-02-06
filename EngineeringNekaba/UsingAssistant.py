from openai import OpenAI
import json

# Initialize OpenAI client
client = OpenAI()

# Function to load IDs from a file

assistant_id = "asst_cKs6f4hEQG1MmjQK2APScafx"
# this one is very good : asst_zTt3ZIssJy89WEBUHLuzCQLk
# this one is top top : asst_1Ovlny0bdLuTdasL7HEQVHRK 
# #vs_mENOJDLpg8RCvqw22PmukARd

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
ask_assistant("عايز تفاصيل عن برنامج الرعايه الصحيه لنقابه المهندسين")

#"ايه انواع الاشعه ال النقابه بتوفرها وايه هي اسعارها"
#"لو سمحت متعرفش ايه اسعار الاشعه"
#"عايزك تقول دكتور باطنه من كل محافظه في مصر"
#"تعرف دكلتره عيون في مدينه نصر؟"
#"يا بتوع الطب انتو انا دماغي وجعاني اوي اوي وعندي صداع جامد فشخ اروح لمين ولا فين في القاهره"
#"هو في دكاتره اطفال في اسكندريه؟"
#"تعرف ماجد محمد عبد العزيز؟"
#"عايز دكاتره اسنان في  مدينه نصر"
#"عايز دكاتره اسنان في دمباط ر"
#"اعمل رسم مخ فين وبكام"
#"ابني لسه مولود وعايز اطهره تقدر تقولي فين وبكام"
#"ايه اسعار معالجه الحروق ومين الدكاتره بتوعهم وفين"
#"مين ليهم الحق انهم يشتركو في البرنامج  و ازاي"
#"انت بتفهم في ايه او انا ممكن اسالك في ايه"
#"انا باطني واجعاني اوي اوي ومش عارف اعمل ايه"
#"ايه هي اسعار اني اشيل ضرس"
#"هيكلفني كام لو عايز اعمل  رسم اعصاب للعصب السابع"
#ايه الاخبار كنت عايز اعرف الاسعار بتاعه لو عايز اشيل دريس او اشيل عصب فداس او اعمل كشف بول او في طفل عايز يتولد اسعار الكلام ده كام وبتتعمل فين
#ايه الاخبار كنت عايز اسال على اسعار المستشفيات في القاهره وهل في دكاتره التعيون في مدينه نصر في القاهره ويا ريت لو في دكاتره اسنان في اسكندريه برده كنت عايز اعرف الاسعار والعنوان واساميهم كل حاجات
#ايه هي خدمات راعي الصحيه المتاحه في وسط البلد عشان انا ابني الصغير تعبان وعايز اخلع اي مستشفى في وسط البلد
#السلام عليكم ايه الاخبار انا كنت عايز اسال عن مستشفيات في دمياط علشان انا من دمياط ودماغي وجعاني قوي ومصدع فهل في اي مستشفيات ممكن تعالج الصداع ده اروح لها مثلا
#"لو سمحت متعرفش فين اقدر اكشف علي نسبه الحديد في الدم وهنكلفني كام"
#"ايه هي الادويه البيساهم فيها المشروع و ايه هي الادويه المش بيساهم فيها المشروع"