import csv
with open('bank-data.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        cust = []
        next(csvFile,None)
        for lines in csvFile:
                cust.append(lines)

#print(cust)
jobs = []
age = []
for line in cust:
	jobs.append(line[1])
	age.append(int(line[0]))

unique_jobs = list(set(jobs))
#print(unique_jobs)

while(True):
	profession = input("type 'END' to quit, Enter profession - ")
	if profession == 'END':
		break

	if profession.lower() in unique_jobs:
		print("Client is eligible")
	else:
		print("Client is not eligible")

age_dict = {}
age_dict["Max"] = max(age)
age_dict["Min"] = min(age)
#print(type(age_dict))
