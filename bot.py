import telebot
import finder
from telebot import types
from playwright.sync_api import sync_playwright

bot = telebot.TeleBot("")

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Start Bot"),
    telebot.types.BotCommand("/help", "Help"),
    telebot.types.BotCommand("/model", "Choose bike model")
])


@bot.message_handler(commands=['start'])
def send_start(message):
    with sync_playwright() as playwright:
        res = finder.run(playwright)
    bot.reply_to(message, res)

    markup = types.InlineKeyboardMarkup()
    button_to_site = types.InlineKeyboardButton(text="See Bike", url=finder.url)
    markup.add(button_to_site)
    bot.send_message(message.chat.id, "Go to CANYON site?", reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Hi! This Bot can help you to check CANYON bikes in stock. You can choose model and size")


@bot.message_handler(commands=['model'])
def choose_model(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Speedmax CFR", callback_data="Speedmax CFR")
    btn2 = types.InlineKeyboardButton("Grizl CF SLX", callback_data="Grizl CF SLX")
    btn3 = types.InlineKeyboardButton("Ultimate CF SL", callback_data="Ultimate CF SL")
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Choose your model", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Speedmax CFR":
        bot.send_message(message.chat.id, text="Not ready yet, choose another model")
    elif message.text == "Grizl CF SLX":
        bot.send_message(message.chat.id, text="Not ready yet, choose another model")
    elif message.text == "Ultimate CF SL":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="XS", callback_data="XS"),
        btn2 = types.InlineKeyboardButton(text="S", callback_data="S"),
        btn3 = types.InlineKeyboardButton(text="M", callback_data="M"),
        btn4 = types.InlineKeyboardButton(text="L", callback_data="L")

        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Choose your size", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
