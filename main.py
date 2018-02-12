import telebot
import constants

bot = telebot.TeleBot(constants.token)

#bot.send_message(142794403, "message")

#upd = bot.get_updates()

#last_upd = upd[-1]

#msg = last_upd.message

@bot.message_handler(content_types = ['text'])
def handle_command(message):
    bot.send_message(constants.msg.chat.id, "ez")

bot.polling(none_stop=True, interval=0)