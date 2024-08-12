from DNAToolkit import *
from utilities import colored
import random

rndDNAStr = ''.join([random.choice(Nucleotides) for _ in range(50)])

DNAStr = validateSeq(rndDNAStr)

print(f'Sequence: {colored(DNAStr)}\n')

print(f'Length: {len(DNAStr)}\n')

print(colored(f'Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print(f'DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"DNA String + Complement + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr)[::-1])} 5' [Complement]\n")
print(f"5' {colored(reverse_complement(DNAStr)[::-1])} 3' [Reverse Complement]\n")
print(f'GC Content: {gc_content(DNAStr)}%\n')
print(f'GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')