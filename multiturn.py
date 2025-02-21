import google.generativeai as genai

genai.configure(api_key="AIzaSyBA47UPEA6lfKAQXJc1-Qnq90ERt4PI1sU")
model = genai.GenerativeModel("gemini-1.5-flash")
chat=model.start_chat(
    history=[
        {"role":"user","parts":"안녕?"},
        {"role":"model","parts":"만나서 반가워. 무엇이든 물어봐!"},
    ]
)
response=chat.send_message("우리집에는 개 두 마리가 있어.")
print(response.text)
print("===")
response=chat.send_message("우리집에는 발자국이 몇 개나 있을까?")
print(response.text)
