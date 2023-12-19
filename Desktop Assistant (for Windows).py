import os
import sys
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3

def welcome():
    time=int(dt.datetime.now().hour)
    if(time>=1 and time<12):
    	speak("Good Morning ")
    elif(time>=12 and time<16):
    	speak("Good Aternoon ")
    else:
    	speak("Good Evening ")
    speak("How Can I Help You !")

def speak(audio):
    print("AI :",audio)
    engine=pyttsx3.init()
    engine.setProperty('voice','en-in')
    speed=engine.getProperty('rate')
    engine.setProperty('rate',speed-60)
    engine.say(audio,name=None )
    engine.runAndWait()
    
def r_voice():
    r=sr.Recognizer()
    with sr.Microphone() as mp:
        print("Recognising....")
        r.pause_threshold=0.8
        audio=r.listen(mp) 
    try:
        query=r.recognize_google(audio,language='en-in')
        print("User Side :",query)
        return query
    except Exception as e:
        print(e)
        speak("Say Again Please..")

if __name__=="__main__":
    os.system('clear')
    welcome()
    while True:
        query=r_voice()
        if(query==None):
            continue
        query=query.lower()
        if('goodbye' in query):
            speak("Ok Good Bye Thakyou for Using Me..")
            break
        elif "open vs code" in query:
            os.system("code")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open chrome" in query:
            os.system("google-chrome")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open camera" in query:
            os.system("cheese")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "text editor" in query:
            os.system("gedit")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open folder" in query:
            os.system("open /nishanth-path")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open vlc" in query:
            os.system("vlc")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "search" in query:
            query=query.replace("search","")
            query=query.replace(" ","")
            webbrowser.open(f"google.com/search?q={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "youtube" in query:
            speak("opening youtube...")
            query=query.replace("youtube","")
            query=query.replace(" ","")
            webbrowser.open(f"youtube.com/results?search_query={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)

        elif "play" in query:
            speak("Starting...")
            query=query.replace("play","")
            yt.playonyt(query)
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open" in query:
            query=query.replace("open","")
            query=query.replace(" ","")
            speak(f"opening {query}...")
            webbrowser.open(f"{query}.com")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break
