# FusionBot Image Generator

Telegram-бот на Python, использующий `aiogram` и интеграцию с нейросетью FusionBrain для генерации изображений по текстовым запросам.

## Описание
FusionBot Image Generator — это бот для Telegram, который принимает текстовые запросы от пользователей и генерирует уникальные изображения с помощью искусственного интеллекта. Бот предоставляет удобный интерфейс, где пользователи могут отправить команду и получить визуально привлекательный результат в считанные секунды.
![{7C1FDD54-7159-4ED3-AEF5-AAD31AC91CC3}](https://github.com/user-attachments/assets/48f2b4b2-384f-4ce8-b0b9-a1de98bd2786)

## Функционал
- Прием текстовых запросов на генерацию изображений
- Интеграция с API FusionBrain для обработки запросов и получения изображений
- Поддержка нескольких форматов изображений
- Управление командными запросами с помощью `aiogram`

## Технологии
- **Python** — основной язык разработки
- **aiogram** — библиотека для взаимодействия с Telegram API
- **FusionBrain API** — генерация изображений на основе нейросети

## Установка и настройка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/purplecodev/FusionBot-Image-Generator.git
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Настройте переменные окружения для API FusionBrain и Telegram Token в файле `config.py`
   
   (API FusionBrain - https://fusionbrain.ai/keys/).
5. Запустите бота:
   ```bash
   python bot.py
   ```

## Лицензия
Этот проект лицензирован под MIT License.
