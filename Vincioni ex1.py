DNA_sequence= 'CCGTTGCTAACTCAGCATACCCACCAGCGAGACCCCAGCGAAGCGCCAGGGTAAGATGCCTTCGTATGTATCCGACGCCGCGTGCCGGCCCACCTCGAGCTCGGCATCGCGAGCGCCAGTACCAGGCGTCAGCAACCGGCATAGTAGGTTTTAGAATATTGTGCGGGGTTCCTAACTCGTAATTTGTTTGTCTTCTTGCACATAGGTTCCAAGAATTAATTAGTTACGGACTTGCCGGTATTGTAGACACCAGGGATTTGGGGAACGAGACCCCGCTAACAGGTCTATCGATGCTTTCCTCAAAGATTTCCTGTAGGGGAAATTTCTCGACAGATCGGCCGGCGCTTAGGTTAGTCCTTAGTTTTAATCCTTTATGACCCGGGTAGCAAGCAGATTTCACCGCCGTGATAAGAGGCCCGGGTACGCAAATAAGCTGCTGGAGATTGCGCCTTCATTTAGAGCGAGAGTAAGTGGTCCTCAGGGCTTGATTTTCATCACATGTGGAAATCTCTGGACAACTATGCACTCAGAACGCTACGGGTCAAAATAGAATTGCTTTAACTGGGCCAGCGGCAGACATTCTTATGTTACAGACGTAAACTGTAGAGAGCGAGGAACCTCGCATCACTAGGTTTCGGGGAAGACTCGTGGCCGCGAATTGATTTGCCATGACTACCGCCTCATAACGTATCATCATCGAATCTAACAAGCGATTGGACGCGCGAACAGTAAAACTATTCCGTGAGGGCAAAGCGTAACTGTTCAAGATGGGCTTTTATTGTTTGGATGACCGAATTGAATATGTGAACAGTAAACACGTCACCGTGCAGGAGCTATCCTCGGGAGGGCTCTTGACTAATGTGCCTAAAGCAGATTAAGACTCTACGGCATCTGGCGTATTCTTTTGATTAAGCCGTGAGACTTTGAATTGTCTCGCCCAGCCG'
numberA=0 
numberC=0
numberG=0
numberT=0
for symbol in DNA_sequence: 
    if symbol == 'A': 
        numberA= numberA+1 
    elif symbol == 'C': 
        numberC= numberC+1
    elif symbol == 'G': 
        numberG= numberG+1 
    else: 
        numberT= numberT+1     
print (numberA, numberC, numberG, numberT)