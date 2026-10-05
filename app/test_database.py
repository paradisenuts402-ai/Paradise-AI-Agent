from .customers import CustomerManager
from .database import get_history


manager = CustomerManager()

customer_id = "test_customer_001"

print("=" * 60)
print("SENDING MESSAGE")

answer = manager.send_message(
    customer_id,
    "سلام، قیمت تخمه آفتابگردان خارجی چنده؟"
)

print("\nAGENT:")
print(answer)


print("\n" + "=" * 60)
print("DATABASE HISTORY")

history = get_history(customer_id)

for role, message in history:
    print(f"{role}: {message}")