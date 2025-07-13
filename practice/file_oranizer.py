import os
import shutil

# get the path of the directory from the user, where file needs to be organize
directory_path = input("Enter the full directory path, where files need to be organize: ")
# print(directory_path)

# check for the existance of the directory
while True:
    if not os.path.isdir(directory_path):
        print('the path is not a directory!')
        directory_path = input("Enter the full directory path, where files need to be organize: ")
    else:
        break

# change the path of the directory
os.chdir(directory_path)

# get the list of sub-directory and files
entries = os.listdir(directory_path)

# ignore the sub-directory and scan through all the files 
# and create sub-directory based on their extension, 
# and move the corresponding file into its subfolders

for file in entries:
    if not os.path.isdir(file):
        name, ext = os.path.splitext(file)
        extension = ext[1:]
        os.makedirs(extension, exist_ok=True)
        # move the file into the respective folder
        shutil.copy(file, extension)
        # after copy, remove the file
        os.remove(file)

print("file organize is successful!")