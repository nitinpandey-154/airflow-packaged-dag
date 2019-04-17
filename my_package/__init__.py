import os

def list_files():
    print os.listdir(os.path.dirname(os.path.realpath(__file__)))


