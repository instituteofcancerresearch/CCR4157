#!/usr/bin/python

import sys
import re
import gzip
import operator
import subprocess
import os
import random

#FUNCTIONS

def read_input_file(input_file_sub,CDR3_patient_sub,patient_sub): 
   try:
      with open(input_file_sub, 'r') as f: #We open the netMHC_file and read it
         for i in f: #start a loop for every line of the file 
             i= i.lstrip() #remove spaces to the left of each line 
             if re.match("[0-9]",i): #if the line starts with 0-9
                 all=[] #We define a list called all
                 all=i.split(',') #and this list is formed by the "words" forming the line separated by a coma
                 my_string=str(all[16])
                 patient_sub.append(str(my_string.split('_')[0]))
                 CDR3_patient_sub[str(all[12])]=str(my_string.split('_')[0])

   except IOError:
      print(str(input_file_sub)," does not exist")
      sys.exit()

   return(CDR3_patient_sub,patient_sub)

#MAIN

#Our program requires 3 arguments (arg0 is the name of the program)

if len(sys.argv) < 2:
    print("Usage", str(sys.argv[0]), " input_file ")
    sys.exit()

input_file=sys.argv[1] 

#Open and read the input: 

CDR3_patient={}
patient=[]
(CDR3_patient,patient)=read_input_file(str(input_file),CDR3_patient,patient) 

#Append the output_file ("_CDR3.txt") for each individual patient

append_txt="_CDR3.txt"
file_list=[p + append_txt for p in patient]
#remove duplicates
file_list = list (dict.fromkeys(file_list))

#OUTFILE 

for file in file_list: 
    with open(file,'w') as fo:
        for key, value in CDR3_patient.items():
            if str(value) == str(file.split('_')[0]):
                fo.write(str(key)+"\n")
            
