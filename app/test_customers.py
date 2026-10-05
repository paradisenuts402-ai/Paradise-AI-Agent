from .customers import CustomerManager

manager = CustomerManager()


print("=" * 60)
print("CUSTOMER A")

print(
    manager.send_message(
        "customer_A",
        "سلام، قیمت تخمه آفتابگردان خارجی چنده؟"
    )
)

print(
    manager.send_message(
        "customer_A",
        "۲۰ کیلو می‌خوام."
    )
)


print("\n" + "=" * 60)
print("CUSTOMER B")

print(
    manager.send_message(
        "customer_B",
        "قیمت پسته احمدآقایی چنده؟"
    )
)

print(
    manager.send_message(
        "customer_B",
        "۵ کیلو می‌خوام."
    )
)


print("\n" + "=" * 60)
print("CUSTOMER COUNT:", manager.customer_count())