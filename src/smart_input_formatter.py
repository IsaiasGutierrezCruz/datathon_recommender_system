import os
from functools import lru_cache

from google.generativeai import GenerativeModel
import google.generativeai as genai

from src.constants import QUERIES_TO_USE_CACHE


# Setup API KEY to use gemini models
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Instructions to clean input
instruct_clean_prompt = (
    "Please try to correct grammar errors and re order the sentence in a meaningful way."
    " The sentence given is to query fashion products, dont change the original idea."
)
instruct_transalation_prompt = (
    'If the following text is not in english please translate it, dont add any additional text\n'
)


@lru_cache(maxsize=QUERIES_TO_USE_CACHE)
def smart_input_formatter(user_product_prompt : str):
    """Call an LLM to clean our user's input"""
    genai.configure(api_key=GOOGLE_API_KEY)

    # model = GenerativeModel('gemini-1.5-flash-latest')
    model = GenerativeModel('gemini-pro')
    prompt = instruct_transalation_prompt + user_product_prompt + '\n' + instruct_clean_prompt
    response = model.generate_content(prompt)

    return response.text