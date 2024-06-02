from dotenv import load_dotenv
from src.smart_input_formatter import smart_input_formatter
from src.model import get_embeddings
from src.vector_database import get_top_similar, load_vector_database

# SETUP
# Load environment variables from the .env file (optional, defaults to '.env')
load_dotenv()
load_vector_database()

# User input
product_prompt = input('Search for a product')

cleaned_product_prompt = smart_input_formatter(product_prompt)

print(cleaned_product_prompt)

top_similar = get_top_similar(
    get_embeddings([cleaned_product_prompt])[0]
)