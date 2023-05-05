import os ,sys
from os.path import abspath, join, dirname


# Set the absolute path of this directory to the list of paths in sys.path
sys.path.insert(0, abspath(join(dirname(__file__),'..')))
from module1 import module1_func

def module2_process_1():
    print("This is module2 processing 1")


def module2_process_2():
    print("This is module2 processing 2")

def import_test():
    print("This is module2 calling")
    module1_func.module1_process_1()