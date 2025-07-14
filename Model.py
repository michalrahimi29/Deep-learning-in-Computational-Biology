import tensorflow as tf
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, AveragePooling1D, BatchNormalization, Dropout, Activation, InputLayer, LSTM
from keras.models import Sequential
from keras.optimizers import Adam

#This is the architecture of the CNN model chosen for predicting RNA binding intensity
def modeli(best_parameters):
    # Those are the optional loss functions and activation function we wanted to test which one is better
    loss_functions = [tf.keras.losses.Poisson(), 'categorical_crossentropy']
    activation_functions = ['sigmoid', 'softmax']

    model = Sequential()
    model.add(Conv1D(best_parameters["filter_number"], kernel_size=best_parameters["kernel_size"], strides=2,
                     input_shape =(best_parameters["max_length"], 4)))
    model.add(Activation('relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(best_parameters["fc_size"], activation='relu'))
    model.add(Dense(units=4, activation=activation_functions[best_parameters["activation_function"]]))
    decay_rate = tf.keras.optimizers.schedules.ExponentialDecay(
      initial_learning_rate=best_parameters["lr"],
      decay_steps=5000,
      decay_rate=0.9)
    adam = Adam(learning_rate=decay_rate, beta_1=0.9, beta_2=0.999)
    model.compile(loss=loss_functions[best_parameters["loss_function"]], optimizer=adam,
                metrics=['accuracy', tf.keras.metrics.AUC(name='auc')])
    return model