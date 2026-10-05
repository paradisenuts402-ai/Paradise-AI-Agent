from ai_agent import build_knowledge


def mock_ai(customer_message):
    knowledge = build_knowledge()

    print("\n--- CUSTOMER ---")
    print(customer_message)

    print("\n--- KNOWLEDGE LOADED ---")
    print(f"Products: {len(knowledge['products']['products'])}")
    print(f"FAQs: {len(knowledge['faq']['faqs'])}")

    print("\n--- MOCK RESPONSE ---")
    print("سیستم آماده اتصال به OpenAI است.")


if __name__ == "__main__":
    mock_ai("قیمت تخمه آفتابگردان خارجی چنده؟")