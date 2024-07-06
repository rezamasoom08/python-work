# importing module
import os
 
# path of the current script
path = 'C:/Users/Mreza/Documents/VS Code'
 
# Before creating
dir_list = os.listdir(path)
print("List of directories and files before creation:")
print(dir_list)
print()
 
# Creates a new file
with open('C:/Users/Mreza/Documents/VS Code/myfile.txt', 'w') as fp:
    pass
 
# After creating
dir_list = os.listdir(path)
print("List of directories and files after creation:")
print(dir_list)

f = open("C:/Users/Mreza/Documents/VS Code/myfile.txt", 'w')
f.write("Hi! I am max. :)")
f.close

f = open("C:/Users/Mreza/Documents/VS Code/myfile.txt", 'r')
print(f.read())
