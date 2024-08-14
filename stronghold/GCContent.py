# Read data from the file (FASTA formatted file)
def readFile(filePath):
    with open(filePath, 'r') as file:
        return [l.strip() for l in file.readlines()]
    
def gc_content(seq):
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

# Clean & prepare data (format using gc_content func)
# Format the data (store the data in a convinient way)
# Run needed operation on the data (pass to gc_content)
# Collect results (Rosalind submission in our case)
