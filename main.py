#!/usr/bin/env python
# -*- coding: utf-8 -*-
# abdeljalil-salhi
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
from pyttsx3 import init
from pywhatkit import playonyt
from datetime import datetime
from os import system

listener = Recognizer()
engine = init()
voices = engine.getProperty("voices")

# Manage the voice properties
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    system("clear || cls")
    try:
        with Microphone() as source:
            print("[+] Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except UnknownValueError:
        command = ""
        pass
    except RequestError as e:
        command = ""
        pass
    except:
        command = ""
        pass
    return command


def run_myalexa():
    command = take_command()

    if "play" in command:
        if "youtube" in command:
            song = command.replace("play ", "")
            talk("Playing " + song)
            playonyt(song)
        else:
            input("[!] Play MP3")

    elif "time" in command:
        talk(
            "Hey Abdel, Current time is {0}".format(
                datetime.now().strftime("%I:%M %p")
            )
        )

    elif "weather" in command:
        input("[!] Weather")

    elif command != "":
        pass


while True:
    run_myalexa()
