import PySimpleGUI as sg
import image
import sys

# This bit gets the taskbar icon working properly in Windows
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation')
sg.theme('Dark Brown')

layout = [[sg.Text('Введите интервал проверки'), sg.InputText(size=(10, 10))],
          [sg.Output(size=(88, 20))],
          [sg.Submit('Начать'), sg.Cancel('закрыть')]]
window = sg.Window('Veeam homework', layout, resizable=False, finalize=True, icon='C:/Users/stass/OneDrive/Pictures/Thesquid.ink-Free-Flat-Sample-Space-rocket.ico')
while True:
    event, values = window.read()

    if event in (None, 'exit', 'закрыть'):
        break