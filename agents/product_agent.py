# agents/product_agent.py
import json
from core.gemini_client import ask_gemini

PRODUCTS_FILE = "data/products.json"

with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
    PRODUCTS = json.load(f)
    print("✅ Loaded products:", PRODUCTS)
    product_titles = [p["title"] for p in PRODUCTS]
    print("✅ Loaded products:", product_titles)

def handle_product_query(query: str, cart: list) -> str:
    # Ask Gemini to match query to our product catalog
    product_titles = [p["title"] for p in PRODUCTS]
    prompt = f"""
    User query: "{query}"
    Products available: {product_titles}
    Match the query to the closest product available. 
    If none matches, say 'no match'.
    """

    print(prompt);
    match = ask_gemini(prompt)
    print(match);
    if "no match" in match.lower():
        return "No matching product found."

    for product in PRODUCTS:
        print(product["title"].lower())
        print(match.lower())
        if match.lower() in product["title"].lower():
            # cart.append(product)
            print("hi")
            return f"Added {product['title']} to cart. Price: ${product['price']}"

    return "Couldn't map your query to a product."
