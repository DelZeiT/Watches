from tkinter import *
from datetime import *

now = datetime.now()
today = date.today()

# окно
window = Tk()
window.title('Часы')
window.geometry('300x200')
window.configure(bg='black')


# функция обновления времени каждую секунду
def tick():
    lbl_time.after(1000, tick)
    now = datetime.now()
    lbl_time['text'] = now.strftime('%H:%M:%S')


# Label
lbl_time = Label(window, font='Arial 20', background="#FFA500", foreground="#FFFFFF")
lbl_time.place(relx=0.5, rely=0.5, anchor=CENTER)

lbl_date = Label(window, text=today, font='Arial 10', background="#FFA500", foreground="#FFFFFF")
lbl_date.grid(column=0, row=0)

# запуск функции
tick()

window.mainloop()