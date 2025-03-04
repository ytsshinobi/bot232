import random
import string
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
GROUP_LINK = "https://t.me/+2oxLmAzwvTM4MDgy"
current_password = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

def generate_password():
    """Tasodifiy 6 xonali parol yaratish"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

async def update_password():
    global current_password
    while True:
        current_password = generate_password()
        await bot.send_message(ADMIN_ID, f"Yangi maxfiy parol: {current_password}")
        await asyncio.sleep(7 * 24 * 60 * 60)  # Har 7 kunda yangilanadi

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Salom! Guruh havolasini olish uchun maxfiy parolni yuboring.")

@dp.message()
async def check_password(message: Message):
    if message.text == current_password:
        await message.answer(f"To‘g‘ri! Guruh havolasi: {GROUP_LINK}")
    else:
        await message.answer("Noto‘g‘ri parol. Qaytadan urinib ko‘ring.")

async def main():
    asyncio.create_task(update_password())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
