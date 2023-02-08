import functions
import PySimpleGUI as g

label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip="Enter todo", key="todo")
add_button = g.Button("Add")
window = g.Window('My to-do app',
                  layout=[[label], [input_box, add_button]],
                  font=('Helvetica', 20))
# now we want a loop to keep running such that the app doesnt close after adding sth
while True:
    # we want to store what happens when we save the window.read()
    event, values = window.read()
    print(event)
    print(values)
    # now we add a match case, to check which button was pressed
    match event:
        case "Add":
            # we call the function to open and read the txt file
            todos = functions.get_todos()
            # we store the new to-do in a variable
            new_todo = values['todo'] + "\n"
            # we update the to-do list that we read
            todos.append(new_todo)
            # now we write it back to the txt file
            functions.write_todos(todos)
        # finally, we need to be able to exit the loop when we press on the "x" symbol to close the window
        case g.WIN_CLOSED:
            break
window.close()
