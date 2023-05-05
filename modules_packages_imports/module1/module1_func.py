import os, sys
from os.path import abspath, join, dirname 

# Set the absolute path of this directory to the list of paths in sys.path
sys.path.insert(0, abspath(join(dirname(__file__),'..')))
print(sys.path)
from module2 import module2_func

def module1_process_1():
    print("This is module1 processing 1")

def module1_process_2():
    print("This is module1 processing 2")

def import_test():
    print("This is module 1 calling/n")
    module2_func.module2_process_1()

import_test()