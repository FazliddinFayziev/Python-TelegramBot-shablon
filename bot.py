# Before starting coding we need some libraries
#such as: 
import telebot # pip install python-telegram-bot/pip install TelegramAPI/pyTelegramBotAPI
from telebot import types

TOKEN='your token which was given by botfather'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','START'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('button name_1')
    item2 = types.KeyboardButton('button name_2')
    markup.add(item1,item2)
    
    bot.send_message(message.chat.id,'Hello,{0.first_name}!'.format(message.from_user),reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'button name_1':
             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
             item1 = types.KeyboardButton('1')
             item2 = types.KeyboardButton('2')
             markup.add(item1, item2)
            
             bot.send_message(message.chat.id,'button name_2',reply_markup=markup)
        
        elif message.text == '1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1📘')
            item2 = types.KeyboardButton('2📘')
            markup.add(item1, item2)
           
            bot.send_message(message.chat.id,'1',reply_markup=markup)
        
# you can add other buttons with elif again and again

bot.polling(none_stop=True)
            
            

            
    

