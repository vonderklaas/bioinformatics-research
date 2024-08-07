from DNAToolkit import *
import random

rndDNAStr = ''.join([random.choice(Nucleotides) for _ in range(20)])

DNAStr = validateSeq(rndDNAStr)

print(countNucFrequency(DNAStr))