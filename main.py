from functions import get_todos, write_todos
import functions
import time
time_now = time.strftime("%d-%b-%Y %H:%M:%S")
print("It is now", time_now)
while True:
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]+'\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith('show'):
        todos = get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])-1
            todos = get_todos()
            print("You will replace this item")
            print(todos[number])
            new_todo = input("Enter you new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(list_to_write=todos)
        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('remove'):
        try:
            removed_item = int(user_action[7:])-1
            todos = get_todos()
            todo_to_remove = todos[removed_item].strip('\n')
            todos.pop(removed_item)
            write_todos(todos)
            message = f"Todo ({todo_to_remove}) was removed from the list"
            print(message)
        except IndexError:
            print('Invalid command')
            continue
        except ValueError:
            print('Please enter the number of the todo to remove')
    elif user_action.startswith('exit'):
        break
    else:
        print('Enter a correct input')
print('Goodbye!!')
