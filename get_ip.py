from requests import get
from tkinter import *

window=Tk()
window.geometry('400x100+200+100')
window.title('Your Public Ip')
window .configure(bg='black')
window.resizable(0,0)
var = StringVar()

def btn_clicked():
    var.set(get('https://api.ipify.org/').text)


entry=Entry(window,bg='cyan',textvariable=var,fg='black',state='readonly',font=('arial',12,'bold'),justify='center')
entry.place(x=110,y=20)
btn=Button(window,text='Get',bg='gray',fg='red',font=('arial',10,'bold'),width=4,height=1,command= btn_clicked,bd=5)
btn.place(x=175,y=55)


window.mainloop()