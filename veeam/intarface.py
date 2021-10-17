import PySimpleGUI as sg
sg.theme('Dark Brown')

layout = [
    [sg.Text('Введите интервал проверки'), sg.InputText(size=(10, 10))
     ],
    [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]],

    [sg.Output(size=(88, 20))],
    [sg.Submit("Начать"), sg.Cancel()]
]
window = sg.Window('File Compare', layout)
while True:
    event, values = window.read()

    if event in (None, 'Exit', 'Cancel'):
        break