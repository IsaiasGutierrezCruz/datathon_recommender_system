import os

from google.generativeai import GenerativeModel
import google.generativeai as genai


# Setup API KEY to use gemini models
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Instructions to clean input
instruct_clean_prompt = (
    "Please try to correct grammar errors and re order the sentence in a meaningful way."
    " The sentence given is to query fashion products."
)
instruct_transalation_prompt = (
    'If the following text is not in english please translate it, dont add any additional text\n'
)


def smart_input_formatter(user_product_prompt : str):
    """Call an LLM to clean our user's input"""
    genai.configure(api_key=GOOGLE_API_KEY)

    model = GenerativeModel('gemini-1.5-flash-latest')
    prompt = instruct_transalation_prompt + user_product_prompt + '\n' + instruct_clean_prompt
    response = model.generate_content(prompt)

    return response.text