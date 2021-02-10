import os
import shutil
import re
import ntpath



def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


cur_dir = os.getcwd()


file_type = str(input('What file you want to move: ')).lower()
targetted_contents = list()

destination_directory = cur_dir + '/' + file_type.upper()
print('Destination directory: ' + destination_directory)

# check if destination directory exists or not
# if not then create a new directory
if not os.path.isdir(destination_directory):
    os.mkdir(destination_directory)


# at this point new destination folder is there

regx = re.compile(r'')


print('File type: ' + file_type)

for x in os.listdir(cur_dir):
    if x.endswith(file_type):
        targetted_contents.append(x)

if file_type == 'py':
    targetted_contents.remove(ntpath.basename(__file__))

print('Targetted content: ' + str(targetted_contents))



contents_of_destination_directory = list()

for x in os.listdir(destination_directory):
    contents_of_destination_directory.append(x)

print('Destination directory contents: ' + str(contents_of_destination_directory))

# if there are common files in both directories then dont' move files
# from source to destination
files_to_move = list()

for x in targetted_contents:
    if x not in contents_of_destination_directory:
        files_to_move.append(x)

# files_to_move contains the files which are to be moved
for x in files_to_move:
    shutil.copy2(os.path.join(cur_dir, x), destination_directory)
    print('Copied: ' + x)