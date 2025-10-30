import os
print("OS name ",os.name)
corrent_dir=os.getcwd()
print("current dir ",os.getcwd())
print("change dir path ",os.chdir("C:\FileIO_test"))

new_dir=os.getcwd()
print("current dir ",new_dir)
#print("make dir ",os.mkdir("Karabi_test_dir"))

new_path=new_dir+"\Karabi_test_dir"
os.makedirs(new_path, exist_ok=True) # no error if the folder is available
filename="karabi.txt"
full_new_path=os.path.join(new_path,filename)  # concatinate or join, Parent folder, subfolder,file

with open(full_new_path,"w"):
    print (full_new_path, "created ")
if os.path.exists(full_new_path):
    print("new_path exist at ", os.getcwd())
    print("files and folders ", os.listdir())
print("remove path ", os.remove(full_new_path))



if os.path.exists(corrent_dir):
    print("exist")

if os.path.exists(full_new_path):
    print("new_path exist")
else: print("new_path NOT exist")