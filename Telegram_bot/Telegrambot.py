import os 
from dotenv import load_dotenv
import telebot
#Bot_username = Alpha42_bot
load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
def main():
    def a2(message):
        bot.reply_to(message, "Umut")
    @bot.message_handler(commands=["Merhaba","merhaba","selam","Selam"])
    def merhaba(message):
        bot.reply_to(message, "selam")
    
    bot.polling()

if __name__ == "__main__":
    main()