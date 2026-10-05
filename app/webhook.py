from fastapi import APIRouter
from pydantic import BaseModel

from .customers import CustomerManager


router = APIRouter()

manager = CustomerManager()


class InstagramMessage(BaseModel):
    sender_id: str
    message: str


@router.post("/webhook/instagram")
def instagram_webhook(data: InstagramMessage):

    try:
        response = manager.send_message(
            data.sender_id,
            data.message
        )

        return {
            "status": "ok",
            "sender_id": data.sender_id,
            "response": response
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }