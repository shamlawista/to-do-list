import functions
import PySimpleGUI as g

label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip="Enter todo", key="todo")
add_button = g.Button("Add")
# this will create a list box and show a list in it. in this case it is the to-do list
# we will attach a key to it, and adjust its size
list_box = g.Listbox(values =functions.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])
# we will also create a new edit button
edit_button = g.Button("Edit")
# now we display the list_box in a new row
window = g.Window('My to-do app',
                  layout=[[label],
                          [input_box, add_button],
                          [list_box, edit_button]
                          ],
                  font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            # first we choose the to-do that we want to edit. for that, we check what values is returned
            # from the window.read(), and we find that the key "todos' will return a list from which we need the
            # first element
            todo_to_edit = values['todos'][0]
            # then we store the new to-do which is in the input box in a variable
            new_todo = values['todo'] + "\n"
            # now we read the todos that we have and store them in a list
            todos = functions.get_todos()
            # then we get the index of the to-do to edit
            index = todos.index(todo_to_edit)
            # now we replace the to-do inside the list
            todos[index] = new_todo
            # finally we write it back to the file
            functions.write_todos(todos)
            # now we want to refresh the list box, we do this by pointing to the to-do box using its key
            # and then by specifying which values do we use to update it with
            window['todos'].update(values=todos)
        case 'todos':
            # now we want to replace the current selection with what we click on from the list_box
            window['todo'].update(value=values['todos'][0])
        case g.WIN_CLOSED:
            break
window.close()
