Nucleotides = ["A", "C", "G", "T"]

# Check the sequence to make sure it is a valid DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

# Count the frequency of DNA nucleotides in the sequence
def countNucFrequency(seq):
    # import collections
    # return dict(collections.Counter(seq))
    tmpFreqDict = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict