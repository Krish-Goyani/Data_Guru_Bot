import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "model", "parts": "Now you are my data science interview mentor i will ask various questions, topic on machine learning and your task is to explain me in reponse of 1. list out commone interview topic of ml 2.common interview question 3.at last message that say ask me other questions "}
    ]
)
response = chat.send_message("follow system message")
print(response.text)
