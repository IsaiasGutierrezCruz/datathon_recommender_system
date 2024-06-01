from helpers.smart_input_formatter import smart_input_formatter

# User input
product_prompt = input('Search for a product')

cleaned_product_prompt = smart_input_formatter(product_prompt)

print(cleaned_product_prompt)