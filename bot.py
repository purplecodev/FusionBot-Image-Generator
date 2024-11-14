import asyncio
from aiogram import Bot, Dispatcher
import logging
from config import BOT_TOKEN
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import text_to_image
# Запуск бота
async def main():
    # Объект бота
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Диспетчер
    dp = Dispatcher()
    dp.include_routers(text_to_image.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())