from tkinter import *
from datetime import *
import winsound

today = date.today()

# окно
window = Tk()
window.title('Часы')
window.geometry('500x400')
window.configure(bg='#333333')

# текстовое поле для ввода времени, на которое нужно установить будильник
hour_input = Entry(window, width=13)
hour_input.place(relx=0.2, rely=0.8)

minute_input = Entry(window, width=13)
minute_input.place(relx=0.4, rely=0.8)

sec_input = Entry(window, width=13)
sec_input.place(relx=0.6, rely=0.8)


# функция установки будильника
def set_alarm():
    now = datetime.now()

    # получаем данные с поля ввода
    hour_alarm = int(hour_input.get())
    minute_alarm = int(minute_input.get())
    sec_alarm = int(sec_input.get())

    # получаем текущее время по отдельности
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    # время будильника в секундах
    sec_alarm = (hour_alarm * 60 + minute_alarm) * 60

    # текщее время в секундах
    current_sec = (current_hour * 60 + current_min) * 60

    # таймер
    taimer = sec_alarm - current_sec

    window.after(taimer * 1000, alarm)

    # стираем введенный текст с поля ввода
    hour_input.delete(0, END)
    minute_input.delete(0, END)
    sec_input.delete(0, END)

# кнопка "Установить будильник"
btn = Button(window, text='Установить будильник', command=set_alarm)
btn.place(relx=0.35, rely=0.9)


# функция вызова будильника
def alarm():
    winsound.Beep(250, 10000)


# функция обновления времени каждую секунду
def tick():
    lbl_hour_int.after(1000, tick)

    now = datetime.now()

    lbl_hour_int['text'] = now.hour
    lbl_minute_int['text'] = now.minute
    lbl_second_int['text'] = now.second

    winsound.Beep(250, 300)

    if now.minute == 0 and now.second == 0:  # если наступил новый час
        winsound.Beep(130, 500)

    if now.second == 0:  # если наступила новая минута
        winsound.Beep(190, 400)

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
