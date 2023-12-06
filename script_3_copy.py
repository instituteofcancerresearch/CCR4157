#!usr/bin/python

import sys
import operator
import subprocess
import os
import csv
import shutil

#Our program requires 3 arguments (arg0 is the name of the program)

if len(sys.argv) < 3:
    print("Usage", str(sys.argv[0]), " folder_path out_file")
    sys.exit()

folder_path=sys.argv[1] #1st argument is the directory of the netMHC predictions
out_file=sys.argv[2] #2nd argument is the output file

with open(out_file,'w') as fo:
    for f in os.scandir(folder_path):
        if os.DirEntry.is_file(f) and 'netMHCpan' in f.name:
            current_file=open(f,'r')
            for line in current_file: 
                fo.write(line)
            current_file.close()
fo.close()

