import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
import google.generativeai as genai

# Load environment variables from the .env file (optional, defaults to '.env')
load_dotenv()

# Setup API KEY to use gemini models
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = GOOGLE_API_KEY)

# Instructions to clean input
instruct_clean_prompt = 'Please try to correct grammar errors and re order the sentence in a meaningful way'
instruct_transalation_prompt = 'If the following text is not in english please translate it \n'

# Call our LLM to clean our user's input
def smart_input_formatter(user_product_prompt : str):
    model = GenerativeModel('gemini-pro')
    prompt = instruct_transalation_prompt + user_product_prompt + '\n' + instruct_clean_prompt
    response = model.generate_content(prompt)
    return response.text