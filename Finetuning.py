from GPyOpt.methods import BayesianOptimization
from main import *
import numpy as np


# With this file we preformed Fine-tuning to the model using Bayesian optimizer
def objective_function(params):
    l1 = int(params[0, 0])
    l2 = int(params[0, 1])
    loss = int(params[0, 2])
    ks = int(params[0, 3])
    af = int(params[0, 4])
    lr = params[0, 5]
    model = modeli(l1, l2, ks, lr, loss, af)
    history = model.fit(x = training_sequences, y = y_train_encoded, validation_data = validation,
            epochs=20, batch_size = 32, verbose=1, shuffle = True, callbacks=[callback])
    val_loss = history.history['val_loss'][-1]
    return val_loss

# creating the ranges we want to test for each hyperparameter
bounds = [{'name': 'l1', 'type': 'discrete', 'domain': (256, 128)},
          {'name': 'l2', 'type': 'discrete', 'domain': (64, 128)},
          {'name': 'loss', 'type': 'categorical', 'domain': (0, 1)},
          {'name': 'ks', 'type': 'discrete', 'domain': (5, 6)},
          {'name': 'af', 'type': 'categorical', 'domain': (0, 1)},
          {'name': 'lr', 'type': 'continuous', 'domain': (0.005, 0.01)}]

# Create the Bayesian optimization object
optimizer = BayesianOptimization(f=objective_function, domain=bounds)
# Run optimization for a few iterations
optimizer.run_optimization(max_iter=10, verbosity=True)
# Get the best hyperparameters
best_l1, best_l2, best_loss, best_size, best_activation, best_learning_rate = optimizer.X[np.argmax(optimizer.Y)]