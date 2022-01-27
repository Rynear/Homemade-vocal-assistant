# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyttsx3
import datetime
from yeelight import Bulb

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')[0]
engine.setProperty('voice', voices.id)
salonStrip = Bulb("192.168.1.48")
chambreBulb = Bulb("192.168.1.81")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:    
        with sr.Microphone() as source:
            print("J'écoute...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language="fr-FR")
            command = command.lower()
            print(command)
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        print('Pas de commande')
        pass
    return command

def try_command(command):
    try:
        talk("Je passe dans le try")
        command
    except:
        talk("Je passe dans le except.")
        pass

def run_alexa():
    talk("J'attends une commande")
    command = take_command()
    talk("J'ai une commande")
    if "la chambre" in command:
        try_command(chambreBulb.turn_off())
        talk("La chambre est éteintes")
    elif "allume la chambre" in command:
        try_command(chambreBulb.turn_on())
        talk("La chambre est allume")
    elif "eteins le salon" in command:
        try_command(salonStrip.turn_off())
        talk("Le salon est éteintes")
    elif "allume le salon" in command:
        try_command(salonStrip.turn_on())
        talk("Le salon est allumé")
    elif "quelle heure est-il" in command:
        try_command(time = datetime.datetime.now().strftime('%H:%M'))
        talk('Il est ' + time)
    else:
        talk("Je n'ai pas compris la demande")

while True:
    run_alexa()