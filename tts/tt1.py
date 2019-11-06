from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os

root=Tk()
root.geometry('400x300')
root.title("TalkIt")
lab1=Label(root,text='Text To Speech Convertor',bg='powder blue',fg='black',font=('arial 16 bold')).pack()
root.config(background='powder blue')

lab2=Label(root,text='Enter text',font=('arial 16'),bg='powder blue',fg='black').pack()
mytext=StringVar()
chkvar=BooleanVar()
chkvar.set(False)

def fetch():
	language='en'
	myob=gTTS(text=mytext.get(),lang=language,slow=False)
	myob.save('Voice1.mp3')
	
def play():
	from pygame import mixer
	mixer.init()
	mixer.music.load("Voice1.mp3")
	mixer.music.play()
   
def fileinp():
	fileName=filedialog.askopenfilename(filetypes=( ("Text files","*.txt") , ("All files","*.*") ) )
	print(fileName)	
	os.system("gtts-cli -f %s --output Voice1.mp3"%fileName)
	#play()


ent1=Entry(root,tex=mytext,font=('arial 13')).pack()

but1=Button(root,text='Convert',width=20,bg='brown',fg='white',command=fetch).place(x=125,y=100)

but2=Button(root,text='Play file',width=20,bg='brown',fg='white',command=play).place(x=125,y=140)

but3=Button(root,text='Input file',width=20,bg='brown',fg='white',command=fileinp).place(x=125,y=180)

Button(root, text='Quit',width=20,bg='brown',fg='white', command=root.quit).place(x=125,y=220)

#chk1=Checkbutton(root,text='Slow mode',width=8,variable=chkvar).place(x=345,y=140)

root.mainloop()

          
