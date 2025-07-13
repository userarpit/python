import multiprocessing, os

def print_records(records):
	"""
	function to print record(tuples) in records(list)
	"""
	for record in records:
        
		print("Name: {0}\nScore: {1}\n".format(record[0], record[1]));print("p2",os.getpid())


    

def insert_record(record, records):
	"""
	function to add a new record to records(list)
	"""
	records.append(record)
	print("New record added!\n");print("p1",os.getpid())

if __name__ == '__main__':
    print(os.getpid())
    with multiprocessing.Manager() as manager:
		# creating a list in server process memory
        records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)])
		# new record to be inserted in records
        new_record = ('Jeff', 8);print("server process",os.getpid())

		# creating new processes
        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

		# running process p1 to insert new record
        p1.start()
        p1.join()

		# running process p2 to print records
        p2.start()
        p2.join()