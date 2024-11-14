import asyncio
import base64
import os
from aiogram import Router
from random import randint
from aiogram.types import FSInputFile
from aiogram import types
from utils.text2image_api import Text2ImageAPI
from config import API_KEY, SECRET_KEY
router = Router()

@router.message()
async def handle_message(message: types.Message):
    if message.text == '/start':
        await message.answer('Здравствуй. Напиши текст по которому я должен сгенерировать картинку')
    else:
        print('start handling...')
        loading_msg = await message.answer("Генерация изображения: 0%")

        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY) # fusionbrain.ai
        model_id = api.get_model()
        uuid = api.generate(message.text, model_id, style=1)
        attempts = 10
        for attempt in range(attempts):
            progress = int((attempt + 1) / attempts * 100)
            await asyncio.sleep(4)
            await loading_msg.edit_text(f"Генерация изображения: {progress}%")
        for _ in range(2):
            for dots in [".", "..", "..."]:
                await loading_msg.edit_text(f"Генерация изображения 100%{dots}")
                await asyncio.sleep(1)
        await loading_msg.delete()
        images = api.check_generation(uuid)
        image_base64 = images[0]
        image_data = base64.b64decode(image_base64)
        random_int = randint(0, 1000)

        with open(f"image{random_int}.jpg", "wb") as file:
            file.write(image_data)
        result = FSInputFile(f"image{random_int}.jpg")
        await message.answer_photo(result)
        os.remove(f"image{random_int}.jpg")