from .customers import CustomerManager
from .database import get_history


customer_id = "test_customer_001"

manager = CustomerManager()

print("=" * 60)
print("HISTORY LOADED FROM DATABASE")

history = get_history(customer_id)

if not history:
    print("No previous history found.")
else:
    for role, message in history:
        print(f"{role}: {message}")


print("\n" + "=" * 60)
print("CURRENT CUSTOMER COUNT:", manager.customer_count())