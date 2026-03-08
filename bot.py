import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import WebAppInfo
from aiohttp import web
import database

# ВСТАВЬ СВОЙ ТОКЕН НИЖЕ
API_TOKEN = 'ТВОЙ_ТОКЕН_ИЗ_BOTFATHER'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Инициализируем базу данных TEQRA
database.init_db()

# --- Блок для Render (исправляет ошибку портов) ---
async def handle(request):
    return web.Response(text="TEQRA Bot is Live!")

app = web.Application()
app.router.add_get("/", handle)

async def on_startup(dp):
    runner = web.AppRunner(app)
    await runner.setup()
    # Render дает порт автоматически, мы его подхватываем
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Web server started on port {port}")
# ------------------------------------------------

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    database.add_user(message.from_user.id, message.from_user.username)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # ПРОВЕРЬ ЭТУ ССЫЛКУ! Она должна вести на твой GitHub Pages
    web_app_url = "https://irinazashubaeva2017-ops.github.io/teqra-bot-ads/"
    markup.add(types.KeyboardButton("Открыть TEQRA Ads ⚡️", web_app=WebAppInfo(url=web_app_url)))
    
    await message.answer(
        f"С праздником 8 марта! 🌷\n"
        f"Бот бренда TEQRA запущен и готов к работе.\n"
        f"Нажми кнопку ниже, чтобы открыть Mini App.",
        reply_markup=markup
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
