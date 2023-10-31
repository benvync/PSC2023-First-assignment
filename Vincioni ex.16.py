#tran
Transitions = 0
Transversions = 0
from Bio import SeqIO
file_path = "rosalind_tran.txt"  
Sequences = list(SeqIO.parse(file_path, "fasta"))

if len(Sequences) == 2:
    
    Sequence1 = Sequences[0]
    Sequence2 = Sequences[1]

    Sequence_id1 = Sequence1.id
    sequence_id2 = Sequence2.id
    Sequence_data1 = str(Sequence1.seq)
    Sequence_data2 = str(Sequence2.seq)
    seq1=Sequence_data1
    seq2=Sequence_data2    
else:
    print("The file does not contain sequences")


if len(seq1) != len(seq2):
    raise ValueError("It is needed that sequences, to be compared, are of the same lenght.")
nucleotide_properties = {
    'A': 'purine',
    'G': 'purine',
    'C': 'pyrimidine',
    'T': 'pyrimidine',
    'U': 'pyrimidine'
}

for symbol1, symbol2 in zip(seq1, seq2):
    if nucleotide_properties[symbol1] == nucleotide_properties[symbol2]:
        if symbol1 != symbol2:
            Transitions += 1
    else:
        Transversions += 1


ratio = Transitions/Transversions
print(ratio)
