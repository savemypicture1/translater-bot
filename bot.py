import telebot
import os
import dotenv
from googletrans import Translator

dotenv.load_dotenv()
TOKEN = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(TOKEN)


def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='en')

    return translated_text.text


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'LEARN THE ENGLISH! BLEAT!!!')


@bot.message_handler(func=lambda message: True)
def translate_message(message):
    user_text = message.text

    translated_text = translate_text(user_text)
    bot.reply_to(message, f'{translated_text}')


bot.polling(none_stop=True)
