from dotenv import find_dotenv, load_dotenv
from src.constants import TOP_N
from src.data import get_base_info
from src.smart_input_formatter import smart_input_formatter
from src.model import get_embeddings
from src.vector_database import get_top_similar, load_vector_database

# SETUP
# Load environment variables from the .env file (optional, defaults to '.env')
find_dotenv()
load_dotenv()
load_vector_database()


# User input
product_prompt = input('Search for a product: ')

cleaned_product_prompt = smart_input_formatter(product_prompt)

print("Searching for...", cleaned_product_prompt)

top_similar = get_top_similar(
    get_embeddings([cleaned_product_prompt])[0],
    n=TOP_N,
)

print(top_similar)

print(get_base_info(top_similar))