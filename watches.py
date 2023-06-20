from tkinter import *
from datetime import *

now = datetime.now()

# окно
window = Tk()
window.title('Часы')
window.geometry('300x200')


# функция обновления времени каждую секунду
def tick():
    lbl_time.after(1000, tick)
    now = datetime.now()
    lbl_time['text'] = now.strftime('%H:%M:%S')


# Label
lbl_time = Label(window, font='Arial 20')
lbl_time.place(relx=0.5, rely=0.5, anchor=CENTER)

# запуск функции
tick()

window.mainloop()