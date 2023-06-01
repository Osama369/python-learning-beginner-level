
import os

#create function to get files path and its directories from the system

def display_directory(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print('{}{}'.format(sub_indent, file))  
        # return files


# promt the user input  for directory path:
directory_path  =input(">>Enter the directory path")
files =display_directory(directory_path)
print(files)







