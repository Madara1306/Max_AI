import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import time
import numpy as nps
import pyautogui as p
import random


GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

r = sr.Recognizer()
engine = pyttsx3.init()

name = 'Sir'

random_number = random.randint(1, 125)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
def wisMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning"+ name)
    elif hour>= 12 and hour<18:
        speak("Good Afternoon" + name)
    else:
        speak("Good Evening" + name)
    speak("I am Max, How can I help you?")

engine = pyttsx3.init('sapi5')
v = engine.getProperty('voices')
name = "master"
exit = ['exit']
engine.setProperty('voice', v[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def search_google(qu):
    url = f"https://www.google.com/search?q={qu}"
    webbrowser.open_new_tab(url)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        quray = r.recognize_google(audio, language = 'en-in')
        print (f"Command =  {quray}\n")
    except Exception as e:
        print(e)
        print(RED + "I can't understand can you say that again please." + RESET)
        speak("I can't understand, can you say that again please.")
        return "None"
    return quray




if __name__ == "__main__":
    wisMe()
    while True:
        quray = takeCommand().lower()
        if 'wikipedia' in quray:
            speak('Searching on wikipedia...')
            quray = quray.replace("wikipedia", "")
            results = wikipedia.summary(quray, sentences = 3)
            speak("Accoding to wikipedia")
            print(GREEN, results, RESET)
            speak(results)
        elif 'open youtube' in quray:
            webbrowser.open_new_tab("https://www.youtube.com")
        elif 'open instagram' in quray:
            webbrowser.open_new_tab("https://www.instagram.com")
        elif 'open google' in quray:
            webbrowser.open_new_tab("https://www.google.com")
        elif 'open zoro' in quray:
            webbrowser.open_new_tab("https://zoro.to/home?source=pwa")
        elif 'open chat gpt' in quray:
            webbrowser.open_new_tab("https://chat.openai.com/chat")
        elif 'open vs code' in quray:
            """ Please Change the file path"""
            vs_path = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)
        elif 'play music' in quray:
            """ Please Change the file path"""
            music_dir = "Music"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[random_number]))
        elif 'the time' in quray:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'close tab' in quray:
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'f4')
        elif 'open cmd' in quray or 'open command prompt' in quray:
            time.sleep(2)
            pyautogui.hotkey('win', 'r')
            time.sleep(1)
            pyautogui.press('c')
            pyautogui.press('m')
            pyautogui.press('d')
            pyautogui.hotkey('enter')
        elif 'close window' in quray:
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
        elif 'open brave' in quray:
            """ Please Change the file path"""
            brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(brave)
        elif 'play video' in quray:
            """ Please Change the file path"""
            video_path = "Videos"
            video = os.listdir(video_path)
            os.startfile(os.path.join(video_path, video[random_number]))
            os.startfile(video_path)
        elif 'exit' in quray:
            break