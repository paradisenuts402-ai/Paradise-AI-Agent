import requests


URL = "http://127.0.0.1:8000/webhook/instagram"


def send_dm(sender_id, message):

    payload = {
        "sender_id": sender_id,
        "message": message
    }

    response = requests.post(
        URL,
        json=payload,
        timeout=60
    )

    print("\n" + "=" * 60)
    print("INSTAGRAM DM")
    print("SENDER:", sender_id)
    print("MESSAGE:", message)

    print("\nAGENT RESPONSE:")

    try:
        print(response.json())
    except Exception:
        print(response.text)


print("Paradise Instagram Simulator")
print("Type 'exit' to quit.\n")


while True:

    sender_id = input("Instagram User ID: ").strip()

    if sender_id.lower() == "exit":
        break

    message = input("DM Message: ").strip()

    if message.lower() == "exit":
        break

    send_dm(sender_id, message)