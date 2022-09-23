#!/usr/bin/env python
import os, shutil
from os.path import isfile, join
from os import path
 
source_dir = '/Users/nadav/Desktop/Uni/Private/USB_project/Test1/'
dest_dir = '/Volumes/NadavUSB'

option = None
try:
    if len(os.listdir(source_dir)) != 0:
        print("folder 1 entered")
        os.chdir(source_dir)
        # f=open('testingFile1.txt','w+')
        # f.write('this is a test doc 1')
         
        #USB files
        DestFiles = [f for f in os.listdir(dest_dir) if isfile(join(dest_dir, f))]

        #PC files
        SourceFiles = [f for f in os.listdir(source_dir) if isfile(join(source_dir, f))]

        print("Source >>" , len(DestFiles),DestFiles)
        print("Dest >>" ,len(SourceFiles),SourceFiles)

        for position, file in enumerate(SourceFiles):
            # print(path.exists(file)) #checking if file is there or not
            if path.exists(file):
                file_sr = SourceFiles[position]
                shutil.copy(file_sr, dest_dir) 

    else:
        print("current directory not found")
except Exception as E:
    print(E)


#hello joe
