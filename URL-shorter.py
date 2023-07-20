import pyperclip
import pyshorteners
from tkinter import *


#GUI for url short converter

window=Tk()
window.geometry('800x300')
window.title("URLs Short converter:")
window.configure(bg='#FFFFFF')
paste_url=StringVar()
shorted_url_addrerss=StringVar()


#function for short converter
def urlshort():
  address=paste_url.get()
  url_short=pyshorteners.Shortener().tinyurl.short(address)
  shorted_url_addrerss.set(url_short)
  

#function to get copied of shorted url 
def copyurl():
  url_short=shorted_url_addrerss.get()
  pyperclip.copy(url_short)
  


#GUI 
Label(window,text='URLs Short Converter',fg='#00acee',font='poppins').pack(pady=10)
Entry(window,textvariable=paste_url,width=65,highlightcolor= "#00acee",highlightthickness=2).pack(pady=10)
Button(window,text='Generate Short URL',command=urlshort,fg='white',bg='#00acee').pack(pady=10)
Entry(window,textvariable=shorted_url_addrerss,width=65,highlightcolor= "#00acee",highlightthickness=2).pack_configure(pady=30)
Button(window,text='Copy URL',fg='white',command=copyurl,bg='#00acee').pack(pady=10)

window.mainloop()