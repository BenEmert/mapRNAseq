from collections import defaultdict
import re

count_files = snakemake.input
outfile = snakemake.output[0]

count_dict = defaultdict(list)

for file in count_files:
    with open(file, 'r') as f_in:
        for line in f_in.readlines():
            line = line.rstrip().split('\t')
            count_dict[line[0]].append(line[1])

samples = [re.search('(?<=analyzed/)[\w]+', path).group() for path in count_files]

with open(outfile, 'w') as f_out:
    f_out.write('gene_name\t' + '\t'.join(samples))
    for gene in count_dict.keys():
        f_out.write('\n' + gene + '\t' + '\t'.join(count_dict[gene]))
