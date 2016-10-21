# accepts as input filename and quality cutoff score
import sys
from Bio import SeqIO

filename = sys.argv[1]
if (filename[-1] != 'a'):
    print("please enter a fasta file as the first argument.")
    sys.exit()

file_prefix = filename.split('.')[0]
output_file = file_prefix + '.report'

print('')
handle = open(filename, "rU")
output = open(output_file, "w")
counter = 0
running_total = 0

for record in SeqIO.parse(handle, "fasta"):
    running_total = running_total + len(str(record.seq))
    counter = counter + 1

output.write("The average read length in ")
output.write(filename)
output.write(" is ")
output.write(str(running_total/counter))
output.write('\n')
    
handle.close()
output.close()
