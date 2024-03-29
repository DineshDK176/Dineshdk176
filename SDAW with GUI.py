import os,webbrowser,pyttsx3,mediawiki,subprocess,urllib.error,time
import wolframalpha as wa
import threading as td
import datetime as dt
import speech_recognition as sr
from tkinter import *
from PIL import Image, ImageTk
from itertools import count

class GifLabel(Label):

    text = ''
    con = ''
    f_back,entry = 0,0
    
    
    def __init__(self, master=None,**kwargs):
        super().__init__(master, **kwargs)
        self.frames = []
        self.loc = 0
        self.delay = 100
        
        
    def image_load(self, gif_pic):
        if isinstance(gif_pic, str):
            gif_pic = Image.open(gif_pic)
            self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(gif_pic.copy()))
                gif_pic.seek(i)

        except EOFError:
             pass

        try:
            self.delay = gif_pic.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(width=1300,bg='black',image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

    engine = pyttsx3.init()
    engine.setProperty('voice', 'en-in')
    engine.setProperty('rate', engine.getProperty('rate') - 40)
    mic = sr.Recognizer()
    
    def speak(self, query,con=None):
        label = Label(root,bg='black')
        txt = ''
        for i in query:
            try:
                txt += i + ' .\n'
            except TypeError:
                pass
        label.config(text=f"AI: {txt}",fg="white")
        label.pack()
        self.engine.say(txt)
        self.engine.runAndWait()
        label.destroy()
        if self.f_back == 0:
            self.r_voice()
            self.f_back=0
        if con == 1:
            root.destroy()
            exit()

    def Thread_speak(self,*text,res=None,con=None):
        text = list(text)
        if res != None:
            c = 0
            for i in res:
                text[0] += (i+' ')
                c += 1
                if c == 35:
                    text[0] += '\n'
        speech = td.Thread(target = self.speak,args = (text,con))
        speech.start()

    def r_voice(self):
        self.f_back=2
        mic = sr.Recognizer()
        with sr.Microphone() as source:
            self.Thread_speak("Recognizing...")
            mic.pause_threshold = 0.8
            audio = mic.listen(source)
        try:
            self.Thread_speak("Wait...")
            query = self.mic.recognize_google(audio, language='en-in')
            self.Thread_speak(f"User Side: {query}\n")
            return query
        except Exception as e:
            self.Thread_speak("Say again, please...")
            return ""

    def Run(self,*action,txt_fld=None):
        self.Thread_speak(f'Openning {action[0]}...')
        os.startfile(f'{action[1]}')
        txt_fld.delete('1.0','end')
        self.entry = 1

    def pros(self, query,txt_fld=None):
        query = query.replace(' ','')

        if ('goodbye' in query)  or ('bye' in query):
            txt_fld.delete('1.0','end')
            self.Thread_speak("Ok GoodBye Thank you for Interacting with Me..",con=1)

        elif ('commandprompt' in query) or ('cmd' in query):
            self.Run('commandprompt','cmd',txt_fld=txt_fld)

        elif ('paint' in query):
            self.Run('paint','mspaint.exe',txt_fld=txt_fld)

        elif ('setting' in query) or ('controlpanel' in query):
            self.Run('setting','control.exe',txt_fld=txt_fld)

        elif ('calculator' in query):
            self.Run('calculator','calc.exe',txt_fld=txt_fld)

        elif ("texteditor" in query) or ("notepad" in query):
            self.Run('notepad','Notepad.exe',txt_fld=txt_fld)

        elif ("wordpad" in query):
            self.Run('wordpad','wordpad.exe',txt_fld=txt_fld)

        elif ("folder" in query) or ("explorer" in query) or ("file" in query):
            self.Run('folder','explorer.exe',txt_fld=txt_fld)

        elif ("vlc" in query) or ("videoplayer" in query):
            self.Run('videoplayer','vlc.exe',txt_fld=txt_fld)

        elif ("windowsmediaplayer" in query) or ('mediaplayer' in query):
            self.Run('media player','wmplayer.exe',txt_fld=txt_fld)

        elif ("chrome" in query) or ("browser" in query):
            self.Run(' ','chrome.exe',txt_fld=txt_fld)

        elif ("firefox" in query):
            self.Run('firefox','firefox.exe',txt_fld=txt_fld)

        elif ("search" in query):
            self.Thread_speak("Searching....")
            query = query.replace("search","")
            query = query.replace(" ","")
            webbrowser.open(f"google.com/search?q={query}")
            txt_fld.delete('1.0','end')
            self.entry = 1

        elif ("youtube" in query):
            self.Thread_speak("Opening Youtube...")
            query = query.replace("youtube","")
            query = query.replace(" ","")
            webbrowser.open(f"youtube.com/results?search_query={query}")
            txt_fld.delete('1.0','end')
            self.entry = 1

        elif ("wikipedia" in query):
            mk = mediawiki.MediaWiki()
            query = query.replace("wikipedia","")
            txt_fld.delete('1.0','end')
            try:
                self.Thread_speak("searching in wikipedia","According to wikipedia",'',res=mk.summary(query,sentences=3).split(' ','.',','))
                
            except mediawiki.DisambiguationError as e:

                self.Thread_speak("Sorry the Information you looking is couldn't find...!")
            self.entry = 1

        elif ("play" in query):
            self.Thread_speak("Starting...")
            query = query.replace("play","")
            yt.playonyt(query)
            txt_fld.delete('1.0','end')
            self.entry = 1

        elif ("shutdown" in query) or ("switchoff" in query) or ("poweroff" in query):
            subprocess.run(["shutdown","-s"])
            txt_fld.delete('1.0','end')
            self.Thread_speak("Ok GoodBye Thank you for Interacting with Me..",con=1)

        else:
            try:
                clt = wa.Client('GPGV2J-KG8TVJT6YT')
                res = clt.query(self.text)
                txt_fld.delete('1.0','end')
                ans=''
                for i in res.results:
                    ans+=i.text
                if ans == '':
                    self.Thread_speak(text='I cannot Understand what are you trying to Say..')
                else :
                    self.Thread_speak('',res = ans)
                self.entry=1
            except urllib.error.URLError as e:
                txt_fld.delete('1.0','end')
                self.Thread_speak("Please Check Your Internet and Try again")

    def get_txt(self,txt_fld=None):
        self.text = txt_fld.get('1.0','end').lower()
        if self.f_back == 1:
            self.pros(self.text,txt_fld=txt_fld)

        else :
            self.text = self.r_voice().lower()
            self.pros(self.text)

    def welcome(self):
        time = int(dt.datetime.now().hour)
        if time >= 1 and time < 12:
            wish = "Good Morning"
        elif time >= 12 and time < 16:
            wish = "Good Afternoon"
        else:
            wish = "Good Evening"
        self.Thread_speak(wish,"I am Michella","How can I help you")

    def key(self,keyboard=None,Mic=None,txt_fld=None,submit=None):
        keyboard.destroy()
        Mic.destroy()
        self.f_back = 1
        self.welcome()
        txt_fld.pack()
        submit.pack()

    def mic(self,keyboard=None,Mic=None):
        keyboard.destroy()
        Mic.destroy()
        self.f_back = 0
        self.welcome()
        
    def des_btn(self,btn=None,keyboard=None,Mic=None):
        btn.destroy()
        keyboard.pack()
        Mic.pack()

    def window(self,master=None):

        btn = Button(master,text='Start',width=10)

        txt_fld = Text(master,width=50,height=1,bg='white',fg='black')

        submit = Button(master,text='Submit',width=10,command=lambda :self.get_txt(txt_fld=txt_fld))

        keyboard = Button(master,width=8,text='Keyboard',command=lambda:self.key(keyboard=keyboard,Mic=Mic,txt_fld=txt_fld,submit=submit))

        Mic = Button(master,width=8,text='Mic',command=lambda:self.mic(keyboard=keyboard,Mic=Mic))

        btn.config(command=lambda: self.des_btn(btn=btn,keyboard=keyboard,Mic=Mic))

        btn.pack()

if __name__ == '__main__':
    global root,btn,txt_fld,submit,keyboard,Mic
    root = Tk()
    root.geometry('1355x850')
    root.title('Desktop  Assistant')
    root.config(bg='black')

    lb = GifLabel(root)
    lb.image_load('D:\\new.gif')
    lb.pack()

    w_thread = td.Thread(target = lambda:lb.window(master=root))
    w_thread.start()
    root.mainloop()
