import asyncio
import aiohttp

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8368942269:AAGlgzhFAomt3OtyFKn1pcNPRvm9FUqJLTQ"

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        "Salom 👋\n"
        "Urganchdagi 7 kunlik ob-havoni bilish uchun /obhavo tugmasini bosing"
    )


@dp.message(Command("obhavo"))
async def obhavo_handler(message: Message):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=41.55&longitude=60.63"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=Asia/Tashkent"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    kun = data["daily"]["time"]
    kunduzi = data["daily"]["temperature_2m_max"]
    kechasi = data["daily"]["temperature_2m_min"]

    text = "⛅️ Urganch uchun 7 kunlik ob-havo:\n\n"
    for i in range(7):
        text += f"sana>>>{kun[i]}  kunduzi>>> {kunduzi[i]}°C  kechasi>>> {kechasi[i]}°C \n"

        from aiogram.types import FSInputFile


    await message.answer(text)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


