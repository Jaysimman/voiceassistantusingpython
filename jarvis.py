from datetime import datetime
from re import S
from this import s
from turtle import left
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("kaalai vanakkam JAY")
    elif hour>=12 and hour<18:
        speak("Good afternoon JAY")
    else:
        speak("Good evening JAY")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    query=""
    try:
        print("Wait for few Moments")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
    except Exception as e:
        print(e)
        speak("say that again please")
    return query 
speak("Hey Jay , I'm your assistant Kaipulla, what Can I do For you?")
wishme()
if __name__ == "__main__":
    while True:
        query =takecommand().lower()
        if "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Jay.")
        elif "what is your name" in query:
            speak("Kaipulla")            
        elif "open youtube" in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")
        elif "Hi Jarvis, How are you" in query or "how are you":
            speak("I am good , How are you boss")
        elif "open google" in query:
            speak("opening Google")
            webbrowser.open("google.com")
        elif "play music" in query:
            musicdir="C:\\Users\\Jay\\Music"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[0]))
        elif "open edge" in query:
            codepath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application"
            os.startfile(codepath)
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        elif "love is" in query or "what do you think about love " in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I am your virtual assistant created by Jay")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif "the time is" in query or "what is the time now" in query:
            time=datetime.datetime.now().strftime("%H:%M")
            speak(time)
        elif "see you later" in query:
            speak("Bye Jay")
            exit()
        elif "tell me joke" in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)
            print(My_joke)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
        elif "play alone" in query:
            webbrowser.open("https://www.youtube.com/watch?v=bPs0xFd4skY")
        elif "close" in query:
            pyautogui.click(x=1898, y=0, button='left')