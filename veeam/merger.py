import PySimpleGUI as sg
import psutil
import time
import sys

# This bit gets the taskbar icon working properly in Windows
if sys.platform.startswith("win"):
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        u"CompanyName.ProductName.SubProduct.VersionInformation"
    )
sg.theme("Dark Brown")





layout = [
    [sg.Text("Введите интервал проверки"), sg.InputText(key='-INPUT-', size=(10, 10))],
    [sg.Output(size=(88, 20))],
    [sg.Submit("Начать"), sg.Exit("закрыть")],
]

window = sg.Window(
    "Veeam homework",
    layout,
    resizable=False,
    finalize=True,
    icon="C:/Users/stass/OneDrive/Pictures/Thesquid.ink-Free-Flat-Sample-Space-rocket.ico",
)
def executeSomething():

    cpu = psutil.cpu_percent(interval=1)  # Вывод загрузки процессора в роцентах
    private_bytes = psutil.virtual_memory().used # Вывод работы оперативной памяти
    working_set = psutil.virtual_memory().percent  # Вывод работы оперативной памяти

    print(
        "\nЗагрузка процессора - {}% \nИспользование памяти - {}% \nПамять - {}".format(
            cpu, working_set, private_bytes
        )
    )
    number = values['-INPUT-']
    time.sleep(int(number))
    while True:
        executeSomething()

while True:
    event, values = window.Read()
    if event in (None, "Exit"):
        break
    if event == "Начать":
        executeSomething()

windows.close()
