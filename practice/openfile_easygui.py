import easygui as gui

path = gui.fileopenbox(msg="Select a file")
print(path)
with open(path, mode="r") as file:
    print(file.read())

path = gui.diropenbox(msg="select dir")
print(path)

