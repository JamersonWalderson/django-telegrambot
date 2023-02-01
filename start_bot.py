import telebot

CHAVE_API = "6039607999:AAFEmx_ZnSduVfdmT1gdU3SWduUoX1_4m7A"

bot = telebot.TeleBot(CHAVE_API)



def init(message):
    return True

@bot.message_handler(func=init)
def start_message(message):
    welcome = """
        Óla, esté é um Bot desenvolvido apenas para estudo. por favor escolha uma opção para continuar:
        /1 Mandar um abraço.
        /2 Se eu fosse um personagem dos cavaleiros do zódiaco quem eu seria?
        /3 O que as estrelas tem para me dizer hoje?

        Respo
    """
    bot.send_message(chat_id=message.chat.id, text=welcome)

bot.polling()
