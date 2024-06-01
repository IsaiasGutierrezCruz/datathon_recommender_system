import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
import google.generativeai as genai

# Load environment variables from the .env file (optional, defaults to '.env')
load_dotenv()

# Setup API KEY to use gemini models
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = GOOGLE_API_KEY)


model = GenerativeModel('gemini-pro')
prompt = "Write a story about a brave knight."
response = model.generate_content(prompt)
print(response.text)