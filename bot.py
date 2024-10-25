import asyncio
import logging
from prompts import PROMPTS
from utils.message_formatter import MessageFormatter
import sys
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
import google.generativeai as genai
import time
import re
from aiogram import F
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
        history=[
            {"role": "model", "parts": f"Hello Gemini"}
        ]
    )


TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher()


@dispatcher.message(Command(commands=['start', 'help']))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    
    await message.answer(PROMPTS['start_message'])


@dispatcher.message(Command(commands=['general_interview']))
async def general_interview_handler(message: Message):
    response = chat.send_message(PROMPTS['general_interview_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)

@dispatcher.message(Command(commands=['ai_general']))
async def ai_general_handler(message: Message):
    response = chat.send_message(PROMPTS['ai_general_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['data_analysis']))
async def data_analysis_handler(message: Message):
    response = chat.send_message(PROMPTS['data_analysis_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['statistics']))
async def statistics_handler(message: Message):
    response = chat.send_message(PROMPTS['statistics_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['machine_learning']))
async def machine_learning_handler(message: Message):
    response = chat.send_message(PROMPTS['machine_learning_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['deep_learning']))
async def deep_learning_handler(message: Message):
    response = chat.send_message(PROMPTS['deep_learning_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['nlp']))
async def nlp_handler(message: Message):
    response = chat.send_message(PROMPTS['nlp_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['computer_vision']))
async def computer_vision_handler(message: Message):
    response = chat.send_message(PROMPTS['computer_vision_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


@dispatcher.message(Command(commands=['generative_ai']))
async def generative_ai_handler(message: Message):
    response = chat.send_message(PROMPTS['generative_ai_prompt'])
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)

@dispatcher.message(F.text & ~F.command)
async def query_handler(message: Message) -> None:
    
    response = chat.send_message(message.text)
    messages = MessageFormatter.split_message(response.text)
    for msg in messages:
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN_V2)
        time.sleep(1)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # And the run events dispatching
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


