import os
from mod_for_files import file as mof


if __name__ == '__main__':
    parent_dir = os.path.dirname(os.path.dirname(os.getcwd()))
    mof.traverse_directory(parent_dir)
