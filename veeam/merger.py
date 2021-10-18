import sys
import time
import PySimpleGUI as sg
import psutil
import win32api
import win32con
import datetime
import json
import ctypes

if sys.platform.startswith("win"):


    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        u"CompanyName.ProductName.SubProduct.VersionInformation"
    )
sg.theme("Dark Brown")

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


def executeSomething():
    cpu = psutil.cpu_percent(interval=1)  # Вывод загрузки процессора в роцентах
    private_bytes = psutil.virtual_memory().used  # Вывод работы оперативной памяти
    working_set = psutil.virtual_memory().percent  # Вывод работы оперативной памяти
    handle = psutil.Process().pid
    current_time = datetime.datetime.now().strftime("%F %T")
    log_str = "|---------------------|---------- |-----------------|-----------------|-----------------------------|\n"
    log_str += "|---------time--------|----cpu----|--private_bytes--|---working_set---|-------------handle----------|\n"

    log_str += (
        "| %s |   %s%%    |   %s   |%s%%            | %s                       |\n"
        % (current_time, cpu, private_bytes, working_set, handle)
    )
    print(log_str)
    f = open("log.json", "a")  # Новый log.txt
    f.write(log_str + "\n\n")  # Написать информацию
    f.close()

    print(
        "\nЗагрузка процессора - {}% \nИспользование памяти - {}% \nПамять - {} \nОткрытые хендлы - {}".format(
            cpu, working_set, private_bytes, handle
        )
    )
    number = values["-INPUT-"]

    time.sleep(int(number))
    while True:
        executeSomething()


while True:
    event, values = window.Read()
    if event in (None, "Exit", 'закрыть'):
        break
    if event == "Начать":
        executeSomething()

windows.quit()
