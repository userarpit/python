
from contextlib import contextmanager

class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename

    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'r')
            yield file
        finally:
            file.close()


# usage
message_writer = MessageWriter('access token.txt')
with message_writer.open_file() as my_file:
    print(my_file.readline())
