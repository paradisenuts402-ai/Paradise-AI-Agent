from .ai_agent import ask_ai


class Conversation:
    def __init__(self):
        self.history = []

    def send(self, customer_message):
        self.history.append({
            "role": "user",
            "content": customer_message
        })

        # فعلاً تاریخچه را به شکل ساده به Agent می‌دهیم
        conversation_text = "\n".join(
            f"{item['role']}: {item['content']}"
            for item in self.history
        )

        answer = ask_ai(conversation_text)

        self.history.append({
            "role": "assistant",
            "content": answer
        })

        return answer