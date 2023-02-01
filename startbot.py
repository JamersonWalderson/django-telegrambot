import telebot

CHAVE_API = "6039607999:AAFEmx_ZnSduVfdmT1gdU3SWduUoX1_4m7A"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["cardapio"])
def cardapio(message):
    text = """O que você quer?\n
    /pizza Pizza
    /burguer Hamburguer
    /salada Salada
    """
    bot.reply_to(message, text)


@bot.message_handler(commands=["pizza"])
def pizza(message):
    bot.reply_to(message, "Saindo a pizza! O tempo de espera é de 20 minutos.")
    bot.send_message(message.chat.id, "Agradecemos seu pedido ver novamente.")
    bot.send_message(message.chat.id, "Caso queria voltar ao menu digite /menu")


@bot.message_handler(commands=["burguer"])
def burguer(message):
    bot.reply_to(message, "Saindo o Hamburguer! O tempo de espera é de 20 minutos.")
    bot.send_message(message.chat.id, "Agradecemos seu pedido ver novamente.")
    bot.send_message(message.chat.id, "Caso queria voltar ao menu digite /menu")


@bot.message_handler(commands=["salada"])
def salada(message):
    bot.reply_to(message, "Saindo a salada! O tempo de espera é de 20 minutos.")
    bot.send_message(message.chat.id, "Agradecemos seu pedido ver novamente.")
    bot.send_message(message.chat.id, "Caso queria voltar ao menu digite /menu")


@bot.message_handler(commands=["reclamar"])
def reclamar(message):
    text = """Pedimos desculpa por qualquer incoveniente, peço que por gentilize envie sua sugestão para:\n
    jamersonwalderson@gmail.com"""
    bot.reply_to(message, text)


@bot.message_handler(commands=["abraco"])
def abraco(message):
    text = f"{message.from_user.first_name}, é um prazer té-lo como nosso cliente e amigo, sinta-se abraçado por toda nossa equipe :)"
    print(message)
    bot.reply_to(message, text)


@bot.message_handler(commands=["dev"])
def dev(message):
    text = """\
    Desenvolvido por Jamerson Walderson.\n
    https://jamersonwalderson.github.io
    """
    bot.reply_to(message, text)


def init(message):
    return True


@bot.message_handler(func=init)
def start_message(message):
    welcome = """
    Óla, para iniciar seu atendimento escolha uma opção:
    /reclamar Reclamar de um pedido.
    /abraco Mandar um abraço.
    /dev Informações sobre o desenvolvedor.
    """
    bot.send_message(chat_id=message.chat.id, text=welcome)


bot.polling()
