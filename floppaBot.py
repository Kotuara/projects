import telebot
from WeatherManager import get_weather

bot = telebot.TeleBot("Token")

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "Погода":
        bot.send_photo(message.chat.id, get_weather())
    elif message.text == "Расписание":
        bot.send_message(message.chat.id, "Расписание на сегодня: ")
    else:
        bot.send_message(message.chat.id, "Список функций: Погода, Расписание(пока что нет)")

bot.polling(none_stop=True, interval=0)
