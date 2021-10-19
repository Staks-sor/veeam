import sys
import time
import PySimpleGUI as sg
import psutil
import win32api
import win32con
import datetime
import ctypes
import base64
import threading

if sys.platform.startswith("win"):


    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        u"CompanyName.ProductName.SubProduct.VersionInformation"
    )
sg.theme("Dark Brown")
class win(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        layout = [
            [
                sg.Text("Введите интервал проверки в секундах"),
                sg.InputText(key="-INPUT-", size=(10, 10)),
            ],
            [sg.Output(size=(88, 20))],
            [sg.Submit("Начать"), sg.Exit("закрыть")],
        ]

        window = sg.Window(
            "Test exercise",
            layout,
            resizable=False,
            finalize=True,
            icon="C:/Users/stass/OneDrive/Pictures/Thesquid.ink-Free-Flat-Sample-Space-rocket.ico",
        )
        while True:
            event, values = window.Read()
            if event in (None, "Exit", 'закрыть'):
                break
            if event == "Начать":
                thread1 = st('Thread1', 1)
                thread1.start()


class st(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        cpu = psutil.cpu_percent(interval=1)  # Вывод загрузки процессора в роцентах
        private_bytes = psutil.virtual_memory().used  # Вывод работы оперативной памяти
        working_set = psutil.virtual_memory().percent  # Вывод работы оперативной памяти
        handle = psutil.Process().pid
        current_time = datetime.datetime.now().strftime("%F %T")
        log_str = " time            {}\n cpu             {}%\n private_bytes   {}\n working_set     {}%\n handle          {}\n".format(
            current_time, cpu, private_bytes, working_set, handle)

        f = open("log.txt", "a")  # Новый log.txt
        f.write(log_str + "\n\n")  # Написать информацию
        f.close()

        print(
            "\nЗагрузка процессора - {}% \nИспользование памяти - {}% \nПамять - {} \nОткрытые хендлы - {}".format(
                cpu, working_set, private_bytes, handle
            )
        )




thread0 = win('Thread0', 0)
thread0.start()






