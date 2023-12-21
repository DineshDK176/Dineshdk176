import subprocess as sp
import os
import sys
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3
import pywhatkit as yt

def welcome():
    time=int(dt.datetime.now().hour)
    if(time>=1 and time<12):
    	speak("Good Morning ")
    elif(time>=12 and time<16):
    	speak("Good Aternoon ")
    else:
    	speak("Good Evening ")
    speak("How Can I Help You !")
    speak("Are You want to Intract with Keyboard.? (Y/N)")
    f_back=input().lower()
    if(f_back=='y'):
        return "y"
    elif(f_back=='n'):
        return "n"


def speak(audio):
    print("AI :",audio)
    if(len(audio)==45):
        audio=audio[0:37]
    engine=pyttsx3.init()
    engine.setProperty('voice','en-in')
    speed=engine.getProperty('rate')
    engine.setProperty('rate',speed-50)
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
    f=welcome()
    while(f=='n'):
        query=r_voice()
        if(query==None):
            continue
        query=query.lower().replace(" ","")
        
        if('goodbye' in query):
            speak("Ok Good Bye Thakyou for Using Me..")
            break
        
        elif ("text editor" in query or "notepad" in query):
            sp.run(["notepad.exe"])
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("open folder" in query):
            sp.run(["explorer.exe"])
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("search" in query):
            query=query.replace("search","")
            webbrowser.open(f"google.com/search?q={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("youtube" in query):
            speak("opening youtube...")
            query=query.replace("youtube","")
            webbrowser.open(f"youtube.com/results?search_query={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("wikipedia" in query):
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("play" in query):
            speak("Starting...")
            query=query.replace("play","")
            yt.playonyt(query)
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("open" in query):
            query=query.replace("open","")
            speak(f"opening {query}...")
            webbrowser.open(f"{query}.com")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break
            
        '''elif("open vs code" in query):
            os.system("code")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break
                
            elif ("open chrome" in query):
            sp.run(["chrome.exe"])
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break
        '''
        
    while(f=='y'):
        query=input("Waiting for Input...").lower().replace(" ","")
        if('goodbye' in query):
            speak("Ok Good Bye Thakyou for Using Me..")
            break
        
        elif ("text editor" in query or "notepad" in query):
            sp.run(["notepad.exe"])
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("open folder" in query):
            sp.run(["explorer.exe"])
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("search" in query):
            query=query.replace("search","")
            webbrowser.open(f"google.com/search?q={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("youtube" in query):
            speak("opening youtube...")
            query=query.replace("youtube","")
            webbrowser.open(f"youtube.com/results?search_query={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("wikipedia" in query):
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("play" in query):
            speak("Starting...")
            query=query.replace("play","")
            yt.playonyt(query)
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break

        elif ("open" in query):
            query=query.replace("open","")
            speak(f"opening {query}...")
            webbrowser.open(f"{query}.com")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break
            
        '''elif("open vs code" in query):
            os.system("code")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break
                
            elif ("open chrome" in query):
            sp.run(["chrome.exe"])
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                speak("Ok Good Bye Thakyou for Using Me..")
                break
        '''
