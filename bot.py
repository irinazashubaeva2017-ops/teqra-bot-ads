import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import WebAppInfo
import database # Подключаем наш файл с базой

API_TOKEN = '8280760100:AAGlB3ENTdxtVsZN0NGBVbTvoICAoMtlp2s'

# Настройка логирования (чтобы видеть ошибки в консоли)
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Запускаем создание базы данных при старте
database.init_db()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Сохраняем пользователя в базу
    database.add_user(message.from_user.id, message.from_user.username)
    
    # Кнопка для Mini App
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Пока поставим гугл для теста, потом заменим на твою ссылку
    web_app = WebAppInfo(url="https://google.com") 
    markup.add(types.KeyboardButton("Открыть TEQRA Ads", web_app=web_app))
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! ⚡️\n"
        "Добро пожаловать в рекламную платформу TEQRA.\n"
        "Нажми на кнопку ниже, чтобы войти в Mini App.",
        reply_markup=markup
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)