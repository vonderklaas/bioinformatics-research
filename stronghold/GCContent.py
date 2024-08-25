# Read data from the file (FASTA formatted file)
def readFile(filePath):
    with open(filePath, 'r') as file:
        return [l.strip() for l in file.readlines()]
    
def gc_content(seq):
    """
    GC Content in a DNA/RNA sequence
    """
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

# Storing our data
FASTAFile = readFile('../test_data/gc_content.txt')
FASTADict = {}
FASTALabel = ''

# print(FASTAFile)

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] = line

# Format the data (store the data in a convinient way)
# Run needed operation on the data (pass to gc_content)
ResultDict = {
    key: gc_content(value) for (key, value) in FASTADict.items()
}
print(ResultDict)

# Collect results (Rosalind submission in our case)
MaxGCKey = max(ResultDict, key=ResultDict.get)

# >Rosalind_0808 -> 59.259259
print(f'{MaxGCKey[1:]}\n{ResultDict[MaxGCKey]}')