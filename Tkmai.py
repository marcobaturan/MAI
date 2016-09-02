# -*- coding: utf-8 -*-
# TODO: everything                                                         
# Author: Marco Garcia Baturan                                             
# Date: 27-08-16                                                           
# Description: General Artificial Intelligence oriented to interaction like
# Virtual Computer Assistant who expand own capabilities using exclusive   
# Python programming language and pythonic tools or methots or ways and any
# AI technic online or offline.                                            
# Licence: GPL                                                             
# Project hosted in: https://github.com/Marcogb81/MAI                      
# Documentation hosted in: https://readthedocs.org                         
# _________________________________________________________________________
# import modules
from Tkinter import *
import pyttsx
import wikipedia
import wolframalpha
# variables
# id of wolframalpha for API module
app_id= "AL9P98-8Q6P8GY8PX"
client = wolframalpha.Client(app_id)
# variable and start tts
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice',"english")
# main function of chatbot
def OnEnter( event):
        # enter the data
        input = I1.get()
        input = input.lower()
        try:
            # wolframalpha's block
            resolve = client.query(input) # give question
            answer = next(resolve.results).text # add info to variable
            #print answer # give answer
            resolve.configure(text = str(Label.get(answer)))
            #espeak.synth("La respuesta es "+str(answer))
            engine.say("The solution is: " + answer)
            engine.runAndWait()
        except:
            try:
                # wikipedia block
                wikipedia.set_lang("en") # select language of wiki it is esperanto
                input = input.split(' ')
                input = ' '.join(input[2:])
                print wikipedia.summary(input, sentences=3) # give answer untill 3 sentences
                engine.say(wikipedia.summary(input, sentences=3))
                engine.runAndWait()
            except:
                duda = "I do not know what to do, write manual to read the manual."
                print duda
                engine.say("I do not know what to do, write manual to read the manual.")
                try:
                    if 'manual' in input:
                        with open('help.txt', 'r') as fin:
                            print fin.read()
                except:
                    pass
# variable and function
window = Tk() # call window from tk
Label(window, text="Wellcome to MAI").grid(row=0,column=0)
Label(window, text="Enter text and press Return").grid(row=1,column=0)
# input textbox
I1= Entry(window) # txt intro to answer
I1.grid(row=2) # position
I1.bind("<Enter>", OnEnter) # input data in textbox to function
# output of result
Label(window, text = "I say: ").grid(row = 3)
resolution = Label(window)  # Label for response
# main block
window.mainloop()