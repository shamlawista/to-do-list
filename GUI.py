import functions
import PySimpleGUI as g

label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip="Enter todo", key="todo")
add_button = g.Button("Add")
list_box = g.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])
edit_button = g.Button("Edit")
complete_button = g.Button("Complete")
exit_button= g.Button("Exit")
window = g.Window('My to-do app',
                  layout=[[label],
                          [input_box, add_button],
                          [list_box, edit_button, complete_button],
                          [exit_button]
                          ],
                  font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_remove = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_remove)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case g.WIN_CLOSED:
            break
window.close()
