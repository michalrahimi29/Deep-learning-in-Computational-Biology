import sys
from dataLoader import *
from Helper import *
import numpy as np
from Model import *
from keras.utils import to_categorical


# This function takes the prediction for each probe in RNAcompete and print to the output file
def evaluate(file_path, prediction_list):
    prediction = [lst[3] + lst[2] + lst[1] - lst[0] for lst in prediction_list]  ## This is the aggregation function-
    # from distribution to RNA binding intensity
    file = open(file_path, 'w')
    for item in prediction:
        file.write(str(item) + "\n")
    file.close()


if __name__ == '__main__':
    outputFile = sys.argv[1]
    RNAcompete_file = sys.argv[2]
    training_files = sys.argv[3:]

    # loading data and splitting to train and validation
    sequences, output = importData(training_files)
    training_sequences, training_outputs, validation_sequences, validation_outputs = splitData(sequences, output)
    rnaCompeteSequences = importRNAcompete(RNAcompete_file)

    # padding the sequences
    maxLength = maxlen(rnaCompeteSequences, sequences)
    training_sequences = calculate_padding(training_sequences, maxLength)
    validation_sequences = calculate_padding(validation_sequences, maxLength)
    rnaCompeteSequences = calculate_padding(rnaCompeteSequences, maxLength)

    # one-hot encoding for each sequence
    training_sequences = np.array(list(map(oneHot, training_sequences)))
    validation_sequences = np.array(list(map(oneHot, validation_sequences)))
    sequences_test = np.array(list(map(oneHot, rnaCompeteSequences)))

    # model initialization
    best_parameters = {"filter_number": 128, "fc_size": 64, "kernel_size": 6, "lr": 0.009368509364907707,
                       "loss_function": 1, "activation_function": 0, "max_length": maxLength}
    model = modeli(best_parameters)
    # from categorical classes to one-hot encoded
    y_train_encoded = to_categorical(np.array(training_outputs), num_classes=4)
    y_valid_encoded = to_categorical(np.array(validation_outputs), num_classes=4)
    validation = (validation_sequences, y_valid_encoded)

    # Define EarlyStopping callback
    callback = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',  # Metric to monitor for early stopping
        patience=3,  # Number of epochs with no improvement to wait before stopping
        min_delta=0.00005,
        restore_best_weights=True  # Restore model weights from the epoch with the best monitored metric
    )

    # model evaluation
    model.fit(x=training_sequences, y=y_train_encoded, validation_data=validation, epochs=20, batch_size=1024,
              verbose=1, shuffle=True, callbacks=[callback])
    prediction_list = model.predict(sequences_test)
    evaluate(outputFile, prediction_list)
