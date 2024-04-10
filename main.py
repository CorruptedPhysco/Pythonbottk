import telebot

API_KEY = '7056447336:AAHp5_udS5vYiDLxp9kg346_4yE8gLgJZEU'
bot = telebot.TeleBot(API_KEY)
def code():
    with open('test.txt', 'r') as     file:
        cobe = file.read()
    return cobe
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """Welcome to the Telegram Bot
 Type /code to get the code""")

@bot.message_handler(commands=['code'])
def send_code_block(message):
  coddde = code()
  code_block = "```GFG\n" + coddde + "\n```"
  bot.send_message(message.chat.id, code_block, parse_mode='Markdown')
  print(" Code send")

def updatte():
    with open('test.txt', 'w') as file:
      file.write(word)
    print(" File updated")
def remove_dxd(text):
    return text.replace('/dxd ', '')

@bot.message_handler(commands=['dxd'])
def update_code(message):
    global word
    word = remove_dxd(message.text)
    updatte()
    bot.reply_to(message, "Code updated successfully!")

print(" Bot started")

bot.polling()
