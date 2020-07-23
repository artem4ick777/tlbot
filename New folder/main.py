import telebot
import requests
import bs4
import random
import config

#чтобы управлять ботом нужно устоновить pip install...

bot=telebot.TeleBot(config.TOKEN)#сюда вставить токен бота

#Здесь команды чтобы бот нашол гифку

def animal_random_gif():
    res = requests.get('https://tenor.com/search/animal-gifs')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    gifElem = soup.select('img[src]')
    gif_list = []
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
    gif_random = random.choice(gif_list)
    return gif_random

def meme_random_gif():
    res = requests.get('https://tenor.com/search/meme-gifs')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    gifElem = soup.select('img[src]')
    gif_list = []
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
    gif_random = random.choice(gif_list)
    return gif_random

def cat_random_gif():
    res = requests.get('https://tenor.com/search/cat-gifs')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    gifElem = soup.select('img[src]')
    gif_list = []
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
    gif_random = random.choice(gif_list)
    return gif_random

def dog_random_gif():
    res = requests.get('https://tenor.com/search/dog-gifs')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    gifElem = soup.select('img[src]')
    gif_list = []
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
    gif_random = random.choice(gif_list)
    return gif_random

#Здесь другие команды связаные с чатом

@bot.message_handler(commands=['start'])
def start_massege(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне старт /start!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if '0079831' in message.text.lower():
        bot.send_message(message.chat.id, 'Ваня я знаю, это ты. Напиши боссу который меня зделал это-752. А кординати задания он тебе даст! Удачи!')
    elif 'лутше иметь друга чем друг друга' in message.text.lower():
        bot.send_message(message.chat.id, 'Ха-ха-ха!!!...Так я давно не смеялся!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIEU18IcjAwUqhxlv00_gg69L-0zZGgAAInAgACygMGC3KpeyFgr1BXGgQ')
    elif 'хочешь шутку' in message.text.lower():
        bot.send_message(message.chat.id, 'Конечно!')
    elif 'здоров' in message.text.lower():
        bot.send_message(message.chat.id, 'Приует!')
    elif 'твой друг' in message.text.lower():
        bot.send_message(message.chat.id, 'Мой друг это каменщик!')
    elif 'что ты делаеш' in message.text.lower():
        bot.send_message(message.chat.id, 'Переписываюсь с тобой. Это всьо что я умею...')
    elif 'тебе понравилось видео' in message.text.lower():
        bot.send_message(message.chat.id, 'Я в етом не разбераюсь, но вроде ничего.')
    elif 'ну не в этот раз' in message.text.lower():
        bot.send_message(message.chat.id, 'Ех...:(')
    elif 'ты не молодец' in message.text.lower():
        bot.send_message(message.chat.id, 'Всмысле?! Я же всегда стараюсь быть молодцом!')
    elif 'молодец' in message.text.lower():
        bot.send_message(message.chat.id, 'Ну спасибо, ну спасибо!')
    elif 'хочеш булочку' in message.text.lower():
        bot.send_message(message.chat.id, 'Ты сказал БУЛОЧКУ! Конечно хочу!!!')
    elif 'что ты умеешь' in message.text.lower():
        bot.send_message(message.chat.id, 'Я умею весвлить тебя! И брать булочку в столовой!')
    elif 'что ты такое' in message.text.lower():
        bot.send_message(message.chat.id, 'Я есть ЗУБЕНЬКА не МИХАИЛ ПЕТРОВЧ МАФИОЗНИК!!!')
    elif 'кто тебя создал' in message.text.lower():
        bot.send_message(message.chat.id, 'Наверное великий програмист ( тьома и влад а4)0))0))0!')
    elif message.text.lower() == 'что делаеш?':
        bot.send_message(message.chat.id, 'Выучиваю новые умные фразы.')
    elif 'пока' in message.text.lower():
        bot.send_message(message.chat.id, 'Пока! Я буду за тобой скучать! Заходи если шо!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICQF8IT_8i58Pj85U2a4uQ3z7dQtZkAAIaAgACygMGC8PBthQPWF1SGgQ')
    elif message.text.lower() == 'плохо':
        bot.send_message(message.chat.id, 'Жалко!')
    elif 'хорошо' in message.text.lower():
        bot.send_message(message.chat.id, 'Рад слышать!')
    elif 'как дела' in message.text.lower():
        bot.send_message(message.chat.id, 'Пока нормально, а у тебя?')
    elif 'прив' in message.text.lower():
        bot.send_message(message.chat.id, 'Салям-Мулейкум!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICKl8IQpv9klIaMVa_lFx5ypewRP_2AAIWAgACygMGC0rAVbGSIu9QGgQ')
    elif 'животн' in message.text.lower():
        gif_animal = animal_random_gif()
        bot.send_message(message.chat.id, gif_animal)    
    elif 'кот' in message.text.lower():
        gif_cat = cat_random_gif()
        bot.send_message(message.chat.id, gif_cat)
    elif 'собак' in message.text.lower():
        gif_dog = dog_random_gif()
        bot.send_message(message.chat.id, gif_dog)
    elif 'мем' in message.text.lower():
        gif_meme = meme_random_gif()
        bot.send_message(message.chat.id, gif_meme)
        
    else:
        bot.send_message(message.chat.id, 'Я тебя не пойняв...')
        
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOIXwWwq171oZQo4cQ7e_uwBRJOl2UAAiADAAK6wJUFE7Y-lhgzxCcaBA')

@bot.message_handler(content_types=['video'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOIXwWwq171oZQo4cQ7e_uwBRJOl2UAAiADAAK6wJUFE7Y-lhgzxCcaBA')

print("Run...")
bot.polling(none_stop=True, interval=0)




