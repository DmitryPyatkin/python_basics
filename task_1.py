"""
    Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
"""

import telebot
import ast

bot = telebot.TeleBot('key')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот для ответа на ваши вопросы! Напишите вопрос, дождитесь ответа, напишите снова для получения ответа') 

@bot.message_handler()
def start(message):
    messages = {
                'first_name' : message.from_user.first_name, 
                'last_name' : message.from_user.last_name,
                'text' : message.text
              }
    
    with open('messages.txt', 'a') as f:
        f.write(str(messages) + '\n')

bot.polling()

# Создает новый файл answers.txt с ответами на сообщения пользователей

import ast
import json

def make_reply_to_messages():
    with open('messages.txt', 'r') as f:
        messages = f.readlines()
    for i in range(len(messages)):
        str = messages[i]
        dictionary = ast.literal_eval(str)
        print(dictionary)
        print('Сообщение:', dictionary['text'])
        answer = input('Введите ответ на сообщение: ')
        dictionary['text'] = answer
        serialized = json.dumps(dictionary, ensure_ascii=False)
        print(serialized)
        with open('answers.txt', 'a') as f:
            f.write(serialized + '\n') 

make_reply_to_messages()  