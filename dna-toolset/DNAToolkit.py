from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(seq):
    """
    DNA -> RNA Transcription.
    Replaces T with Uracil
    """
    return seq.replace("T", "U")

def reverse_complement(seq):
    """
    Swapping A with T and G with C.
    Reversing newly generated string.
    """
    # complement_list = []
    # for nuc in seq:
    #     complement_list.append(DNA_ReverseComplement[nuc])
    # complement_string = ''.join(complement_list)
    # return complement_string[::-1]
    
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subsec(seq, k=20):
    """
    GC Content in DNA/RNA sub-sequence length k (20 by default)
    """
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res