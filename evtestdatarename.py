#!/usr/bin/python

'''
Utility to rename files for EyeVerify Test Data for straight gaze.
Checking this in to Github because I use this fairly often from multiple machines.
'''

import os
import subprocess
import os.path
import sys

def renameFiles(dir_name):
    for filename in os.listdir(dir_name):
        #print "Dir_name: " + dir_name + " Filename: " + filename
        beg_index = -1
        try:
            beg_index = filename.index("_C")
            newFilename = filename[0:beg_index+2] + ".png"
            if os.path.isfile(newFilename):
                print "Destination file: " + newFilename + " already exists. Overwriting!!!"
            os.rename(dir_name + "/" + filename, dir_name + "/" + newFilename)
            print "Renamed file: Original: " + filename + " new: " + newFilename
        except ValueError:
            print "Bad indexes for filename: " + filename + " : beg_index=" + str(beg_index)

def nameFilesInAllSubdirs(dir_name):
    renameFiles(dir_name)
    for root, dirs, files in os.walk(dir_name):
        print "Renaming files in directory: " + root
        for dir in dirs:
            renameFiles(root+dir)

def main():
    proj_dir = ""
    if len(sys.argv) > 1:
        proj_dir = str(sys.argv[1])
    else:
        proj_dir = '.'
    nameFilesInAllSubdirs(proj_dir)

if __name__ == "__main__":
    main()
