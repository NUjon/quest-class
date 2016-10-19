# accepts as input filename and quality cutoff score
import sys
from Bio import SeqIO

filename = sys.argv[1]
if (filename[-1] != 'q'):
    print("please enter a fastq file as the first argument.")
    sys.exit()
file_prefix = filename.split('.')[0]
output_file = file_prefix + '.fasta'

quality_level = int(sys.argv[2])
if  quality_level > 60:
    print("please enter a quality level as the second argument between 1 - 60.")
    sys.exit() 

print("filename = ", filename, "quality level = ", quality_level)

print('')
handle = open(filename, "rU")
output = open(output_file, "w")
for record in SeqIO.parse(handle, "fastq"):
    qual = record.format("qual")
    qual_list = qual.split()
    del qual_list[0]
    del qual_list[0]
#    print(qual_list)
    longest_read, bp_length, start_idx, end_idx, best_start, best_end = 0, 0, 0, 0, 0, 0 

    for index, score in enumerate(qual_list):
        bp_length = bp_length + 1
        if int(score) < quality_level:
            if bp_length > longest_read:
                longest_read = bp_length 
                best_end = index
                best_start = start_idx
            start_idx = index+1
            bp_length = 0
    if bp_length > longest_read:
        longest_read = bp_length
        best_end = index
        best_start = start_idx
    print('the longest read for this record is', longest_read)
    print('it starts at', best_start, ' and ends at ', best_end)

    output.write(record.id)
    output.write('\n')
    output.write(str(record.seq[best_start:best_end]))
    output.write('\n')
    
    print("length of qual_list = ", len(qual_list))
    
    print('')
handle.close()
output.close()
