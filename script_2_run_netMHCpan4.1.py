#!/bin/bash

#Before running the code the root directory, the HPV sequence, the HLA file and the patient ID folder have to be completed/created. 

root_dir=*YOUR ROOT DIRECTORY*

protein_file=$root_dir/INPUT/*HPV_SEQUENCE*

hla_file=$root_dir/INPUT/*PATIENT HLA FILE*

out_dir=$root_dir/OUTPUT/PEPTIDE_PREDICTIONS/*PATIENT_ID*/predictions


if [[ -f "$hla_file" ]];then
	while read p; do
	out_file=$out_dir/E*.netMHCpan4_1.${p}.out
	if [[ -f ${out_file} ]];then
	continue
	else
	netMHCpan-4.1/netMHCpan -BA $protein_file -a $p -s > $out_file
	fi
	done <$hla_file
fi

