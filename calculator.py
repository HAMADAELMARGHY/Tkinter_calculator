from tkinter import *
window=Tk()
window.title('Calculator')
window.resizable(1,0)
var_text=StringVar()
operator=''
##############################################################################################

# operation programing
#######################################################################################################
def display(number):
    global operator
    operator=operator + str(number)
    var_text.set(operator)



def equal():
    try:
        global operator
        result = str(eval(operator))  # the eval function evaluates the “String” like a python expression and returns the result as an integer.
        var_text.set(result)
        operator=result
    except Exception:
        pass

def clear():
    global operator
    var_text.set('')
    operator=''


#######################################################################################################

# widgets  design
#####################################################################################################

entry=Entry(window,bg='powder blue',bd=30,font=('arial',20,'bold'),justify='right',textvariable=var_text)
entry.grid(columnspan=4)
bt7=Button(window,text='7',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(7))
bt7.grid(column=0,row=1,padx=5,pady=5)
bt8=Button(window,text='8',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(8))
bt8.grid(column=1,row=1,padx=5,pady=5)
bt9=Button(window,text='9',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(9) )
bt9.grid(column=2,row=1,padx=5,pady=5)
bt_add=Button(window,text='+',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display('+'))
bt_add.grid(column=3,row=1,padx=5,pady=5)
bt4=Button(window,text='4',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(4))
bt4.grid(column=0,row=2,padx=5,pady=5)
bt5=Button(window,text='5',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(5))
bt5.grid(column=1,row=2,padx=5,pady=5)
bt6=Button(window,text='6',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(6))
bt6.grid(column=2,row=2,padx=5,pady=5)
bt_subtract=Button(window,text='-',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display('-'))
bt_subtract.grid(column=3,row=2,padx=5,pady=5)
bt1=Button(window,text='1',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(1))
bt1.grid(column=0,row=3,padx=5,pady=5)
bt2=Button(window,text='2',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(2))
bt2.grid(column=1,row=3,padx=5,pady=5)
bt3=Button(window,text='3',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(3))
bt3.grid(column=2,row=3,padx=5,pady=5)
bt_multiply=Button(window,text='x',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display('*'))
bt_multiply.grid(column=3,row=3,padx=5,pady=5)
bt0=Button(window,text='0',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display(0))
bt0.grid(column=0,row=4,padx=5,pady=5)
bt_clear=Button(window,text='C',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=clear)
bt_clear.grid(column=1,row=4,padx=5,pady=5)
bt_equal=Button(window,text='=',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=equal)
bt_equal.grid(column=2,row=4,padx=5,pady=5)
bt_division=Button(window,text='/',bg='#88888a',fg='#6b0000',font=('arial',20,'bold'),padx=16,bd=8,command=lambda:display('/'))
bt_division.grid(column=3,row=4,padx=5,pady=5)





window.mainloop()