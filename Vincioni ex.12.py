#cons
import numpy as np
import pandas as pd
import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

DNA10_1 = ''
DNA10_2 = ''
DNA10_3 = ''
DNA10_4 = ''
DNA10_5 = ''
DNA10_6 = ''
DNA10_7 = ''
DNA10_8 =''
DNA10_9=''
DNA10_10=''

fasta_file = 'rosalind_cons.txt'
with open(fasta_file, "r") as file:
    records = list(SeqIO.parse(file, "fasta"))
    if len(records) < 10: #sufficiency condition
        print("The file has no enough sequences for the needed variables.")
    else:
        DNA10_1 = str(records[0].seq)
        DNA10_2 = str(records[1].seq)
        DNA10_3 = str(records[2].seq) 
        DNA10_4 = str(records[3].seq) 
        DNA10_5 = str(records[4].seq) 
        DNA10_6 = str(records[5].seq) 
        DNA10_7 = str(records[6].seq) 
        DNA10_8 = str(records[7].seq) 
        DNA10_9= str(records[8].seq) 
        DNA10_10 = str(records[9].seq) 

DNA_sequences = [DNA10_1, DNA10_2, DNA10_3, DNA10_4, DNA10_5, DNA10_6, DNA10_7,DNA10_8,DNA10_9,DNA10_10]

length = len(DNA10_1)
pos = 0

A_Row = [0] * length
C_Row = [0] * length
G_Row = [0] * length
T_Row = [0] * length

while (pos < length):
    for sequence in DNA_sequences:
        base = sequence[pos]
        if (base == "A"):
            A_Row[pos] = A_Row[pos] + 1
        elif (base =="C"):
            C_Row[pos] = C_Row[pos] + 1
        elif (base =="G"):
            G_Row[pos] = G_Row[pos] + 1
        elif (base =="T"):
            T_Row[pos] = T_Row[pos] + 1
        else:
            print("error1")
    pos = pos + 1

consensus = Seq("")
aCount = 0
cCount = 0
gCount = 0
tCount = 0
maxCount = 0

pos = 0

while (pos < length):
    aCount = A_Row[pos]
    cCount = C_Row[pos]
    gCount = G_Row[pos]
    tCount = T_Row[pos]
    maxCount = max([aCount,cCount,gCount,tCount])
    
    if (maxCount == aCount):
        consensus = consensus + "A"
    elif (maxCount == cCount):
        consensus = consensus + "C"
    elif (maxCount == gCount):
        consensus = consensus + "G"
    elif (maxCount == tCount):
        consensus = consensus + "T"
    else:
        print("error2")
    
    pos = pos + 1
    
print (consensus)
print("A: " + ' '.join(map(str,A_Row)))
print("C: " +' '.join(map(str,C_Row)))
print("G: " +' '.join(map(str,G_Row)))
print("T: " +' '.join(map(str,T_Row)))

print("\n---\n")


