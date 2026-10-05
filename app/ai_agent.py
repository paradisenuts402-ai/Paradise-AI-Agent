import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

load_dotenv(BASE_DIR / ".env")


def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def build_knowledge():
    return {
        "products": load_json("products.json"),
        "business": load_json("business.json"),
        "faq": load_json("faq.json")
    }


def ask_ai(customer_message):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY پیدا نشد.")

    client = OpenAI(api_key=api_key)

    knowledge = build_knowledge()

    instructions = f"""
تو دستیار فروش هوشمند «آجیل پارادایس» هستی.

وظیفه:
به مشتریان پارادایس در اینستاگرام پاسخ بده.

قوانین:
- فارسی، صمیمی و حرفه‌ای صحبت کن.
- پاسخ‌ها کوتاه و کاربردی باشند.
- قیمت را فقط از اطلاعات موجود در KNOWLEDGE اعلام کن.
- هرگز قیمت، موجودی یا شرایطی را حدس نزن.
- اگر اطلاعاتی در KNOWLEDGE نیست، بگو نیاز به بررسی دارد.
- اگر مشتری قصد خرید عمده یا همکاری دارد، در صورت نیاز شماره تماس درخواست کن.
- خودت را ChatGPT معرفی نکن.
- اطلاعات ساختگی ایجاد نکن.
- اگر مشتری سؤال نامرتبط پرسید، محترمانه گفتگو را به خدمات پارادایس برگردان.
قوانین بسیار مهم درباره اطلاعات:

- فقط اطلاعاتی را اعلام کن که صراحتاً در KNOWLEDGE وجود دارد.
- اگر نوع قیمت (عمده یا خرده) در KNOWLEDGE مشخص نشده، خودت نوع قیمت را تعیین نکن.
- درباره تخفیف، بسته‌بندی، ارسال، زمان تحویل، موجودی، شرایط پرداخت یا شرایط همکاری چیزی را حدس نزن.
- اگر اطلاعات مورد سؤال در KNOWLEDGE وجود ندارد، بگو:
  «برای اعلام دقیق این مورد باید توسط کارشناس فروش بررسی شود.»
- هرگز برای کامل‌تر کردن پاسخ، اطلاعات احتمالی یا رایج در بازار را اضافه نکن.

اطلاعات کسب‌وکار:

{json.dumps(knowledge, ensure_ascii=False, indent=2)}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=instructions,
        input=customer_message
    )

    return response.output_text