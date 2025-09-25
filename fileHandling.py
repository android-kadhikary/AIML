# file1= open("karabi.txt","r")
# containt = file1.read() # this is for reading full file in a string
# print("----Reading line by line----" ,containt)
# for line in containt:
#     print(line)
# file1.close()

# with open ("karabi.txt","r") as reader1 : # this is the best way to handle file, 
#                                             # stored in variable reader1, IO stream
#     for l1 in reader1:
#         print(l1.strip())

# with open ("karabi.txt","r") as reader :
#     print(reader.readline())
#     print("----Reading full file----")
#     print(reader.read())

# try:
#     with open ("karabi.txt","r") as reader3 :
#         print(reader3.read(7))  # read 7 characters
# except FileNotFoundError as e:
#     print(f"Error: {e}")
# finally:
#     print("Execution completed")    

# with open ("karabi.txt","a") as writer :
#     writer.write("\nI am appending this line.")

import os
print("Current working directory:", os.getcwd())
#print("List of files and directories in current directory:", os.listdir())
# os.rename("old_filename.txt", "new_filename.txt")
# os.remove("new_filename.txt") # to delete a file
# os.mkdir("new_directory") # to create a new directory
# os.rmdir("new_directory") # to remove a directory
# os.chdir("new_directory") # to change the current working directory

from pathlib import Path
file2= open("karabi_1.txt","w")
file2.close()
path = Path("karabi_1.txt")
# print("File exists:", path.exists())
# print("File name:", path.name)
# print("File suffix:", path.suffix)  
# print("File stem:", path.stem)
# print("Parent directory:", path.parent)
# print("File size in bytes:", path.stat().st_size)
# print("File permissions:", path.stat().st_mode)
# print("File last modified time:", path.stat().st_mtime)
# print("File last accessed time:", path.stat().st_atime)
# print("File creation time:", path.stat().st_ctime)
# print("Is it a file?", path.is_file())
# print("Is it a directory?", path.is_dir())
# print("Absolute path:", path.resolve())
# print("Home directory:", Path.home())
# print("Current directory:", Path.cwd())
# print("Parts of the path:", path.parts)
# print("Is the path absolute?", path.is_absolute())


# print("Joining paths:", path.parent / "newfile.txt")
# print("Iterating over directory contents:")

file_new = path.parent / "karabi_renamed.txt"
file_new1 = path.parent / "karabi_1.txt"
print("New file path:", file_new)
try:
    path.rename("karabi_renamed.txt")
except FileExistsError as e:
    print(f"Error: {e}")
