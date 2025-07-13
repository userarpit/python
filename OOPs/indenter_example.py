class Indenter:

    def __init__(self):
        self.lvl = -1

    def __enter__(self):
        # print("enter")
        self.lvl += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("exit")
        self.lvl -= 1

    def print(self, text):
        # print("print")
        print("    " * self.lvl + text)


indent = Indenter()
with indent:
    indent.print("hi")
    with indent:
        indent.print("hello")
        with indent:
            indent.print("bonjour")
    indent.print("hey")
