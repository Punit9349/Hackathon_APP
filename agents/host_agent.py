# agents/host_agent.py
from agents import product_agent, payment_agent
from core.memory import cart
from core.gemini_client import ask_gemini

def handle_query(query: str) -> str:
    """
    Use Gemini to classify query and route to the right agent.
    """
    classification_prompt = f"""
    You are a router for an AI shopping assistant.
    Decide if the user query is about:
    - 'product' (search, browse, add to cart),
    - 'payment' (cart, checkout, order),
    - or 'other' (chit-chat).

    User query: "{query}"
    Answer with only one word: product, payment, or other.
    """
    category = ask_gemini(classification_prompt).lower()

    if "product" in category:
        return product_agent.handle_product_query(query, cart)
    elif "payment" in category:
        return payment_agent.handle_payment_query(query, cart)
    else:
        return ask_gemini(f"User asked: {query}. Respond like a helpful shopping assistant.")
