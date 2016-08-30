# -*- coding: utf-8 -*-
# import modules and functions
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx
# create functiions
def maichat(input):
    # start voice engine
    global response
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', "spanish")
    # init the bot and give a name
    chatbot = ChatBot("MAI")
    # training the bot
    chatbot.set_trainer(ListTrainer)
    chatbot.train("chatterbot.corpus.spanish")
    # preventive intro for limitation non supported utf-8 encoding
    message = """Hola, soy el chatbot interno de MAI, si vas ha charlar conmigo
    por favor no uses acentos o tildes pues la tecnologia en la que estoy basada
    aunque busca patrones de aprendizaje esta basada en el ingles y carece de un
    soporte alfabetico sin acentos ni signos mas alla del ingles. Soporto mayusculas
    ,minusculas, coma y punto. Por todo lo demas en un principio no sabre 
    nada y aprendere como un bebe. Para salir del chat, cierra la ventana."""
    print message
    # get a response and puth together in While
    while True:
        charla = input
        # change phrase of get_responser for input
        response = chatbot.get_response(charla)
        # ready only mode and be disable by comentarized
        # because I need a continued learning
        # chatbot = ChatBot("MAI", read_only=True)
        print response
    return response
    engine.say(response)
    engine.runAndWait()
