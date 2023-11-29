import sys, time

'''
First argument: GLIPH2_output_cluster.csv
Second argument: threshold for skipping convergence groups
                 with fewer than X samples (int)

Prints the output to STDOUT 
'''

infile = open(sys.argv[1], "r")
threshold_num_in_cluster = int(sys.argv[2])

#skipping header line
infile.readline()

all_clusters = list()
current_cluster = dict()

current_cluster["sample"] = list()
current_cluster["cdr3"] = list()
current_cluster["tcr_v"] = list()
current_cluster["tcr_j"] = list()
current_cluster["freq"] = list()

all_samples = set()

# Go through file and collect all relevant information in dictionaries 

for line in infile:
    # GLIPH2 files contain convergence groups delineated by an empty line
    # Using that empty line to save and reset the dictionary
    if line != "\n":
        ll = line.strip("\n").split(",") 

        index = ll[0]
        pattern = ll[1]
        fisher_score = ll[2]
        final_score = ll[5]
        cluster_type = ll[11]

        cdr3 = ll[12]
        tcr_v = ll[13]
        tcr_j = ll[14]

        sample_name = ll[16]
        freq = ll[17]

        all_samples.add(sample_name)

        # These are one per CDR3 sequence in the group
        current_cluster["sample"].append(sample_name)
        current_cluster["cdr3"].append(cdr3)
        current_cluster["tcr_v"].append(tcr_v)
        current_cluster["tcr_j"].append(tcr_j)
        current_cluster["freq"].append(freq)

        # These are one per convergence group
        current_cluster["index"] = index
        current_cluster["pattern"] = pattern
        current_cluster["fisher_score"] = fisher_score
        current_cluster["final_score"] = final_score
        current_cluster["cluster_type"] = cluster_type

    else:
        # New convergence group, initiate new dict entry
        all_clusters.append(current_cluster)
        current_cluster = dict()

        current_cluster["sample"] = list()
        current_cluster["cdr3"] = list()
        current_cluster["tcr_v"] = list()
        current_cluster["tcr_j"] = list()
        current_cluster["freq"] = list()

# Then create a better structured output
# Start with header string with properly sorted sample names

header_string = "cluster_index_pattern\tfisher_score\tfinal_score\tcluster_type"

for sample in sorted(all_samples):
    header_string += "\t" + sample

print(header_string)

for cluster in all_clusters:

    if len(set(cluster["sample"])) < threshold_num_in_cluster:
        continue # SKIPPING clusters with fewer than x samples 

    output_string = ""

    pattern = cluster["pattern"]
    fisher_score = cluster["fisher_score"]
    final_score = cluster["final_score"]
    cluster_type = cluster["cluster_type"]
    index = cluster["index"]

    output_string += f"{index}_{pattern}\t{fisher_score}\t{final_score}\t{cluster_type}"
   
    # Count the total clone count for each sample, ie count clonecount per sample
    sample_string_clone_freqs = ""
    for sample in sorted(all_samples):
        total_freq = 0 # If the sample isn't part of the group, count is 0
        for i in range(0,len(cluster["sample"])):
            if (sample == cluster["sample"][i]):
                # Add upp all the counts in this convergence group from the sample
                total_freq += int(float(cluster["freq"][i]))

        sample_string_clone_freqs += "\t" + str(total_freq)

    output_string += sample_string_clone_freqs
    print(output_string)
