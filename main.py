import telebot
#from telegram.ext import Application,commandhandler,messagehandler,filters,contexttypes
Token ='6525699111:AAEYZYJpY8dkY5x0VMOiwq13mUVObNHrzTo'
bot=telebot.TeleBot(Token)
@bot.message_handler(["start"])
def start(message):
    bot.reply_to(message,"Geet ji Wassup? Please use this bot as a calculator")

@bot.message_handler()
def custom(message):
    try:
        msg=eval(message.text.strip())
    except Exception as e:
        msg="I'm unable to evaluate it . Please write something sensible"
    bot.reply_to(message,msg)
        
bot.polling()