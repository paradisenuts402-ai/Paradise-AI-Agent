from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.customers import CustomerManager
from app.webhook import router as webhook_router

app = FastAPI(title="Paradise AI Agent")
app.include_router(webhook_router)

manager = CustomerManager()


class ChatMessage(BaseModel):
    customer_id: str
    message: str


HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Paradise AI Agent</title>

    <style>

        body {
            margin: 0;
            font-family: Tahoma, Arial, sans-serif;
            background: #f5f5f5;
        }

        .container {
            max-width: 800px;
            margin: 30px auto;
            background: white;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 5px 25px rgba(0,0,0,.08);
        }

        .header {
            padding: 20px;
            background: #111;
            color: white;
            text-align: center;
        }

        .header h2 {
            margin: 0 0 6px;
        }

        .header small {
            opacity: .7;
        }

        .customer {
            padding: 15px;
            border-bottom: 1px solid #eee;
            background: #fafafa;
        }

        .customer label {
            font-size: 13px;
            display: block;
            margin-bottom: 7px;
        }

        .customer input {
            width: 100%;
            box-sizing: border-box;
            padding: 11px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }

        #chat {
            height: 450px;
            overflow-y: auto;
            padding: 20px;
        }

        .message {
            margin-bottom: 15px;
            padding: 12px 15px;
            border-radius: 12px;
            line-height: 1.8;
            white-space: pre-wrap;
        }

        .user {
            background: #e8f0fe;
            margin-left: 80px;
        }

        .bot {
            background: #f1f1f1;
            margin-right: 80px;
        }

        .label {
            font-size: 12px;
            opacity: .6;
            margin-bottom: 4px;
        }

        .input-area {
            display: flex;
            gap: 10px;
            padding: 15px;
            border-top: 1px solid #eee;
        }

        .input-area input {
            flex: 1;
            padding: 14px;
            border: 1px solid #ddd;
            border-radius: 10px;
            font-size: 15px;
            outline: none;
        }

        button {
            padding: 0 25px;
            border: none;
            border-radius: 10px;
            background: #111;
            color: white;
            cursor: pointer;
            font-size: 15px;
        }

        button:disabled {
            opacity: .5;
        }

    </style>

</head>


<body>

<div class="container">

    <div class="header">

        <h2>🤖 Paradise AI Agent</h2>

        <small>
            Local Customer Chat
        </small>

    </div>


    <div class="customer">

        <label>
            شناسه مشتری
        </label>

        <input
            id="customerId"
            value="customer_001"
            placeholder="مثلاً customer_001"
        >

    </div>


    <div id="chat"></div>


    <div class="input-area">

        <input
            id="message"
            placeholder="پیام مشتری را بنویسید..."
            autocomplete="off"
        >

        <button
            id="send"
            onclick="sendMessage()"
        >
            ارسال
        </button>

    </div>

</div>


<script>

const input =
    document.getElementById("message");

const button =
    document.getElementById("send");

const customerId =
    document.getElementById("customerId");

const chat =
    document.getElementById("chat");


input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    }
);


function addMessage(text, type, label) {

    const box =
        document.createElement("div");

    box.className =
        "message " + type;

    const labelElement =
        document.createElement("div");

    labelElement.className =
        "label";

    labelElement.textContent =
        label;

    const textElement =
        document.createElement("div");

    textElement.textContent =
        text;

    box.appendChild(labelElement);
    box.appendChild(textElement);

    chat.appendChild(box);

    chat.scrollTop =
        chat.scrollHeight;
}


async function sendMessage() {

    const message =
        input.value.trim();

    const id =
        customerId.value.trim();


    if (!message || !id) {
        return;
    }


    input.value = "";

    button.disabled = true;


    addMessage(
        message,
        "user",
        "مشتری " + id
    );


    try {

        const response =
            await fetch("/chat", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    customer_id: id,

                    message: message

                })

            });


        const data =
            await response.json();


        if (data.error) {

            addMessage(
                data.error,
                "bot",
                "خطا"
            );

        } else {

            addMessage(
                data.response,
                "bot",
                "Paradise AI"
            );

        }

    } catch (error) {

        addMessage(
            "ارتباط با Agent برقرار نشد.",
            "bot",
            "خطا"
        );

    }


    button.disabled = false;

    input.focus();
}


</script>

</body>

</html>
"""


@app.get("/chat", response_class=HTMLResponse)
def chat_page():

    return HTML


@app.post("/chat")
def chat_api(message: ChatMessage):

    try:

        response = manager.send_message(
            message.customer_id,
            message.message
        )

        return {
            "response": response
        }

    except Exception as e:

        return {
            "error": str(e)
        }