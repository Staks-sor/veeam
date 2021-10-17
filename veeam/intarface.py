import PySimpleGUI as sg
layout = [
    [sg.Text('Введите интервал проверки'), sg.InputText(size=(10, 10))
     ],

    [sg.Output(size=(88, 20))],
    [sg.Submit("Начать"), sg.Cancel()]
]
window = sg.Window('File Compare', layout)
while True:
    event, values = window.read()

    if event in (None, 'Exit', 'Cancel'):
        break