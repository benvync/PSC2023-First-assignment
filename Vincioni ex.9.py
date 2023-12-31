def translate_rna_to_protein(rna_sequence, codon_table):
    protein_sequence = ""
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        amino_acid = codon_table.get(codon, None)
        if amino_acid == "Stop": #codon recognized for the end of translation
            break  
        protein_sequence += amino_acid if amino_acid else "X"
    return protein_sequence

RNA_sequence = 'AUGAAGGCCGAGGGAAUCCUAUGGUUUAAGCCUUGCACUCGGAGUGAAUCCAUAGUCGGGGCACGGGUAAAGUCGGUAUUUGCCUGGAUUCGAUUUACCCAUAACCUCAUACCCUUGGGACGGUCGACGGUCCUGCGUUGGUUCCUCUUGGUUCGAAUACGAGGUGGUUCAGGAGCGCUAGCAACCAAAUUACAUAACGUACCAAUAUCUUUCUUCUGCGAGGACCACCGGGAGAACUGCGUAAGGCAGGGCACGCUGGUGGGGAUCUACAGGUCCAACAUCCCUGGCCGUGCGUGCGGGGUCAGGCAGUUCCUGAUACCGAGACUGCUUCCGGGCUUUGCGCGGAGCCCUUGCCGAAGGAGGGAACGAGCAUAUUUCACCGUGGUUCCCACUUUACCGAAAGAUGAUAGAGAACAAGUUAAACCGAACGCAGACAAAAGUGGCCACGUACGUGGUACUCACCGAGGUUAUAAAAGGAGCUCGCACAUACAUAGCGAAGUCGAGAGUGCAGCCUUCUCACGUCCCUGGCUCUAUAACGGCAUAGGGCGAUGCCUGUUCUCCGCUGUGACGGGGGUGGAGUCCUUGAUAUCAGCACGACUCGAGUUUACAUGUAAUGGGACCCCGAUGAGGGAGUGGUCUGACAACGCCGUUCAUUCUCAUGAGUGCUCGACGCCACCAUCAUGUCACGCUGAGCCGAAGAACUGCCGCCAUCUUAGGCUGUACCAAAGGCUCCUUCCUCUGGCAGCCUUCGUCGUGAAAACGUGUUACAUGCUCUGCCCUCACAGACUUAUGCCGCGAUCCCAACCCGGUAUAAUCCACUUACCUGCCCCUAGAGACGUGAAGGGAGGUACACCGCUUGACGCAACUCUGACCCCAGGUUCUGGUGCACCUAACCAUGAUAGCCUGGCAGUAUCGGAUGCUGCCGUUCACGGAUUUGUUCUGAAAAAGUUCUCCCAGUCCACAGCAUCGCGAGCGCGUCGCGUCUUGAUUCCCGAGGCCGGCCGUAUAGGACAAGGGCCCCACUCAGCCGAGAAAGAAAGCUCGGCGCCGUGUGUUUUCCGUGAAUAUUGCGCCCGCAUUGGUUCAACAUGGUGUGUACCGUGUCGCCAAUUCUAUACGCUACAUCGCCUACCAGUUACUUUGUACUCUCAACAGCACCCGAAAUUUACUCAAUACACUCGUCGGCGGUGUGUCUGGGGCCCGUCCGUUCAUAGUGGGUCUUCGGCGUGCAGUCAGAGAAAUAAUAUGGGCGCUUACAUGAUAAGACUGAGGGGAUCCUGCGUAAUCUCGACUUCCGUAGGGCGAGCUCUAGUACGACACCGCGAGCCCAACGACAUUGAUGCGUCAGUAAGCGAGUCUCGUGUACUCUGCAAUUACAUACCAGUGAGAAGUCCGGAGAAUUGUAUGAGGGCGCUCGAGUCCGUUUGCAGCAUUGCAAGUUUACCAGAGUAUUUUCUCUGGGCAUGGUACUCCAGACCACCAUUGUUCGUUGUCGACCUGCUCUUGGUAGACCGGGGUGACGAUAACGGGUUAGCGCUCCUAGUACUAGAGAUGACAUAUAAACACGACUCAACUGGGCCCUGUGAAUCUAAGGUGAAACUCGGAAACAACACUCAUUCGGAGCGUUGCGUUAAAAGUUUCGGCCACGUGAUCACUAUUGGGUUGGAUUCACAAGCUACCUAUGAUGUACCGAGCGGGUUCCCUCGAACGGCAACCUAUAGCUCACGGAUGGCGGUAGCUCUAACCGUGGACGGUACGGAUAAGAAUAUUGUUUUUGGGCUGCCUCUUAGUGCUGGUCCUGAUCCGUUGGAAGGACGACUUCUGGUUACUGAGCCCACUCCACCCUCAUGCUCAUUCCUCAACAGCGGGUUCGCCGCAAGUCUCAAGUGUACGCUCCCGAGAUUUGAUUCGUCCGCGUUAGGACGAAAGUUCGUGACCAAGCUUAAUCGGCAUCCAGUGCAGGCGGGUAUAACUGGUUCGGCAUCACGGUCCAAAAAGGGUGCAUACUCGGCGGCAGGAUACCGGUGUCUAGCCGGUCGCCGUUGGGACACAAUCGGACCUGCACCACGCGUGUCCCGGAUGUAUAUGAACGCGAGCAAGAUUUUAGACACCCAACUUGAUUUAAGCAUGCCAAGACUGACCCUUCUUAUCACGACUCCGUCCGCAAGUAUGCUUCCAACUGACGUCUAUAAUCUACUGAUGGGUCAUUUCCGAAUAUACGACUCGAUACAAAAAAUAACGGAGUUAUACAUAAAUGUCUUUGUGUCGAAAAUGACCAGCGUGCCCAAAUCCUACACAAGGAGACGUGUUAAUACGCGCCCGUUAAAGCGCCACGAUUUAGGGCGAUGUGGGCUCAGCCUUGCCAAGCCUAUGCCAUUUAUAUCGAGGACCUCUCUGUCUCUUGAUAAAUCUUCCCAGUUGGUUGGGGCAAUUGGUCCGCAAAUAGAAGCUUGCCGUCCACAUCGAAUGACGGUGGAGUAUGCCGUGUUCACGCUCUCUGCAUCCCCCUAUUCUAGAUGGGUGGAGCGCUAUCAUCUCGGGCCAUGCCCUCGAGCUCCUCCCCGGUCAGAAUUGAUGUUCAAGACCCCCAACGGGAAGCACUUGGUUGUAGACCAGGAGGAUCCUAUACUCAAAAGGGUGGGCAUAAGAACCAGGUUAAUUCUGGUAGAUUUACAGGAUAAUGCUCUACAGCUGGAAUCUCAAGCGCGCGGAGUUGAGUUAUCCCUGCGUUGCAGAACCAUGAUAAGAAUAGUCAAUCCUCCCAUAGGAACAUUGUUAGAAUCUACUAGGGCGGGUUCUUCUAGCACCCAUAAUCUGGGCAGCGAAGUACCGUCUCUUAGGAAAGUGACAGCG'
#codon table as reference to translate the sequence in protein
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
#actual translation
protein_sequence = translate_rna_to_protein(RNA_sequence, codon_table)
print(protein_sequence)
