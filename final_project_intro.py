import telebot
from telebot import types

token = '1094865183:AAGH3s7ND6P0iH6oIWDsu4I9-QgW3SeChf4'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello ,'
                                      'I will help you find lessons in ocs')
    markup = types.InlineKeyboardMarkup(row_width=1)
    eng = types.InlineKeyboardButton("Englsih", callback_data="as1")
    eco = types.InlineKeyboardButton("Ecology", callback_data="as2")
    pyt = types.InlineKeyboardButton("Python", callback_data="as3")
    inn = types.InlineKeyboardButton("intro2eng", callback_data="as4")
    phy = types.InlineKeyboardButton("Physics", callback_data="as5")
    cal = types.InlineKeyboardButton("Calculus", callback_data="as6")
    rus = types.InlineKeyboardButton("Russian", callback_data="as7")
    tur = types.InlineKeyboardButton("Turkish", callback_data="as8")
    pca = types.InlineKeyboardButton("Physical Culture", callback_data="as9")
    markup.add(eng, eco, pyt, inn, phy, cal, rus, tur, pca)
    bot.send_message(message.chat.id, 'What do you need?',
                     reply_markup=markup)


@bot.message_handler(commands=['settings'])
def start_message(message):
    bot.send_message(message.chat.id, 'There is no problem here\n'
                                      'Click on /help')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'If you want to start the program,\n'
                                      'press the /start command!\n\n'
                                      'If you need help with python,\n'
                                      'press to /python_language command!\n\n'
                                      'If you need help with HTML,\n'
                                      'press to /html_language command!\n\n'
                                      'If you want to create '
                                      'a telegram bot like me,\n'
                                      'press to /create_a_bot command!')


