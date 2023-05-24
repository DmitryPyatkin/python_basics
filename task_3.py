"""
    Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.
"""

import telebot
import random

bot = telebot.TeleBot('YOUR_API_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который загадывает число от 1 до 1000. Попробуйте угадать его! Введите /play для начала игры.')

@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, 'Игра началась! Я загадал число от 1 до 1000. Введите свой вариант:')

    number = random.randint(1, 5)
    tries = 0

    @bot.message_handler(func=lambda m: True)
    def guess(message):
        nonlocal tries
        nonlocal number
        try:
            guess_number = int(message.text)
        except ValueError:
            bot.send_message(message.chat.id, 'Некорректный ввод. Попробуйте еще раз.')
            return
            
        tries += 1

        if guess_number > number:
            bot.send_message(message.chat.id, 'Мое число меньше. Попробуйте еще раз.')
        elif guess_number < number:
            bot.send_message(message.chat.id, 'Мое число больше. Попробуйте еще раз.')
        else:
            bot.send_message(message.chat.id, f'Поздравляю! Вы угадали число за {tries} попыток. Чтобы сыграть еще раз, введите команду /play.')
            tries = 0
            number = random.randint(1, 5)

@bot.message_handler(commands=['play'])
def new_game(message):
    play(message)

bot.polling()


