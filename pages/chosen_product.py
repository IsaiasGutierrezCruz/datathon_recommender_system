import streamlit as st
from src.constants import TOP_N, NUMBER_COLS
from src.vector_database import get_top_similar, load_vector_database, get_embedding_from_id
from src.data import get_base_info


load_vector_database()

st.title(f'{st.session_state.product_display_name}')




st.image(st.session_state.link_image)#, width=300)
st.write(
    f"{st.session_state.article_type} | {st.session_state.gender}"
)
st.write(
    f"Colors: {st.session_state.base_colour}, {st.session_state.colour1}"
)

embedding_product_chosen = get_embedding_from_id(st.session_state.item)


with st.spinner("Looking for products..."):
    top_similar = get_top_similar(
        embedding_product_chosen,
        n=TOP_N + 1,
    )
    top_similar = [similar for similar in top_similar if similar != st.session_state.item]
    items = get_base_info(top_similar)


st.header("Similar products")



num_rows = TOP_N // NUMBER_COLS

cont = 0
for row in range(0, num_rows):
    cols = st.columns(NUMBER_COLS)

    for col in cols:
        item = items[cont]
        with col:
            st.header(item.get("productDisplayName", "-"))
            st.image(item.get("link"))
            st.write(
                f"{item.get('articleType')} | {item.get('gender')}"
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

                st.switch_page('pages/chosen_product.py')

        cont += 1