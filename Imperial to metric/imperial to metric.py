import PySimpleGUI as sg
import calculation


feet_label = sg.Text("Enter feet")
feet_input = sg.Input(key='feet')
inches_label = sg.Text("Enter inches")
inches_input = sg.Input(key='inches')

convert_button = sg.Button("Convert")
result_text = sg.Text(key='result')


window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [convert_button, result_text]])
while True:
    event, values = window.read()
    match event:
        case "Convert":
            print(event)
            print(values)
            calculated_result = calculation.convertor(float(values['feet']), float(values['inches']))
            window['result'].update(value=calculated_result)
        case sg.WIN_CLOSED:
            break

window.close()
