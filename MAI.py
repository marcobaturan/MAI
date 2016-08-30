# -*- coding: utf-8 -*-
# wolframalpha code api: AL9P98-HHVWK6QGQ2
"""
Author: Marco Garcia Baturan
Date: 28-8-16
License: opensource
Description: MAI means Marco's Artificial Intelligence, in begining works like
virtual assistant of personal computer and it is based in Chat, API's, TTS.
In the future I will add voice recognition, handwriting, Computer Vision and 
database based in SQLite. This module is based i Udemy's course of 
https://github.com/KhanradCoder/PyDa-Course-Code
"""
# import modules
import pyttsx
import wikipedia
import wolframalpha
import wx
from datetime import datetime
# app di wolramalpha
app_id= "AL9P98-HHVWK6QGQ2"
client = wolframalpha.Client(app_id)
# start voice engine
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice',"spanish")
#  main class
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="MAI")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hola, soy MAI, asistente virtual en Python para Linux.")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self, event):
        # enter the data
        input = self.txt.GetValue()
        input = input.lower()
        # poner aquí los otros modulos
        try:
            # agregar modulo de chatbot
            from maichat import maichat
            maichat(input)
            try:
                # agregar modulo rae
                from diccionario import diccionario
                diccionario(input)
            except:
                try:
                    # give manual
                    if 'manual' in input:
                        with open('help.txt', 'r') as fin:
                            print fin.read()
                except:
                    pass
        except:
            try:
                # wolframalpha's block
                resolve = client.query(input) # give question
                answer = next(resolve.results).text # add info to variable
                print answer # give answer
                #espeak.synth("La respuesta es "+str(answer))
                engine.say("La respuesta es" + answer)
                engine.runAndWait()
            except:
                try:
                    # wikipedia block
                    wikipedia.set_lang("es") # select language of wiki it is esperanto
                    input = input.split(' ')
                    input = ' '.join(input[2:])
                    print wikipedia.summary(input, sentences=3) # give answer untill 3 sentences
                    engine.say(wikipedia.summary(input, sentences=3))
                    engine.runAndWait()
                except:
                    duda = "No se que hacer"
                    print duda
                    engine.say("No se que hacer")
                    engine.runAndWait()

if __name__ == "__main__":
    # automatic greetings based in hour day
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
