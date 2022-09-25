from datetime import datetime
import os, sys, shutil, easygui
from time import strftime
from unittest.util import strclass
from os.path import isfile,isdir, join
from os import path
 
timestamp = strftime("%y.%m.%d.%H.%M.%S")
print(timestamp)
#Win
#source_dir = 'C:/Users/Joe/OneDrive/.1. Joe/.0. Personal/.2. USB Project/Test1'
source_dir = easygui.diropenbox()
dest_dir = easygui.diropenbox()
dest_dir2 = dest_dir+'/'+'USBArchive-'+timestamp

#Mac
# source_dir = '/Users/nadav/Desktop/Uni/Private/USB_project/Test1/'
# dest_dir = '/Volumes/NadavUSB'

option = None
try:
    if len(os.listdir(source_dir)) != 0:
        print("folder 1 entered")
        os.chdir(source_dir)
        # f=open('testingFile1.txt','w+')
        # f.write('this is a test doc 1')

        #Files inside directory
        #USB files
        DestFiles = [f for f in os.listdir(dest_dir) if isfile(join(dest_dir, f))]
        #PC files
        SourceFiles = [f for f in os.listdir(source_dir) if isfile(join(source_dir, f))]

        #Directories inside directory
        DestDirs = [f for f in os.listdir(dest_dir) if isdir(join(dest_dir, f))]
        SourceDirs = [f for f in os.listdir(source_dir) if isdir(join(source_dir, f))]

        #print("Source >>" , len(DestFiles),DestFiles)
        #print("Dest >>" ,len(SourceFiles),SourceFiles)

        i=0
        for x in range(0,(len(SourceFiles))):
            print(SourceFiles[i]) 
            i+=1

        for position, dir in enumerate(SourceDirs):
            # print(path.exists(file)) #checking if file is there or not
            if path.exists(dir):
                dir_sr = SourceDirs[position]
                shutil.copytree(dir_sr, dest_dir2)
                
        for position, file in enumerate(SourceFiles):
            # print(path.exists(file)) #checking if file is there or not
            if path.exists(file):
                file_sr = SourceFiles[position]
                #copy2 used as it takes datetime metadata
                shutil.copy2(file_sr, dest_dir2) 

    else:
        print("current directory not found")
except Exception as E:
    print(E)

