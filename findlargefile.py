# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 18:29:05 2018

@author: markp
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def search_folder(location, min_filesize):
    for foldername, subfolders, filenames in os.walk(location):
        for filename in filenames:
            try:
                size_bytes = os.path.getsize(os.path.join(foldername, filename))
                if min_filesize * 1024 ** 2 <= size_bytes:
                    yield filename, size_bytes
            except FileNotFoundError:
                print("an error")
                # maybe log error, maybe `pass`, maybe raise an exception
                # (halting further processing), maybe return an error object

filesize = 30
location = r'D:\GDrive\water\RioGrande_MakeData_Mark'

if __name__ == '__main__':
    print('This program searches for ...')
    print('Files larger than %d MB in location: %s' % (filesize, location))
    for filename, size in search_folder(location, filesize):
        print(filename)