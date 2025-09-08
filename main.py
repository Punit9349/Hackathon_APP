# main.py
from agents.voice_agent import get_user_input
from agents.host_agent import handle_query

def main():
    print("=== AI Shopping Assistant (Gemini) ===")
    print("Type 'exit' to quit.\n")
    while True:
        query = get_user_input()
        if query.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        response = handle_query(query)
        print("Assistant:", response, "\n")

if __name__ == "__main__":
    main()
