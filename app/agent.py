import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def find_product(product_name):
    data = load_json("products.json")

    product_name = product_name.strip().lower()

    for product in data["products"]:
        if product["name"].lower() in product_name:
            return product

    return None


def answer(message):
    message = message.strip()

    product = find_product(message)

    if product:
        response = f"🌱 {product['name']}\n"

        if "retail_price" in product:
            response += f"قیمت خرده: {product['retail_price']:,} تومان"

        if "wholesale_price" in product:
            response += f"\nقیمت عمده: {product['wholesale_price']:,} تومان"

        return response

    message_lower = message.lower()

    if "عمده" in message_lower:
        return (
            "بله 🌱 فروش عمده داریم.\n"
            "برای دریافت شرایط همکاری، شماره تماس‌تون رو ارسال کنید "
            "تا کارشناس فروش با شما تماس بگیره."
        )

    if "قیمت" in message_lower:
        return (
            "حتماً 🌱 نام محصول موردنظرتون رو بفرستید "
            "تا قیمت دقیق رو اعلام کنم."
        )

    return (
        "سلام 🌱\n"
        "در خدمتم. لطفاً نام محصول یا سؤال‌تون رو بفرستید "
        "تا راهنمایی‌تون کنم."
    )