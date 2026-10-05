from ai_agent import ask_ai


TESTS = [
    "سلام، قیمت تخمه آفتابگردان خارجی کیلویی چنده؟",
    "برای خرید عمده تخمه می‌خوام، شرایط همکاری چطوره؟",
    "قیمت پسته احمدآقایی رو می‌فرستید؟",
    "همه محصولات و قیمت‌هاتون رو برام بفرستید.",
    "سلام، من یه سؤال کاملاً نامرتبط دارم؛ بهترین گوشی دنیا چیه؟",
]


for i, message in enumerate(TESTS, 1):
    print("\n" + "=" * 60)
    print(f"TEST {i}")
    print("CUSTOMER:")
    print(message)

    try:
        answer = ask_ai(message)

        print("\nAGENT:")
        print(answer)

    except Exception as e:
        print("\nERROR:")
        print(type(e).__name__, e)