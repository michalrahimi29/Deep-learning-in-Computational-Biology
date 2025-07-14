import random
import numpy as np

# This file includes the functions for preforming padding and the one-hot encoding function

"From a given set of sequences we find the longest sequence"
def maxLengthSequence(sequences):
    maxLength = 0
    # Search for the maximum sequence length in all RBNS and RNAcompete files.
    for line in sequences:
        length = len(line)
        if length > maxLength:
          maxLength = length
    return maxLength


"Finding the max length between test set and train set, in order to know how much to pad"
def maxlen(rnaCompeteSequences, sequences):
    maxLengthRNAcompete = maxLengthSequence(rnaCompeteSequences)
    maxLength = maxLengthSequence(sequences)
    if maxLengthRNAcompete > maxLength:
      maxLength = maxLengthRNAcompete
    return maxLength


"One-hot encoding of the RNA/DNA sequences"
def oneHot(string):
    trantab = str.maketrans('ACGTU', '01233')
    string = str(string)
    data = [int(x) for x in list(string.translate(trantab))]
    ret = np.eye(4)[data]
    return ret


"Creating the distribution of the nucleotides "
def calculate_padding(sequences, maxLength):
    nucleotides = 0
    Letters_occurences = [0, 0, 0, 0]
    for line in sequences:
        nucleotides += len(line)
        Letters_occurences[0] += line.count('A')
        Letters_occurences[1] += line.count('T')
        Letters_occurences[2] += line.count('G')
        Letters_occurences[3] += line.count('C')
    occurences = [x / float(nucleotides) for x in Letters_occurences]
    pad_sequences = []
    for seq in sequences:
        pad_sequences.append(Padding(occurences, seq, maxLength))
    return pad_sequences


"Padding each sequence with length < maxLength. Padding from both sides- half to the right and half to the left"
def Padding(occurences, sequence, maxLength):
    pad1 = random.choices(['A', 'T', 'G', 'C'], weights=occurences, k=int(np.floor((maxLength - len(sequence)) / 2)))
    pad2 = random.choices(['A', 'T', 'G', 'C'], weights=occurences, k=int(np.ceil((maxLength - len(sequence)) / 2)))
    padSequence1 = ''.join([str(elem) for elem in pad1])
    padSequence2 = ''.join([str(elem) for elem in pad2])
    return padSequence1 + sequence + padSequence2