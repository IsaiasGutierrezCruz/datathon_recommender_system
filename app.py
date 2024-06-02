from src.constants import NUM_MAX_WORDS, NUMBER_COLS, TOP_N
from src.data import get_base_info
from src.smart_input_formatter import smart_input_formatter
from src.model import get_embeddings
from src.vector_database import get_top_similar, load_vector_database


import streamlit as st
from dotenv import find_dotenv, load_dotenv

# SETUP
# Load environment variables from the .env file (optional, defaults to '.env')
find_dotenv()
load_dotenv()
load_vector_database()


def run():
    st.title("Fashion products")
    st.write("Fashion product matching from natural language prompts")

    product_prompt: str = st.text_input(
        "Search for a product, describe it...",
        help="You can specify type, color, season, age range, etc.",
        max_chars=NUM_MAX_WORDS
    )

    if product_prompt:
        cleaned_product_prompt = smart_input_formatter(product_prompt)
        st.warning(f"Refactored to '{cleaned_product_prompt}'")
        # print("Searching for...", cleaned_product_prompt)

        with st.spinner("Looking for products..."):
            top_similar = get_top_similar(
                get_embeddings([cleaned_product_prompt])[0],
                n=TOP_N,
            )
            items = get_base_info(top_similar)

        # display 3 items for each row
        num_rows = TOP_N // NUMBER_COLS

        # TODO
        # last_row = TOP_N % NUMBER_COLS
    
        cont = 0

        for row in range(0, num_rows):
            cols = st.columns(NUMBER_COLS)

            for col in cols:
                item = items[cont]
                with col:
                    st.header(item.get("productDisplayName", "-"))
                    st.image(item.get("link"))
                    price = f"| ${item.get('discountedPrice')}"
                    st.write(
                        f"{item.get('articleType')} | {item.get('gender')} {price}"
                    )
                    st.write(
                        f"Colors: {item.get('baseColour')}, {item.get('colour1')}"
                    )

                    if st.button(f"View Product {item.get('id')}"):
                        st.session_state.item = item.get('id')
                        st.session_state.product_display_name = item.get('productDisplayName')
                        st.session_state.link_image = item.get('link')
                        st.session_state.article_type = item.get('articleType')
                        st.session_state.gender = item.get('gender')
                        st.session_state.base_colour = item.get('baseColour')
                        st.session_state.colour1 = item.get('colour1')
                        st.session_state.discounted_price = item.get('discountedPrice')

                        st.switch_page('pages/chosen_product.py')

                cont += 1


if __name__ == "__main__":
    run()