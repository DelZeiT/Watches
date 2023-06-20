from tkinter import *
from datetime import *
import winsound

now = datetime.now()
today = date.today()

# окно
window = Tk()
window.title('Часы')
window.geometry('500x250')
window.configure(bg='#333333')


# функция обновления времени каждую секунду
def tick():
    lbl_hour_int.after(1000, tick)
    now = datetime.now()
    lbl_hour_int['text'] = now.hour
    lbl_minute_int['text'] = now.minute
    lbl_second_int['text'] = now.second
    winsound.Beep(250, 400)


# Label
# виджет часов
lbl_hour_int = Label(window, font='Arial 50', bg="#00CC99", fg="#FFFFFF")
lbl_hour_int.place(relx=0.2, rely=0.2)

# виджет минут
lbl_minute_int = Label(window, font='Arial 50', bg="#0099FF", fg="#FFFFFF")
lbl_minute_int.place(relx=0.4, rely=0.2)

# виджет секунд
lbl_second_int = Label(window, font='Arial 50', bg="#660099", fg="#FFFFFF")
lbl_second_int.place(relx=0.6, rely=0.2)

# виджет "часы"
lbl_hour_str = Label(window, text='   часы   ', font='Arial 14', bg="#00CC99", fg="#FFFFFF")
lbl_hour_str.place(relx=0.2, rely=0.6)

# виджет "минуты"
lbl_minute_str = Label(window, text=' минуты ', font='Arial 14', bg="#0099FF", fg="#FFFFFF")
lbl_minute_str.place(relx=0.4, rely=0.6)

# виджет"секунды"
lbl_second_str = Label(window, text='секунды', font='Arial 15', bg="#660099", fg="#FFFFFF")
lbl_second_str.place(relx=0.6, rely=0.6)

# виджет даты
lbl_date = Label(window, text=today, font='Arial 10', background="#00CC33", foreground="#FFFFFF")
lbl_date.grid(column=0, row=0)

# запуск функции
tick()

window.mainloop()