# CCR4157

TCR sequencing data from the CCR4157 study

This repository includes code used in the paper "T-cell receptor determinants of response to chemoradiation in locallyadvanced HPV16-driven malignancies" published in Frontiers in Oncology (Front. Oncol. 13:1296948.
doi: 10.3389/fonc.2023.1296948)

## UMAP from GLIPH2 results

### Python requirements for UMAP

Notebook tested with Python version 3.9.18
The following packages are required

* ipykernel
* scikit-learn
* matplotlib
* seaborn
* statsmodels
* hdbscan
* umap-learn

### How to run

#### parsing script `gliph_data_parser.py` 
This script converts GLIPH2 output (the cluster.csv output file) into the correct input format for the UMAP notebook. The parser takes a second argument defined as the minimum number of samples you want represented in convergence groups, groups with fewer samples than the threshold will be filtered out by the parser. The threshold used in the publication was 10.

#### UMAP python notebook

The parsed GLIHP2 data needs to be set in the notebook.

The Python notebook has a set of cells in the end which output the significant clusters of convergence groups and their GLIPH2 information for further analysis. 

## ERGO from the GLIPH2 UMAP results

This part includes 6 scripts with different steps of how to run ERGO based on the significant UMAP clusters

### How to run


#### Script 1 (bash script): run netmMHCpan4.1.

The netMHCpan4.1. should be downloaded and installed following instructions from https://services.healthtech.dtu.dk/services/NetMHCpan-4.1/

The following information should be filled by the user: 

root_dir= root directory. 

protein_file= directory of the HPV16 E2, E5, E6 and E7 txt files (can be downloaded from this page). 

hla_file= directory of the individual HLA type (txt file) for each patient (can be downloaded from this page).

out_dir= output directory. 

#### Script 2 (python script):  copy

This script copies the output from netMHCpan4.1. files (predictions for each HPV oncoprotein) into an inidividual patient-based file in another folder. 

#### Script 3 (python script): generate table

This script generates a table from the copied netMHCpan4.1. predictions to select those epitopes with an Elution Rank <1. 

#### Script 4 (python script): extract CDR3

This script extracts the CDR3 amino acid sequence from the GLIPH2 UMAP output. 

#### Script 5 (python script): ERGO generate table

This script generates a table from the extracted CDR3 and the predicted immunogenic epitopes. 

#### Script 6(bash script): Run ERGO

This script runs ERGO. It requires some information to be filled by the user: 

root_dir= root directory

ERGO_input_dir= this is the output directoru from the previous script (ERGO generate table)

out_dir= output directory. 

In addition, requires to download and install the ERGO scripts (https://github.com/IdoSpringer/ERGO-II)
