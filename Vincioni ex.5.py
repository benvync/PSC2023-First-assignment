from Bio import SeqIO
def calculate_GC_content(sequence):
    GC_count = sum(base in 'GC' for base in sequence)
    total_length = len(sequence)
    GC_content = (GC_count / total_length) * 100
    return GC_content

def find_highest_GC_content(FASTA_file):
    records = SeqIO.parse(FASTA_file, "fasta") 
    highest_GC_id, highest_GC = max((record.id, calculate_GC_content(str(record.seq))) for record in records)
    return highest_GC_id, highest_GC
fasta_file = "rosalind_gc.txt"
highest_gc_id, highest_gc = find_highest_GC_content(fasta_file)
print(highest_gc_id, highest_gc)
