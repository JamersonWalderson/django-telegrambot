import telebot

CHAVE_API = "6039607999:AAFEmx_ZnSduVfdmT1gdU3SWduUoX1_4m7A"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["cardapio"])
def cardapio(message):
    text = ""
    bot.reply_to(message, text)

@bot.message_handler(commands=["reclamar"])
def reclamar(message):
    text = """Pedimos desculpa por qualquer incoveniente, peço que por gentilize envie sua sugestão para:\n
    jamersonwalderson@gmail.com"""
    bot.reply_to(message, text)

@bot.message_handler(commands=["abraco"])
def abraco(message):
    text =f"{message.from_user.first_name}, é um prazer té-lo como nosso cliente e amigo, sinta-se abraçado por toda nossa equipe :)"
    print(message)
    bot.reply_to(message, text)

@bot.message_handler(commands=["dev"])
def dev(message):
    text = """\
    Desenvolvido por Jamerson Walderson.\n
    Portifólio: https://jamersonwalderson.github.io
    Linkedin: https://www.linkedin.com/in/jamerson-walderson-803618171/
    Github: https://github.com/JamersonWalderson\
    """
    bot.reply_to(message, text)



def init(message):
    return True

@bot.message_handler(func=init)
def start_message(message):
    welcome = """
        Óla, esté é um Bot desenvolvido apenas para estudo. por favor escolha uma opção para continuar:
        /cardapio Ver cardapio.
        /reclamar Reclamar de um pedido.
        /abraco Mandar um abraço.
        /dev Informações sobre o desenvolvedor.

        Respo
    """
    bot.send_message(chat_id=message.chat.id, text=welcome)

bot.polling()
