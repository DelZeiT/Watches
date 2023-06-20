from tkinter import *

# окно
window = Tk()
window.title('Часы')
window.geometry('300x200')

# Label
lbl_time = Label(window, font='Arial 20')
lbl_time.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()