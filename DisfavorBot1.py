import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.filters.command import Command
from datetime import date
from Bot_tokken import TOKEN

dp = Dispatcher() # Диспетчер

logging.basicConfig(level=logging.INFO) # Включаем логирование, чтобы не пропустить важные сообщения

@dp.message(Command("info")) # Хэндлер на команду /info
async def cmd_info(message: Message):
    start_bot_time = date(2025, 1, 11)
    await message.answer(f"Бот создан: {start_bot_time}")
    

@dp.message(Command("start")) # Хэндлер на команду /start
async def cmd_start(message: Message):
    kb = [
        [
            types.InlineKeyboardButton(text="Продолжить", callback_data='next_info')
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Привет! это мой бот-визитка', reply_markup=keyboard)

@dp.callback_query(F.data == 'next_info') # Кнопка "Продолжить"
async def plus_word(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Обо мне", callback_data='about_me')],
        [types.InlineKeyboardButton(text="Stepik", url='https://stepik.org/users/714567549/profile'),
        types.InlineKeyboardButton(text="GitHub", url='https://github.com/kilocod3')],
        [types.InlineKeyboardButton(text="О боте", callback_data='profil'),]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Что ты хочешь знать?', reply_markup=keyboard)
    
@dp.callback_query(F.data == "about_me") # О себе
async def about_me_callback(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Codewars", url='https://www.codewars.com/users/kilocod3')],
        [types.InlineKeyboardButton(text="Вернуться", callback_data='next_info')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Дата написания текста: 15.01.2025.\n Студент 4 курса.\n Специальностей: "Прикладная математика и информатика" и "Программная инженерия"', reply_markup=keyboard)
    
@dp.callback_query(F.data == "profil")
async def about_me_callback(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Вернуться", callback_data='next_info')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Работает как бот-визитка', reply_markup=keyboard)   

async def main(): # Запуск процесса поллинга новых апдейтов
    bot = Bot(token=TOKEN) # Объект бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())