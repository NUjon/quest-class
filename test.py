from Bio import SeqIO

#handle = open("SRR062634_1.filt.fastq", "rU")
print('')
handle = open("exome.fastq", "rU")
for record in SeqIO.parse(handle, "fastq"):
    qual = record.format("qual")
    qual_list = qual.split()
    del qual_list[0]
    del qual_list[0]
    print(qual_list)
    longest_read, bp_length, start_idx, end_idx, best_start, best_end = 0, 0, 0, 0, 0, 0 

    for index, score in enumerate(qual_list):
        bp_length = bp_length + 1
        if int(score) < 30:
            if bp_length > longest_read:
                longest_read = bp_length 
       #         end_idx = index
       #         best_end = end_idx
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
    print("length of qual_list = ", len(qual_list))
#    print(record.seq)
    print('')
handle.close()
