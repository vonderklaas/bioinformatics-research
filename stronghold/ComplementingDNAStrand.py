DNA_ReverseComplement = {"A": "T", "T": "A", "G": "C", "C": "G"}

def reverse_complement(seq):
    """
    Swapping A with T and G with C.
    Reversing newly generated string.
    """
    complement_list = []
    for nuc in seq:
        complement_list.append(DNA_ReverseComplement[nuc])
    complement_string = ''.join(complement_list)
    return complement_string[::-1]


print(reverse_complement("ATGTCTGAGGACTAGTGCCATTCTTAATCAGGTAACGTTGTTATCCATGGGTAAAACCTTTGGAGGGTGTAACTCGGGTTCGCGTAGATGACACGGAAGGGAGTTAGGATTTAGCCACCTCTAAAAACAGGAGTAGCACGCACTGCACTCTGCACGACAGTGCTCTAGCGAATCTCGTGTATTCTGATAATCGGGTTCCGGGGCAGAGAGTGCCTCGATTAACGTTCCGATATGTATGCGCATCCCCTGAAATTTTCCCCTTAGTAAGAAACTAAGGGCGATGGACACCAGTACGGTACGCAGCTACGCGTCTGACATAAGGACACGTTCTTAACCCGCCATCTGGGTAGTATAGATGATATTCGACAACTATGTTGTGAGAGAAGAACATGGTAGCTGAATTCGAGGGACCGACTGGGTCCAAAACAGCTCCATCCACCCTACTATTGACCTGCAGTAGAATAACACTTATGCCCGCGGGATGTATTGGAGCGTTCAGAGTATCTGCGTTCAGTATGCTAACATTTCTCATTCGGGAACCTTATTGTCATCGCGGTCATCTTCGAAGGAACATTTACAGAACAGCTGACCATTAGCCAGTAACGACGCCGCGTTTCAGTCCCGGAACGGTTAGACATGATACCATAAGCCGTCTATACAAGAACGGGCTGTTGGCGGCGTAGATAGAAATATTAGTACATTCGAGCATTCCAGTAGATGCGAATGAGTCGGTCCCAAGGGCTTCTGTATTTGATTAGAAGAAGTTAATCGGCGCTTCGTCGGTGGCTACGACTAGTTGGAATCGCCAACACTTCGGCATGCCGTCGTTAAGGCAATTTATAAAGATCTGTAGGAGCGTCGATAATAAAGTCACCCTTTGATCCGTCTTGCGCACTCAGCTTCTTAGATGTATTTGTGACTACC"))