import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'BOT_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    welcome_msg = (
        "✨ **Welcome to Axiom GameDev**\n\n"
        "I am your dedicated mentor for mastering the Unity Engine. "
        "My goal is to simplify complex game development concepts for you.\n\n"
        "**Current status:** Project Architecture Phase.\n\n"
        "**Available Commands:**\n"
        "🔹 /about - Project Vision & Mission\n"
        "🔹 /games - Developer Portfolio\n\n"
        "*Educational modules (Physics, Math, C#) are currently under development.*"
    )
    await message.answer(welcome_msg, parse_mode="Markdown")

@dp.message_handler(commands=['about'])
async def cmd_about(message: types.Message):
    about_text = (
        "🛡 **Axiom GameDev: Portfolio Project**\n\n"
        "This autonomous mentor is developed as a technical submission for the "
        "**Lester B. Pearson International Scholarship** at the University of Toronto.\n\n"
        "The project aims to lower the entry barrier for beginner developers by providing "
        "structured, high-fidelity guidance on game engine mechanics."
    )
    await message.answer(about_text, parse_mode="Markdown")

@dp.message_handler(commands=['games'])
async def cmd_games(message: types.Message):
    await message.answer("🎮 **Check out my game projects on itch.io:**\n[Your Link Here]")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
