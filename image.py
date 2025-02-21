import PIL.Image
import google.generativeai as genai 

genai.configure(api_key="AIzaSyBA47UPEA6lfKAQXJc1-Qnq90ERt4PI1sU")
model = genai.GenerativeModel("gemini-1.5-flash")

picture = PIL.Image.open(".\practice_1126\실습용이미지.jpg")
response = model.generate_content(["어떤 이미지인지 알려줘.", picture])

print(response.text)