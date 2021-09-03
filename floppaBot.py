import telebot
from WeatherManager import get_weather

bot = telebot.TeleBot("1998668397:AAHYZRNcEVoZR27YeVN717k267-f1B3tTns")

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "Погода":
        bot.send_photo(message.chat.id, get_weather())
    elif message.text == "Расписание":
        bot.send_message(message.chat.id, "Расписание на сегодня: ")
    else:
        bot.send_message(message.chat.id, "Список функций: Погода, Расписание(пока что нет)")

bot.polling(none_stop=True, interval=0)