def get_todos(filepath="todo.txt"):
    """ this function will read the content of a file, and return the lines in a list"""
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos


def write_todos(list_to_write, filepath="todo.txt"):
    """ writes a list into a file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(list_to_write)


if __name__ == "__main__":
    print('Hello')
