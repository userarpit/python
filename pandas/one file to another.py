file_data = []
with open("jenkinsfile","r") as file:
    for line in file:
        file_data.append(line)
        # print(line)

# print(file_data)
with open("copy jenkinsfile","w") as file:
    file.write("".join(file_data))
