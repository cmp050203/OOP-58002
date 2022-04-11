from tkinter import *
window=Tk()

def Fullname():
    name['text'] = 'Myname'

label = Label(text='Enter your Fullname:', fg='Green')
label.place(x=30, y=50)

button = Button(text='Click to display your Fullname', fg='Green', command=Fullname)
button.place(x=30, y=100)

entername = Entry(textvariable='Myname', bd='5')
entername.place(x=230, y=50)

name = Entry(text='This is my name', bd='5')
name.place(x=230, y=100)

window.title('Midterm in OOP')
window.geometry("500x200+10+10")
window.mainloop()