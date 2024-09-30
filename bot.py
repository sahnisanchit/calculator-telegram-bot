from config import *
import os
import telebot,openai
ChatStr=''
#to get results according to last chat, we use this str to save our chat in chatstr
def ChatModel(prompt):
    global ChatStr
    openai.api_key=OPENAI_KEY
    ChatStr+=f"Sanchit :{prompt}\n Pasmud: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ChatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    print(response)
    ChatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text'] 
bot=telebot.TeleBot(BOT_API)
@bot.message_handler(['start'])
def start(message):
    print(message)
    bot.reply_to(message,f"Hello Welcome {os.getlogin()} here")
@bot.message_handler() 
def chat(message):
    try:
        reply = ChatModel(message.text)
        bot.reply_to(message,reply)
    except Exception as e:
        print(e)
        bot.reply_to(message.text,e)
    
    
print("Bot Started..")
bot.polling() 