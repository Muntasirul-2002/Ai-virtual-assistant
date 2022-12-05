from asyncio import subprocess
from cgitb import text
from dataclasses import replace
from distutils.file_util import move_file
from distutils.log import info
from importlib.resources import path
from time import strftime
from turtle import stamp
#from lib2to3.pytree import _Results
from unittest import result
import webbrowser
from click import command, open_file
from jmespath import search
from numpy import void
from pip import main
import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import flask
import wikipedia
import os
import pyjokes
import wikipedia as googleScrap
import pprint
#from utils import opening_text
import subprocess as sp
import requests
import choice
import my_ip



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 166)

engine.setProperty('volume', 0.8)

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def whishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")    


def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")

        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)


    try:
        print("Recognizing...")
        speak("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)

        print("Say that again...")
        speak("Say that again...")
        return "None"
    return query

    
if __name__ == '__main__':
    whishMe()
    speak("initialising your galaxy")
    speak("I am Raisa tamanna , How may I help you?")

while True:
    query = takeCommand().lower()

    if 'play' in query:
        song = query.replace('play','')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif 'wikipedia' in query:
        query = query.replace('wikipdia', '')
        speak('searching Wikipedia...')
        result = wikipedia.summary(query,sentence=2)
        speak('Acrroding to wikipedia')
        print('result')
        speak('result')

        
    elif 'google' in query:
        google = query.replace('google', '')
        speak('opening' + google)
        webbrowser.open("google.com")

    elif 'search' in query:
        search ="https://www.google.com/search?q="+query
        webbrowser.open(search)

    elif 'youtube' in query:
        youtube = query.replace('youtube', '')
        speak('opening' + youtube)
        webbrowser.open("youtube.com")

    elif 'whatsapp' in query:
        whatsapp = query.replace('whatsapp', '')
        speak('opening whatsapp' + whatsapp)
        webbrowser.open("whatsapp.com")
    
    elif 'open code' in query:
        codePath = "E:\\Software\\Microsoft VS Code\\Code.exe"
        speak("opening...")
        os.startfile(codePath)
    
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    
    elif 'facebook' in query:
        facebook = query.replace('facebook', '')
        speak('opening..' + facebook)
        webbrowser.open("facebook.com")
    
    elif 'instagram' in query:
        instagram = query.replace('instagram', '')
        speak('opening..' + instagram)
        webbrowser.open("instagram.com")

    elif 'linkedIn' in query:
        linkedIn = query.replace('linkedIn','')
        speak('opening..'+linkedIn)
        webbrowser.open("linkedIn.com")

    elif 'github' in query:
        github = query.replace('github', '')
        speak('opening..' + github)
        webbrowser.open("github.com")

    elif 'i love you' in query:
        speak("i love you too")

    elif 'how are you' in query:
        speak("i am fine,what about you")
    
    elif 'are you single' in query:
        speak("No i am in a reletionship with muntasirul islam")

    elif 'whats the time' in query:
        speak("sorry,i cannot tell because i have a headache")

    elif 'are you virgin' in query:
        speak("sorry,i can't tell")

    elif 'What is the name of this laptop' in query:
        speak('This is DELL VOSTRO 3400.Intel core i3. specialy made for students')

    elif 'what is your name' in query:
        speak("My name is Muntasirul islam and i'm from galaxy.")

    
    
    elif 'thank you' in query:
        speak("you are most wellcome")

    elif 'codechef' in query:
        codechef = query.replace('codechef', '')
        speak('opening..' + codechef)
        webbrowser.open("codechef.com")
    
    elif 'Anydesk' in query:
        speak = 'opening...'
        path = "C:\Program Files (x86)\AnyDesk\Anydesk.exe"
        os.startfile([path])

    elif 'TurboC++' in query:
        codepath = "C:\\TURBOC3\\Turbo C++\\Turbo C++.exe"
        speak("opening..")
        os.startfile(codepath)   
    
    elif 'today weather' in query:
        search ="https://www.google.com/search?q="+query
        #speak('you can see direct in google')
        speak(result)
        webbrowser.open(search)

    elif 'open photoshop 7.0' in query:
        codepath="C:\\Program Files (x86)\\Adobe\\Photoshop 7.0.exe"
        speak("opening")
        os.startfile(codepath)

    elif 'open avro keyboard' in query:
        codepath= "C:\Program Files (x86)\Avro Keyboard.exe"
        speak("opening..")
        os.startfile(codepath)

    elif 'send whatsapp massage' in query:
        speak("On what number should I send the massage sir?")
        number= input("Enter the number:")
        speak("What is the massage sir?")
        massage=takeCommand().lower()
        send_whatsapp_massage=(number,massage)
        speak("I've sent the message sir.")

    elif 'send an email' in query:
        speak("On what number should I send the massage sir?")
        receiver_address= input("Enter email address:")
        speak("what should be the subject sie?")
        subject= takeCommand().capitalize()
        speak("what is the massage sir?")
        message= takeCommand().capitalize()
        
    
    
    
    

    

    
    
    
        




    

    
             
    
