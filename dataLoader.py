import random

# This file responsible for the reading of the files, splitting the data to train set, validation set, uploading the
# test set and setting the labels.

"This function extract concentration from a filename"
def extract_concentration(filename):
    return filename.split('_')[1].split('.')[0]


"This function create output labels based on the concentrations"
def set_labels(filename, lines):
    concentration = extract_concentration(filename)
    if 'pM' in concentration:
        concentration_num = 1
    else:
        concentration = concentration.split('nM')[0]
        if concentration == 'input':
            concentration_num = 0
        else:
            # Low concentration: <= 100
            # Medium concentration: 100 < x <= 500
            # High concentration: > 500
            number = int(concentration)
            if number <= 100:
                concentration_num = 1
            elif 100 < number <= 500:
                concentration_num = 2
            else:
                concentration_num = 3
    y = [concentration_num] * lines
    return y


"This function reads all the files of specific RBP and load from each file X sequences"
def importData(files):
    sequences = []
    output = []
    numOfLines = 100000
    for file in files:
        with open(file, 'r') as seq_file:
            counter = 0
            while counter < numOfLines:
                line = seq_file.readline().split('\t')[0]
                if 'N' in line:
                    continue
                else:
                    counter += 1
                    sequences.append(line)
        output.extend(set_labels(file, numOfLines))
    return sequences, output


"Splitting the data to test set and train set"
def splitData(sequences, output):
    data = list(zip(sequences, output))
    random.shuffle(data)
    # Calculate the number of data for training and validation
    train_proportion = 0.8
    num_data = len(data)
    num_train_data = int(train_proportion * num_data)
    # Split the data into training and validation sets
    training_set = data[:num_train_data]
    validation_set = data[num_train_data:]
    # Unzip the training and validation sets into separate lists
    training_sequences, training_outputs = zip(*training_set)
    validation_sequences, validation_outputs = zip(*validation_set)
    return training_sequences, training_outputs, validation_sequences, validation_outputs


"Uploading the test set"
def importRNAcompete(rnaCompeteFile):
    with open(rnaCompeteFile, 'r') as rnaCompete_seq:
        rnaCompeteSeq = rnaCompete_seq.read().splitlines()
        return rnaCompeteSeq
