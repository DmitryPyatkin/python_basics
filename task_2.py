"""
    Задача 2. Напишите программу, которая позволяет считывать из файла вопрос,
    отвечать на него и отправлять ответ обратно пользователю.
"""

import telebot
import ast

bot = telebot.TeleBot('key')

def find_question(first_name, last_name):
    with open('messages.txt', 'r') as f:
        messages = f.readlines()
    for i in range(len(messages)):
        str = messages[i]
        dictionary = ast.literal_eval(str)
        if first_name == dictionary['first_name'] and last_name == dictionary['last_name']:
            return dictionary['text']

def find_answer(first_name, last_name):
    with open('answers.txt', 'r') as f:
        answers = f.readlines()
    for i in range(len(answers)):
        str = answers[i]
        dictionary = ast.literal_eval(str)
        if first_name == dictionary['first_name'] and last_name == dictionary['last_name']:
            return dictionary['text']

@bot.message_handler()
def reply(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    answer = find_answer(first_name, last_name)
    question = find_question(first_name, last_name)
    bot.reply_to(message, f'Сообщение пользователя: {question}\nОтвет на сообщение: {answer}')

bot.polling()