import os,webbrowser,pyttsx3,mediawiki
import pywhatkit as yt
import datetime as dt
import speech_recognition as sr

def welcome():
    time=int(dt.datetime.now().hour)
    if time>=1 and time<12:
        wish="Good Morning"
    elif time>=1 and time<12:
        wish="Good Afternoon"
    else:
        wish="Good Evening"
    speak(wish)
    speak("I am Michella")
    speak("Are you want to intract with Keyword ")
    f_back=input("(Y/N)").lower()
    return f_back
    

def speak(wish):
    engine=pyttsx3.init()
    engine.setProperty('voice','en-in')
    speed=engine.getProperty('rate')
    engine.setProperty('rate',speed-65)
    print("AI :",wish)
    engine.say(wish,name=None )
    engine.runAndWait()
    
def r_voice():
    r=sr.Recognizer()
    with sr.Microphone() as mp:
        print("Recognising....")
        r.pause_threshold=0.8
        audio=r.listen(mp)
    try:
        print("Wait...")
        query=r.recognize_google(audio,language='en-in')
        print("User Side :",query)
        return query
    except Exception as e:
        print(e)
        speak("Say Again Please..")

def pros(query):
    con=''
    mk=mediawiki.MediaWiki()
    
    query=query.replace(' ','')
    if 'goodbye' in query  or 'bye' in query:
        con='n'          
    elif "chrome" in query:
        speak("Opening Chrome...")
        os.startfile("chrome.exe")
        con = input("Are you continue (Y/N):").lower()

    elif "texteditor" in query or "notepad" in query:
        speak("Opening...")
        os.startfile("Notepad.exe")
        con = input("Are you continue (Y/N):").lower()
    elif "wordpad" in query:
        speak("Openning...")
        os.startfile("wordpad.exe")
        con = input("Are you continue (Y/N):").lower()
            
    elif "folder" in query or "explorer" in query or "file" in query:
        speak("Opening...")
        os.startfile("explorer.exe")
        con = input("Are you continue (Y/N):").lower()
            
    elif "vlc" in query or "videoplayer" in query:
        speak("Opening...")
        os.startfile("vlc.exe")
        con = input("Are you continue (Y/N):").lower()
            
    elif "windowsmediaplayer" in query or 'mediaplayer' in query:
        speak("Openning...")
        os.startfile("wmplayer.exe")
        con = input("Are you continue (Y/N):").lower()

    elif "search" in query:
        speak("Searching....")
        query=query.replace("search","")
        query=query.replace(" ","")
        webbrowser.open(f"google.com/search?q={query}")
        con = input("Are you continue (Y/N):").lower()

    elif "youtube" in query:
        speak("Opening Youtube...")
        query=query.replace("youtube","")
        query=query.replace(" ","")
        webbrowser.open(f"youtube.com/results?search_query={query}")
        con = input("Are you continue (Y/N):").lower()

    elif "wikipedia" in query:
        speak("searching in wikipedia")
        query=query.replace("wikipedia","")
        try:
            result=mk.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(result)
            speak("Do You want to Save this Content..")
            save=input("(Y/N)").lower()
            if save=='y':
                speak("Where You want to Save this content.")
                path=input("Enter Full Path : ")
                file=open(path,'w')
                file.write("Wikipedia Result:\n")
                file.write(result)
                file.close()
                speak("The above Content is Saved Sucessfully.. ")
        except mediawiki.DisambiguationError as e:
            speak("Sorry the Information you looking is couldn't find...!")
    elif "play" in query:
        speak("Starting...")
        query=query.replace("play","")
        yt.playonyt(query)
        con = input("Are you continue (Y/N):").lower()
                
    else:
        speak("Sorry I can't Understand what you Trying to Say!!")

            
    if(con == 'n'):
        speak("Ok GoodBye Thank you for Interacting with Me..")

    return con

if __name__=="__main__":
    f=welcome()
    speak("How can I help you")
    while True:
        if f=='y':
            query=input("Waiting for Input... ").lower()
            r=pros(query)
            if r=='n':
                break
        else:
            query=r_voice().lower()
            if(query==None):
                continue
            r=pros(query)
            if r=='n':
                break
