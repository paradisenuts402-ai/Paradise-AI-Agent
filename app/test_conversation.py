from conversation import Conversation


chat = Conversation()

messages = [
    "سلام، قیمت تخمه آفتابگردان خارجی چنده؟",
    "۲۰ کیلو می‌خوام.",
    "برای مغازه‌ست.",
    "قیمت عمده‌اش رو حساب کن."
]


for i, message in enumerate(messages, 1):
    print("\n" + "=" * 60)
    print(f"MESSAGE {i}")
    print("CUSTOMER:")
    print(message)

    answer = chat.send(message)

    print("\nAGENT:")
    print(answer)