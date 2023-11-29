# CCR4157

## Python requirements for UMAP

Notebook tested with Python version 3.9.18
The following packages are required

* ipykernel
* scikit-learn
* matplotlib
* seaborn
* statsmodels
* hdbscan
* umap-learn

The parsing script `gliph_data_parser.py` converts GLIPH2 output (the cluster.csv output file) into the correct input format for the UMAP notebook. The parser takes a second argument defined as the minimum number of samples you want represented in convergence groups, groups with fewer samples than the threshold will be filtered out by the parser. The threshold used in the publication was 10.  

The Python notebook has a set of cells in the end which output the significant clusters of convergence groups and their GLIPH2 information for further analysis. 

