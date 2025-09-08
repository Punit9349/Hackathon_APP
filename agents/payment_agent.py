# agents/payment_agent.py
from core.gemini_client import ask_gemini
from core.memory import session_state
from datetime import datetime

def handle_payment_query(query: str, cart: list) -> str:
    if not cart:
        return "Your cart is empty. Add some products first."

    if "checkout" in query.lower() or "pay" in query.lower():
        items = ", ".join([p["title"] for p in cart])
        total = sum([p["price"] for p in cart])
        confirm_prompt = f"""
        The user wants to checkout.
        Cart: {items}, Total: ${total}.
        Generate a friendly confirmation message.
        """
        confirmation = ask_gemini(confirm_prompt)

        # Mock checkout
        order = {
            "id": int(datetime.utcnow().timestamp()),
            "items": cart.copy(),
            "total": total,
            "timestamp": datetime.utcnow().isoformat()
        }
        session_state["orders"].append(order)
        cart.clear()

        return confirmation + f"\nOrder placed! Order ID: {order['id']}"

    return "Say 'checkout' to place your order."
