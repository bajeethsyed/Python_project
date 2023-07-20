from tkinter.ttk import *
from tkinter import *
from threading import Thread

from datetime import datetime
from time import sleep

from pygame import mixer

window = Tk()
window.title("Alarm-Clock")
window.geometry('300x150')
window.configure(bg='#ffffff')

body=Frame(window, width=300, height=150, bg='#ffffff')
body.grid(row=0,column=0)

name = Label(body,text='Set Your Alarm',font=('poppins 15 bold'),bg='#ffffff')
name.place(x=75,y=10)

hr=Label(body,text='Hour',font=('poppins 10 bold'),bg='#ffffff')
hr.place(x=20,y=45)
d_hr=Combobox(body,width=5,font=('poppins 13 bold'))
d_hr['values']=('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
d_hr.current(0)
d_hr.place(x=20,y=70)

min=Label(body,text='Minute',font=('poppins 10 bold'),bg='#ffffff')
min.place(x=100,y=45)
d_min=Combobox(body,width=5,font=('poppins 13 bold'))
d_min['values']=('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
d_min.current(0)
d_min.place(x=100,y=70)

pr=Label(body,text='Period',font=('poppins 10 bold'),bg='#ffffff')
pr.place(x=180,y=45)
d_pr=Combobox(body,width=5,font=('poppins 13 bold'))
d_pr['values']=('AM','PM')
d_pr.current(0)
d_pr.place(x=180,y=70)

selected=IntVar()

def start():
  t=Thread(target=alarm)
  t.start()
  
def stop():
  mixer.music.stop()
  
rad = Radiobutton(body,font=('poppins 10 bold'),value=1,text='Start',bg='#ffffff',command=start,variable=selected)
rad.place(x=20,y=100)


def ring_alarm():
  mixer.music.load('alarm-clock.mp3')
  mixer.music.play()
  selected.set(0)
  
  rad1 = Radiobutton(body,font=('poppins 10 bold'),value=2,text='Stop',bg='#ffffff',command=stop,variable=selected)
  rad1.place(x=100,y=100)
  

def alarm():
  set_hr=d_hr.get()
  set_min=d_min.get()
  set_pr=d_pr.get()
  while 1:
    
    now=datetime.now()
    p_hr=now.strftime('%I')
    p_min=now.strftime('%M')
    p_pr=now.strftime('%p')
    print(selected.get(),p_hr,p_min,p_pr)
    
    if p_pr == set_pr:
      if p_hr == set_hr:
        if p_min == set_min:
          ring_alarm()
          break
    
    sleep(1)
    


mixer.init()
window.mainloop()