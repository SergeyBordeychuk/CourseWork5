import os

import requests
from celery import shared_task
from config import settings


@shared_task
def send_telegram_message(message, chat_id):
    if chat_id:
        params = {'chat_id': chat_id, 'text': message}
        requests.get(f'{settings.TELEGRAM_API_URL}{os.getenv('TELEGRAM_BOT_API')}/sendMessage', params=params)
