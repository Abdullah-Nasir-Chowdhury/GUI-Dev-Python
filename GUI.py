# hello_world.py

import PySimpleGUI as sg

# sg.Window(title="Hello World", layout=[[]], margins=(100,50)).read()

layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]

# create the window
window = sg.Window("Demo", layout)

# create an event loop
while True:
    event, values = window.read()
#     End program if user closes window or
#     presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

