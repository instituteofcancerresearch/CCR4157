#!/usr/bin/python


import sys
import re
import gzip
import operator
import subprocess
import os
import random


#FUNCTIONS

def read_epitope_file(epitope_file_sub): 
    peptides_sub=[]
    try:
        with open(epitope_file_sub, 'r') as f:
            for i in f:
                i=i.rstrip()
                peptides_sub.append(i)

    except IOError: 
        print(str(epitope_file_sub), " does not exist")
        sys.exit()

    return(peptides_sub) 

def read_CDR3_file(CDR3_file_sub):
    CDR3_list_sub=[]
    try: 
        with open(CDR3_file_sub,'r') as f:
            for i in f:
                i=i.rstrip()
                CDR3_list_sub.append(i)

    except IOError: 
        print(str(CDR3_file_sub)," does not exist")
        sys.exit()

    return(CDR3_list_sub)

#MAIN

#Our program requires 3 arguments (arg0 is the name of the program)

if len(sys.argv) <4:
   print("Usage", str(sys.argv[0]), " CDR3_file epitope_file output_file")
   sys.exit()

CDR3_file=sys.argv[1]  
epitope_file=sys.argv[2] 
output_file=sys.argv[3]

(CDR3_list)=read_CDR3_file(CDR3_file)

(peptides)=read_epitope_file(epitope_file)

out_file=open(output_file,'w') #We generate an output file in writting mode.
for i in range(0, len(CDR3_list)):
    for j in range(0,len(peptides)):
        out_file.write(str(CDR3_list[i])+","+str(peptides[j])+"\n")

out_file.close()
