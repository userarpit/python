import csv
import prime

class CSVFileManager:

    def __init__(self,file_path):
        self.file_path = file_path

    
    def read_csv(self):
        return self._read(delimiter = ',')
    
    def read_tsv(self):
        return self._read(delimiter = '\t')

    def _read(self,delimiter):
        with open(self.file_path,"r") as file:
            return [row for row in csv.reader(file,delimiter=delimiter)]

csv_comma = CSVFileManager("test.txt")
print(csv_comma.read_csv())