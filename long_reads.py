# accepts as input filename and quality cutoff score
import sys
from Bio import SeqIO

filename = sys.argv[1]
if (filename[-1] != 'a'):
    print("please enter a fasta file as the first argument.")
    sys.exit()
file_prefix = filename.split('.')[0]
output_file = file_prefix + '.trimmed.fasta'

read_threshold = int(sys.argv[2])
#    sys.exit() 

print("filename = ", filename, "read length = ", read_threshold)

print('')
handle = open(filename, "rU")
output = open(output_file, "w")
for record in SeqIO.parse(handle, "fasta"):
    print(record.id)
    
    if len(str(record.seq)) > read_threshold:
         output.write('>')
         output.write(record.id)
         output.write('\n')
         output.write(str(record.seq))
         output.write('\n')
    
handle.close()
output.close()
