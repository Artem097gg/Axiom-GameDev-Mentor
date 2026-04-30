import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
try:
    from lessons import PHYSICS_LESSON
except ImportError:
    PHYSICS_LESSON = "Error: lessons.py file not found. Please create it in the same directory."

API_TOKEN = 'BOT_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    welcome_msg = (
        "✨ **Welcome to Axiom GameDev**\n\n"
        "I am your academic mentor for Unity Engine. I am here to help you "
        "understand the technical depth behind game mechanics.\n\n"
        "**Available Educational Modules:**\n"
        "🔹 /explainphysic - Unity Physics Engine (PhysX)\n"
        "🔹 /about - Project Vision & Mission\n"
        "🔹 /games - Developer Portfolio\n\n"
        "*Phase 3: Computational Mathematics is currently in research.*"
    )
    await message.answer(welcome_msg, parse_mode="Markdown")

@dp.message_handler(commands=['explainphysic'])
async def cmd_physic(message: types.Message):
    await message.answer(PHYSICS_LESSON, parse_mode="Markdown")

@dp.message_handler(commands=['about'])
async def cmd_about(message: types.Message):
    about_text = (
        "🛡 **About Axiom GameDev**\n\n"
        "This project is a technical showcase for the **Lester B. Pearson International Scholarship** "
        "at the University of Toronto.\n\n"
        "It focuses on Bridging the gap between high-school knowledge and professional game architecture."
    )
    await message.answer(about_text, parse_mode="Markdown")

@dp.message_handler(commands=['games'])
async def cmd_games(message: types.Message):
    await message.answer("🎮 **Check out my game projects on itch.io:**\n[https://a-dev-k.itch.io/]")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
