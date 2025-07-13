from contextlib import contextmanager

class MessageWriter(object):
	def __init__(self, filename):
		self.file_name = filename

	@contextmanager
	def open_file(self):
		try:
			file_name = open(self.file_name, 'w')
			yield file_name
		finally:
			file_name.close()
# usage
message_writer = MessageWriter('foo.txt')
with message_writer.open_file() as my_file:
	my_file.write('hello world')