#!/bin/bash

root_dir=**

ERGO_input_dir=$root_dir/**

out_dir=$root_dir/OUTPUT/ERGO_output/**

if [[ -d "$ERGO_input_dir" ]];then
	for ERGO_file in $ERGO_input_dir/*.csv;do
		filename=$(echo "$ERGO_file" | sed -e 's/\.csv$//' -e 's/.*\_//');			
		out_file=$out_dir/${filename}.ERGO_RESULTS.txt;
		if [[ -f ${out_file} ]];then
			continue
		else
			printf "python ERGO.py predict ae vdjdb specific cpu --model_file=./models/ae_vdjdb1.pt --train_data_file=./TCR_Autoencoder/tcr_autoencoder.pt --test_data_file=$ERGO_file > $out_file""\n"   
			python ERGO.py predict ae vdjdb specific cpu --model_file=./models/ae_vdjdb1.pt --train_data_file=./TCR_Autoencoder/tcr_autoencoder.pt --test_data_file=$ERGO_file > $out_file
		fi
	done 
fi
