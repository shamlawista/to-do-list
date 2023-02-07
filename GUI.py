import functions
# this will save us from writing PySimpleGUI all the time
import PySimpleGUI as g

# this will create a label that can be shown in the window
label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip= "Enter todo")
# now we want to add a button
add_button = g.Button("Add")
# this creates a window, and you insert the name between the parenthesis, and connect the other instances to it
window = g.Window('My to-do app', layout=[[label], [input_box, add_button]])
# now we want to display the window on the screen
window.read()
# this will create a "close window" button
window.close()
