from .conversation import Conversation
from .database import save_message, get_history


class CustomerManager:
    def __init__(self):
        self.customers = {}

    def get_customer(self, customer_id):
        if customer_id not in self.customers:
            conversation = Conversation()

            history = get_history(customer_id)

            for role, message in history:
                conversation.history.append({
                    "role": role,
                    "content": message
                })

            self.customers[customer_id] = conversation

        return self.customers[customer_id]

    def send_message(self, customer_id, message):
        conversation = self.get_customer(customer_id)

        save_message(
            customer_id,
            "user",
            message
        )

        answer = conversation.send(message)

        save_message(
            customer_id,
            "assistant",
            answer
        )

        return answer

    def customer_count(self):
        return len(self.customers)