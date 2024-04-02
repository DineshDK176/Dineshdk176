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
    f_back,con  = 0,0

    #To Load the GIF image as a Label
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
        
        try:
                
            self.engine.say(txt)
            self.engine.runAndWait()
            
        except RuntimeError:
            time.sleep(5)
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
        self.con = con
        text = list(text)
        if res != None:
            res.split()
            c = 0
            for i in res:
                text[2] += i
                text[2] += ' '
                c += 1
                if c == 100:
                    text[2] += '\n'
                    c=0
        speech = td.Thread(target = self.speak,args = (text,con))
        speech.start()

    def r_voice(self):
        self.f_back=2
        if self.con != 1:
            mic = sr.Recognizer()
            with sr.Microphone() as source:
                self.Thread_speak("Wating for the Command...")
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

        elif ("youtube" in query):
            self.Thread_speak("Opening Youtube...")
            query = query.replace("youtube","")
            query = query.replace(" ","")
            webbrowser.open(f"youtube.com/results?search_query={query}")
            txt_fld.delete('1.0','end')

        elif ("wikipedia" in query):
            mk = mediawiki.MediaWiki()
            query = query.replace("wikipedia","")
            txt_fld.delete('1.0','end')
            try:
                self.Thread_speak("searching in wikipedia","According to wikipedia",'',res=mk.summary(query,sentences=3))
                
            except mediawiki.DisambiguationError as e:

                self.Thread_speak("Sorry the Information you looking is couldn't find...!")
                self.Thread_speak("Give Clear Content..")
            except Exception:
                self.Thread_speak("Please Check Your Internet and Try again")

        elif ("play" in query):
            
            try:
                query = query.replace("play","")
                yt.playonyt(query)
                self.Thread_speak("Starting...")
                txt_fld.delete('1.0','end')

            except Exception:
                self.Thread_speak("Please Check Your Internet and Try again")

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
                    self.Thread_speak('I cannot find the answer..')
                else :
                    self.Thread_speak(ans)
            except urllib.error.URLError :
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
        keyboard.pack_forget()
        self.f_back = 1
        Mic.pack()
        txt_fld.pack()
        submit.pack()

    def mic(self,keyboard=None,Mic=None,txt_fld=None,submit=None):
        Mic.pack_forget()
        txt_fld.pack_forget()
        submit.pack_forget()
        keyboard.pack()
        self.f_back = 0
        
    def window(self,master=None):

        #Destination of the Mic Image
        mic_ico = PhotoImage(file = "D:\\All Properties\\Python\\Projects\\SDAW\\Addeds\\Mic.png")

        #Destination of the Keyboard Image
        key_ico = PhotoImage(file = "D:\\All Properties\\Python\\Projects\\SDAW\\Addeds\\Keyboard.png")

        txt_fld = Text(master,width=50,height=1,bg='white',fg='black')

        submit = Button(master,text='Submit',width=10,command=lambda :self.get_txt(txt_fld=txt_fld))

        keyboard = Button(master,image = key_ico,command=lambda:self.key(keyboard=keyboard,Mic=Mic,txt_fld=txt_fld,submit=submit))

        Mic = Button(master,image = mic_ico,command=lambda:self.mic(keyboard=keyboard,Mic=Mic,txt_fld=txt_fld,submit=submit))

        keyboard.pack()
        
        self.welcome()

        self.r_voice()
        
        
if __name__ == '__main__':
    try:
        import pywhatkit as yt
    except Exception as e:
        pass

    global root
    
    root = Tk()
    root.geometry('1355x850')
    root.title('Desktop  Assistant')
    root.config(bg='black')

    lb = GifLabel(root)
    #Destination of the GIF image
    lb.image_load('D:\\All Properties\\Python\\Projects\\SDAW\\Addeds\\AI Interface.gif')
    lb.pack()

    w_thread = td.Thread(target = lambda:lb.window(master=root))
    w_thread.start()
    root.mainloop()