@bot.message_handler(commands=['entertainment'])
def start_message(message):
    markup1 = types.InlineKeyboardMarkup(row_width=1)

    foot = types.InlineKeyboardButton("Football", callback_data="sa1")
    new = types.InlineKeyboardButton("News", callback_data="sa2")
    nat = types.InlineKeyboardButton("nat_geo_wild", callback_data="sa3")
    film = types.InlineKeyboardButton("Films", callback_data="sa4")
    gam = types.InlineKeyboardButton("Gamers", callback_data="sa5")
    markup1.add(foot, new, nat, film, gam)
    bot.send_message(message.chat.id, 'WHAT DO YOU PREFER?',
                     reply_markup=markup1)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'as1':
            bot.send_message(call.message.chat.id, 'English:\n'
                                              'https://classroom.'
                                              'google.com/c/MTU5MjczNzc1MDk1')
            bot.send_message(call.message.chat.id, 'Teacher: Sagyn Basnyat')
            bot.send_message(call.message.chat.id, 'Gmail: sagun.basnyat@alatoo.edu.kg')


        if call.data == 'as2':
            bot.send_message(call.message.chat.id, 'Ecology:\n'
                                              'https://classroom.'
                                              'google.com/c/MTUzNjg2NTcxMTM5')
            bot.send_message(call.message.chat.id, 'Teacher: Turdukan Bekimbetova')
            bot.send_message(call.message.chat.id, 'Gmail: '
                                              'turdukan.bekimbetova@iaau.edu.kg')

        if call.data == 'as3':
            bot.send_message(call.message.chat.id, 'Python:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=28')
            bot.send_message(call.message.chat.id, 'Teachers: '
                                      'Ruslan Isaev and Gulzada Esenalieva')
            bot.send_message(call.message.chat.id, 'Gmail: ruslan.isaev@alatoo.edu.kg')
            bot.send_message(call.message.chat.id, 'Gmail: ruslan.isaev@iaau.edu.kg')
            bot.send_message(call.message.chat.id, 'Gmail: gulzada.'
                                      'esenalieva@alatoo.edu.kg')


        if call.data == "as4":
            bot.send_message(call.message.chat.id, 'Intro2eng:\n'
                                              'https://ocs.iaau.edu.kg/'
                                              'course/view.php?id=2')
            bot.send_message(call.message.chat.id, 'Teacher: Burul Shambetova')
            bot.send_message(call.message.chat.id, 'Gmail: '
                                              'burul.shambetova@alatoo.edu.kg')


        if call.data == "as5":
            bot.send_message(call.message.chat.id, 'Physics:\n'
                                              'https://ocs.iaau.edu.kg/'
                                              'course/view.php?id=135')
            bot.send_message(call.message.chat.id, 'Teacher: Tahir Aslan')
            bot.send_message(call.message.chat.id, 'Gmail: '
                                              't.aslan@alatoo.edu.kg')

        if call.data == "as6":
            bot.send_message(call.message.chat.id, 'Calculus:\n'
                                              'https://ocs.iaau.edu.kg/'
                                              'course/view.php?id=193')
            bot.send_message(call.message.chat.id, 'Teacher: Khalid Mohammad')
            bot.send_message(call.message.chat.id, 'Gmail: '
                                              'khalid.mohammad@alatoo.edu.kg')

        if call.data == "as7":
            bot.send_message(call.message.chat.id, 'Russian:\n'
                                              'https://ocs.iaau.edu.kg/'
                                              'course/view.php?id=409')
            bot.send_message(call.message.chat.id, 'Teacher: Surakan Muzurbekovna')
            bot.send_message(call.message.chat.id, 'Gmail: '
                                              'surakan.alymbekova@iaau.edu.kg')

        if call.data == "as8":
            bot.send_message(call.message.chat.id, 'Turkish:\n'
                                              'https://ocs.iaau.edu.kg/'
                                              'course/view.php?id=1550')
            bot.send_message(call.message.chat.id, 'Teacher: Mr Mehmet')
            bot.send_message(call.message.chat.id, 'Gmail: ')
        if call.data == "as9":
            bot.send_message(call.message.chat.id, 'Physicalculture:\n'
                                              'https: //ocs.iaau.edu.kg/'
                                              'course/view.php?id=1217')
            bot.send_message(call.message.chat.id, 'Teacher: '
                                              'Irina Chalova')
            bot.send_message(call.message.chat.id, 'Gmail: '
                                              'irina.chalova@iaau.edu.kg')
        if call.data == "sa1":
            bot.send_message(call.message.chat.id, 'Football:'
                                              'https://www.'
                                              'youtube.com/c/TARAFTARKANALIHD/videos')
            bot.send_message(call.message.chat.id, 'https://www.youtube.com/channel/'
                                              'UCO8qj5u80Ga7N_tP3BZWWhQ/videos')
            bot.send_message(call.message.chat.id, 'https://www.'
                                              'youtube.com/c/AllFootball28/videos')
            bot.send_message(call.message.chat.id, 'https://www.'
                                              'youtube.com/c/Score90/videos')
        if call.data == "sa2":
            bot.send_message(call.message.chat.id, 'News: '
                                              'https://www.'
                                              'youtube.com/c/NBCNews/videos')
            bot.send_message(call.message.chat.id, 'https://www.youtube.com/c/'
                                              'BBCNews/videos')
            bot.send_message(call.message.chat.id, 'https://www.'
                                              'youtube.com/c/globalnews/videos')
            bot.send_message(call.message.chat.id, 'https://www.'
                                              'youtube.com/c/ddnews/videos')
        if call.data == "sa3":
            bot.send_message(call.message.chat.id, 'Nat Geo Wild: '
                                              'https://www.youtube.com/channel'
                                              '/UChqjsr9DovXmAUtS_q_2V0w/videos')
        if call.data == "sa4":
            bot.send_message(call.message.chat.id, 'Films'
                                              ':https://www.'
                                              'youtube.com/c/FilmsterRu/videos')
            bot.send_message(call.message.chat.id, 'https://www.youtube.'
                                              'com/c/RVisionChannel/videos')
            bot.send_message(call.message.chat.id, 'https://www.youtube.com/channel/'
                                              'UCK3AJaBVixx5BvCPLI2Ho9g/videos')
        if call.data == "sa5":
            bot.send_message(call.message.chat.id, '1) Marmok:\n\n'
                                              'https://www.'
                                              'youtube.com/c/MrMarmok/videos')
            bot.send_message(call.message.chat.id, '2) Joe speen:\n\n'
                                              'https://www.'
                                              'youtube.com/c/JoeSpeen/videos')
            bot.send_message(call.message.chat.id, '3) Quantum:\n\n'
                                              'https://www.'
                                              'youtube.com/c/QuantumGames/videos')
            bot.send_message(call.message.chat.id, '4) Buster:\n\n'
                                              'https://www.youtube.'
                                              'com/c/%D0%91%D1%83%D1%81%'
                                              'D1%82%D0%B5%D1%80/videos')



@bot.message_handler(commands=['python_language'])
def start_message(message):
    bot.send_message(message.chat.id, 'Here you can learn to'
                                      ' python for free.')
    bot.send_message(message.chat.id, 'https://www.'
                                      'w3schools.com/python/')


@bot.message_handler(commands=['html_language'])
def start_message(message):
    bot.send_message(message.chat.id, 'Here you can learn to'
                                      ' html for free.')
    bot.send_message(message.chat.id, 'https://www.'
                                      'w3schools.com/html/default.asp')


@bot.message_handler(commands=['create_a_bot'])
def start_message(message):
    bot.send_message(message.chat.id, 'Here you can create a new bot.')
    bot.send_message(message.chat.id, 'https://t.me/BotFather')


def echo_all(message):
    bot.reply_to(message, 'I do not have such kind of command')
    bot.send_message(message.chat.id, 'If you get bored click on'
                                      ' /entertainment')
    bot.send_message(message.chat.id, 'if you need help click on /help')


bot.polling()