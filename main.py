from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import openai
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "6170111729:AAEF9A2mEg8AOz8znJ5K8tPH6RCWmGUD5Wk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

openai.api_key = "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"

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name
    logging.info(f'{user_name}')
    await message.reply(f"Привет, {user_name}! Меня зовут Гена, чем я могу тебе помочь?")

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
    model='text-davinci-003',
    prompt= message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[' You:']
)
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)