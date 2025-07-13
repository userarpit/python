import json


# function to add to JSON
def write_json(new_data, filename="conda.txt"):
    with open(filename, "r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # print(file_data)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended


y = {"emp_name": "Arpit", "email": "masterarpit@gmail.com", "job_profile": "Full Time"}

write_json(y)
