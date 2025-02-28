import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey =""
bot_id = "5753496927:AAGGcmvPW2UXzsYspSMPhKtnAc_j6TOx7HU"

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    movie = message.text
    movie = movie.replace("/movie","")
    response = requests.get( f"http://www.omdbapi.com/?apikey=bcd3f769&t={movie}")
    movie_data=response.json()
    print(json.dumps(movie_data,indent = 4))
    bot.reply_to(message,f"{movie_data['Poster']} \nMovie Name: {movie_data['Title']} \nYear: {movie_data['Year']} \nReleased: {movie_data['Released']} \nImdb Rating: {movie_data['imdbRating']}")
    bot.send_photo(message,{movie_data['Poster']})
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    with open('movie_data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([movie_data['Title'],movie_data['Year'],movie_data['Released'],movie_data['imdbRating']])


  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    chat_id = message.chat.id 
    print()
    movie_data=open('movie_data.csv','rb')
    bot.send_document(chat_id,movie_data)
    
    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
