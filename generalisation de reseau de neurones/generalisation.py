import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
from tqdm import tqdm

def init(dimensions):

    parametres = {}

    for c in range(1, len(dimensions)):
        parametres["W"+str(c)] = np.random.randn(dimensions[c], dimensions[c - 1])
        parametres["b"+str(c)] = np.random.randn(dimensions[c], 1)
    
    return parametres

def forward_propagation(X, parametres):

    activations = {'A0':X}

    for c in range(1, len(parametres)//2 + 1):
        Z = parametres["W"+str(c)].dot(activations["A"+str(c-1)]) + parametres["b"+str(c)]
        activations["A"+str(c)] = 1/(1+np.exp(-Z))
    
    return activations

def back_propagation(y, parametres, activations):

    m = y.shape[0]
    C = len(parametres)//2

    dZ = activations["A"+str(C)] - y
    gradients = {}

    for c in range(1, C + 1):
        gradients["dW"+str(c)] = 1/m * np.dot(dZ, activations["A"+str(c-1)].T)
        gradients["db"+str(c)] = 1/m * np.sum(dZ, axis=1, keepdims=True)
        if c > 1: dZ = np.dot(parametres["W"+str(c)].T, dZ) * activations["A"+str(c-1)] * (1 - activations["A"+str(c-1)])
    
    return gradients

def update(gradients, parametres, learning_rate):
    
    for c in range(1,len(parametres)//2 + 1):
        parametres["W"+str(c)] = parametres["W"+str(c)] - learning_rate * gradients["dW"+str(c)]
        parametres["b"+str(c)] = parametres["b"+str(c)] - learning_rate * gradients["db"+str(c)]
    
    return parametres

def log_loss(A, y):
    return 1 / len(y) * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A))

def predict(X, parametre):
    activations = forward_propagation(X, parametre)
    return activations["A"+str(len(parametre)//2)]

def deep_neural_network(X, y, hidden_layers = (16, 16, 16), learning_rate = 0.001, n_iter = 3000):
    
    # initialisation parametres
    dimensions = list(hidden_layers)
    dimensions.insert(0, X.shape[0])
    dimensions.append(y.shape[0])
    np.random.seed(1)
    parametres = init(dimensions)

    # tableau numpy contenant les futures accuracy et log_loss
    training_history = np.zeros((int(n_iter), 2))

    C = len(parametres) // 2

    # gradient descent
    for i in tqdm(range(n_iter)):

        activations = forward_propagation(X, parametres)
        gradients = back_propagation(y, parametres, activations)
        parametres = update(gradients, parametres, learning_rate)
        Af = activations['A' + str(C)]

        # calcul du log_loss et de l'accuracy
        training_history[i, 0] = (log_loss(y.flatten(), Af.flatten()))
        y_pred = predict(X, parametres)
        training_history[i, 1] = (accuracy_score(y.flatten(), y_pred.flatten()))

    # Plot courbe d'apprentissage
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(training_history[:, 0], label='train loss')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(training_history[:, 1], label='train acc')
    plt.legend()
    plt.show()

    return training_history


X, Y = make_circles(n_samples=100, noise=0.1, factor=0.3, random_state=0)
X = X.T
Y = Y.reshape(1,Y.shape[0])


deep_neural_network(X,Y, (2,2))