#!/usr/bin/python

import sys
import re
import gzip
import operator
import subprocess
import os
import random

#FUNCTIONS

def read_netMHC_file(netMHC_file_sub,SB_WB_sub): 
   try:
      with open(netMHC_file_sub, 'r') as f: #We open the netMHC_file and read it
         for i in f: #start a loop for every line of the file 
             i= i.lstrip() #remove spaces to the left of each line 
             if re.match("[0-9]",i): #if the line starts with 0-9
                 all=[] #We define a list called all
                 all=i.split() #and this list is formed by the "words" forming the line separated by a whitespace
                 if float(all[12]) <= float(1.0):
                     j=str(all[9])
                     SB_WB_sub.append(j)
               
   except IOError:
      print(str(netMHC_file_sub)," does not exist")
      sys.exit()

   return(SB_WB_sub)

#MAIN

#Our program requires 3 arguments (arg0 is the name of the program)

if len(sys.argv) < 2:
    print("Usage", str(sys.argv[0]), " netMHC_prediction_dir output_file")
    sys.exit()

netMHC_pred_dir=sys.argv[1] 
output_file=sys.argv[2] 

#Read de netMHCpan outputs

SB_WB=[] #Create empty LIST
for netMHC_file in os.listdir(netMHC_pred_dir): #start looping over the files that are on the folder (directory, arg1)
   if netMHC_file.endswith(".out"): #if the files in that folder ends with .out
       (SB_WB)=read_netMHC_file(str(netMHC_pred_dir)+"/"+str(netMHC_file),SB_WB) 

#OUTFILE 

out_file=open(output_file,'w') 

for pep in SB_WB:
    out_file.write(str(pep)+"\n")

out_file.close()
