import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher()


@dispatcher.message(Command(commands=['start', 'help']))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    start_message = '''
    👋 Welcome to Data Guru Bot! 

    I'm your AI-powered interview preparation assistant, designed to help you ace your Data Science interviews. I provide detailed answers to interview questions across multiple domains of Data Science.

    🎯 How to use this bot:
    Use these commands to practice specific interview topics:

    📌 General Interview Prep
    /general_interview - Common behavioral and professional questions
    /ai_general - General AI industry questions

    📊 Data & Statistics
    /data_analysis - Data analysis and visualization questions
    /statistics - Statistical concepts and methods

    🤖 Machine Learning & Deep Learning
    /machine_learning - Traditional ML algorithms and concepts
    /deep_learning - Neural networks and deep learning architectures

    🔬 Specialized Fields
    /nlp - Natural Language Processing
    /computer_vision - Computer Vision
    /generative_ai - Generative AI and Large Language Models

    💡 Tips for best results:
    - Choose a specific command based on your interview focus
    - Ask clear, focused questions
    - Request examples if needed
    - Follow up for clarification if needed

    🚀 Getting Started:
    1. Select a topic using one of the commands above
    2. Ask your question
    3. Get a detailed, interview-focused response

    ❓ For example:
    After using /statistics, you could ask:
    "Explain p-value in simple terms"
    or
    After /machine_learning:
    "What is the difference between bagging and boosting?"

    Type /help anytime to see this menu again.

    Ready to start your interview prep? Choose a command to begin! 🎯
    '''
    await message.answer(start_message)


@dispatcher.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


