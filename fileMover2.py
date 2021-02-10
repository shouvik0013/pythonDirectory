import os
import shutil
import ntpath
from tqdm import tqdm
import time


# current directory as global variable
CUR_DIR = os.getcwd()


class FileMover(object):

    def __init__(self):
        self.cur_dir = CUR_DIR
        self.destination_dir = None
        self.destination_dir_existed = True
        self.file_type = None
        self.contents_cur_dir = list()
        self.contents_des_dir = list()
        self.files_to_be_moved = list()
        self.common_files = list()

    @classmethod
    def path_leaf(cls,path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def user_input(self):
        self.file_type = str(input('Enter the file type: ')).lower()
        return

    def destination_dir_check_create(self):
        self.destination_dir = os.path.join(self.cur_dir, self.file_type.upper())
        if not os.path.isdir(self.destination_dir):
            self.destination_dir_existed = False
            os.mkdir(self.destination_dir)
            print(FileMover.path_leaf(self.destination_dir) + ' Created...')
            return
        print(FileMover.path_leaf(self.destination_dir) + ' is already here...')
        return

    def create_list_of_files_to_be_moved(self):
        for x in os.listdir(self.cur_dir):
            if x.endswith(self.file_type):
                self.contents_cur_dir.append(x)
        # remove the source file if file-type is .py
        if self.file_type == 'py':
            self.contents_cur_dir.remove(__file__)
        # if previously des_dir existed then check its contents
        if self.destination_dir_existed:
            for x in os.listdir(self.destination_dir):
                self.contents_des_dir.append(x)
        # if destination directory has some files
        # which are also present in cur_dir then there are 2 possibilities
        # if dest_dir has updated files then not move file
        # from cur_dir
        # if dest_dir has outdated file then remove file and copy file
        # from source folder

        # copying the current directory contents
        self.files_to_be_moved = self.contents_cur_dir[:]

        for x in self.contents_cur_dir:
            if x in self.contents_des_dir:
                # now x is common file to both folders
                if os.stat(os.path.join(self.cur_dir, x)) < os.stat(os.path.join(self.destination_dir, x)):
                    self.files_to_be_moved.remove(x)
        return

    def move_files(self):
        for x in tqdm(iterable=self.files_to_be_moved):
            shutil.copy2(os.path.join(self.cur_dir, x), os.path.join(self.destination_dir))
            #print('Moved: ' + str(x))
            time.sleep(.2)
        print('All {} files has been moved'.format(str(len(self.files_to_be_moved))))


obj1 = FileMover()
obj1.user_input()
obj1.destination_dir_check_create()
obj1.create_list_of_files_to_be_moved()
#print(obj1.files_to_be_moved)
obj1.move_files()