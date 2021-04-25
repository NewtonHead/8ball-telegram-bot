import telebot
import random
bot = telebot.TeleBot("TOKEN" , parse_mode=None) #Insert your bot token here

@bot.message_handler(commands=['start', 'help']) #Available commands
def handle_start_help(message):
    if message.chat.type == "private":
        bot.reply_to(message, 'Hey! i can tell you fortune if you @ me')

@bot.message_handler(regexp='@BotName') #Insert your bot @name
def handle_fortuna_command(message):
    answer = random.randint(1, 19) #Gets the random answer
    if answer == 1:
        bot.reply_to(message, 'It is certain.')
    elif answer == 2:
        bot.reply_to(message, 'It is decidedly so.')
    elif answer == 3:
        bot.reply_to(message, 'Without a doubt.')
    elif answer == 4:
        bot.reply_to(message, 'Definitely.')
    elif answer == 5:
        bot.reply_to(message, 'You may rely on it.')
    elif answer == 6:
        bot.reply_to(message, 'As i see it, yes.')
    elif answer == 7:
        bot.reply_to(message, 'Most likely.')
    elif answer == 7:
        bot.reply_to(message, 'Yes.')
    elif answer == 8:
        bot.reply_to(message, 'Outlook good.')
    elif answer == 9:
        bot.reply_to(message, 'Signs point to yes.')
    elif answer == 10:
        bot.reply_to(message, 'Reply hazy, try again.')
    elif answer == 11:
        bot.reply_to(message, 'Ask again later.')
    elif answer == 12:
        bot.reply_to(message, 'Better not tell you now.')
    elif answer == 13:
        bot.reply_to(message, 'Cannot predict now.')
    elif answer == 14:
        bot.reply_to(message, 'Concentrate and ask again.')
    elif answer == 15:
        bot.reply_to(message, 'Dont count on it')
    elif answer == 16:
        bot.reply_to(message, 'My reply is no.')
    elif answer == 17:
        bot.reply_to(message, 'My sources say no.')
    elif answer == 18:
        bot.reply_to(message, 'Very doubtful.')
    elif answer == 19:
        bot.reply_to(message, 'Outlook no so good.')

bot.polling()
