from DNAToolkit import *
from utilities import colored
import random

rndDNAStr = ''.join([random.choice(Nucleotides) for _ in range(50)])

DNAStr = validateSeq(rndDNAStr)

print(f'Sequence: {colored(DNAStr)}\n')

print(f'Length: {len(DNAStr)}\n')

print(colored(f'Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print(f'DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")
