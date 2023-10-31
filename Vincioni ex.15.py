def find_longest_common_substring(DNA_strings): #FIRST the longest and then iterates through the string
    reference = DNA_strings[0]
    longest_common_substring = ""
    for i in range(len(reference)):
        for j in range(i + len(longest_common_substring) + 1, len(reference) + 1):
            substring = reference[i:j]
            is_common_substring = all(substring in dna_string for dna_string in DNA_strings[1:])
            if is_common_substring and len(substring) > len(longest_common_substring):
                longest_common_substring = substring

    return longest_common_substring

DNA_strings = []
with open("rosalind_lcsm.txt", "r") as file: #INPUT file
    DNA_string = ""
    for line in file:
        if line.startswith(">"):
            if DNA_string:
                DNA_strings.append(DNA_string)
            DNA_string = ""
        else:
            DNA_string += line.strip()
    if DNA_string:
        DNA_strings.append(DNA_string)
result = find_longest_common_substring(DNA_strings)
print( result)  #longest common substring