import telebot
import random
from api import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

facts = {
    1: "Telegram був створений у 2013 році Павлом та Миколою Дуровими.",
    2: "Telegram підтримує ботів, які можуть надсилати не лише текст, а й фотографії, відео та документи.",
    3: "Telegram Bot API дозволяє форматувати повідомлення за допомогою HTML та Markdown."
}

@bot.message_handler(commands=['start'])
def send_zdalova_privet_ky_privetmedved(message):
    bot.send_message(
        message.chat.id,
        "Здалова! Я знаю декілька команд, надішли їх мені, і я розкажу тобі про себе. Наприклад: Привіт; Хто ти?; Як тебе звати?; Що ти вмієш?; Розкажи щось цікаве;"
    )

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Здалова!")

    elif message.text == "Хто ти?":
        bot.send_message(
            message.chat.id,
            "Я твій перший чат-бот на занятті з програмування в Inter-web! Чуть чуть умніше Fable 5.2"
        )

    elif message.text == "Як тебе звати?":
        bot.send_message(
            message.chat.id,
            "Мене звуть VityaUganda408. А як звати тебе?"
        )

    elif message.text == "Що ти вмієш?":
        bot.send_message(
            message.chat.id,
            "Я вмію все, чому мене навчив мій творець!"
        )

    elif message.text == "Розкажи щось цікаве":
        fact = random.choice(list(facts.values()))
        bot.send_message(message.chat.id, fact)

    else:
        bot.send_message(
            message.chat.id,
            "Я тебе не розумію. Напиши щось інше."
        )

bot.polling(none_stop=True, interval=0)