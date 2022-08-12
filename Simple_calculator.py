from tkinter import *
window=Tk()
window.geometry('250x300')
window.resizable(0,0)
window.configure(bg='black')
window.title('simple calculator')
##########################################################################################################
first=StringVar()
second=StringVar()
third=StringVar()
#########################################################################################################
# Button Commands
########################################################################################################


def addition():
    third.set('+')


def subtraction():
    third.set('-')


def multiplication():
    third.set('x')


def division():
    third.set('÷')


def equal():
    try:
        if third.get()=='+':
            third.set(float(first.get())+float(second.get()))    # x=(third.get())
            first.set(third.get())
            second.set('')
        elif third.get()=='-':
            third.set(float(first.get())-float(second.get()))
            first.set(third.get())
            second.set('')
        elif third.get() == 'x':
            third.set(float(first.get()) * float(second.get()))
            first.set(third.get())
            second.set('')
        elif third.get() == '÷':
            third.set(float(first.get()) / float(second.get()))
            first.set(third.get())
            second.set('')
    except Exception:
        pass


################################################################################################################
# Widgets Design
###############################################################################################################
label_first=Label(window,text='First',bg='black',fg='#641E16',font=('arial',12,'italic'),bd=5)
label_second=Label(window,text='Second',bg='black',fg='#641E16',font=('arial',12,'italic'),bd=5)
label_answer=Label(window,text='Answer',bg='black',fg='#641E16',font=('arial',12,'italic'),bd=5)
btn_add=Button(window,text='+',bd=4,font=('arial',8,'bold'),bg='#641E16',activebackground='#641E16',command=addition)
btn_sub=Button(window,text='-',bd=4,font=('arial',8,'bold'),bg='#641E16',activebackground='#641E16',command=subtraction)
btn_mult=Button(window,text='x',bd=4,font=('arial',8,'bold'),bg='#641E16',activebackground='#641E16',command=multiplication)
btn_div=Button(window,text='÷',bd=4,font=('arial',8,'bold'),bg='#641E16',activebackground='#641E16',command=division)
btn_equal=Button(window,text='=',bd=6,bg='#641E16',width=3,activebackground='#641E16',command=equal)
first_ent=Entry(window,textvariable=first,bg='#1A5276',font=('arial',10,'italic'),bd=4)
second_ent=Entry(window,textvariable=second,bg='#1A5276',font=('arial',10,'italic'),bd=4)
third_ent=Entry(window,textvariable=third,bg='#1A5276',font=('arial',10,'italic'),bd=4)
#####################################################################################
# Widgets Geometry Management
########################################################
label_first.place(x= 5,y=10)
label_second.place(x=5 ,y=70)
label_answer.place(x=5 ,y=220)
btn_add.place(x= 105,y=140)
btn_sub.place(x= 135,y= 140)
btn_mult.place(x= 165,y=140)
btn_div.place(x= 195,y=140 )
btn_equal.place(x=130,y=255)
first_ent.place(x=90,y=10)
second_ent.place(x=90,y=70)
third_ent.place(x=90,y=220)
window.mainloop()