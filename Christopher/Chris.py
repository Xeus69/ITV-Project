import pyttsx3
import datetime
import os
import wikipedia
import webbrowser
import smtplib
import speech_recognition  as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#if __name__=="__main__":
 #   speak("I'm Batman")

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning, Sir")
    
    elif hour >=12 and hour < 18:
        speak("Good Afternoon, Sir")

    else:
        speak("Good Evening, Sir")

    speak("I am Christopher, How May I assist you?")

def command():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: " "{query}\n")
        return query

    except Exception as e:
        print("Could you please repeat that? ")
        return "None"
    



if __name__ == "__main__":
    greet()
    while True:
    # if 1:
        query = command().lower()


 