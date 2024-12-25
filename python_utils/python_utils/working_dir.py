"""
This file contains a helper function to assist when
needing to execute code (such as reading in a file) in
a specific directory. 
"""

from contextlib import contextmanager
import os

@contextmanager
def working_dir(path):
    cur_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cur_dir)
