import os

import telebot

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))


def notification:
    bot.send_message(chat_id='', text=f'')