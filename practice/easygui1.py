import easygui as gui

# print(gui.msgbox(msg="Hello!", ok_button = "Click me!"))
color_tuple = ("Red","blue","yellow")
color = gui.indexbox(
    msg="select color",
    title="color",
    choices=color_tuple
)
print(color)
print(color_tuple[color])

color_value = gui.enterbox(msg="which color", title="choose")
print(color_value)
gui.msgbox("Please provide a valid page number.", "Whoops!")