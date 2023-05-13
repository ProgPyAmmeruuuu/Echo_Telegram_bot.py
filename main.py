import telebot

bot = telebot.TeleBot('Your_token_ot_@botfather_in_the_telegram')

@bot.message_handler(func=lambda message: message.text == message.text)
#func echo
def echo(message):
    #bot will send echo message
    bot.send_message(message.chat.id, message.text)

    

bot.polling(none_stop=True)
