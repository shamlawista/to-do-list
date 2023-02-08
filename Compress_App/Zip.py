import PySimpleGUI as sg
from Zipping import make_archive

label1 = sg.Text("Select files to compress")
# this will create an input widget
input1 = sg.Input()
# this is already programmed to browse file directory
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
# this is already programmed to choose a folder
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
# this will be a box where we indicate whether compression was successful or not
output_label = sg.Text(key="output")

window = sg.Window("File compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])
while True:
    event, values = window.read()
    # always print what you get, so that you know the types and what to do with them
    print(event, values)
    # in case we have multiple files, we need to split them into a list
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")
    if event == sg.WIN_CLOSED:
        break

window.close()
