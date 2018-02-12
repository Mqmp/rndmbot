import telebot
import constants

token = "286888171:AAGb0YLpt_aXbeI3DvjTz7TlASwO0nq49-8"

bot = telebot.TeleBot(constants.token)

upd = bot.get_updates()
if upd == []:
    while upd == []:
        upd = bot.get_updates()
        
last_upd = upd[-1]

msg = last_upd.message
