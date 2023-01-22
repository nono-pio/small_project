import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def init(n0, n1, n2):
    W1 = np.random.randn(n1, n0)
    b1 = np.random.randn(n1, 1)
    W2 = np.random.randn(n2, n1)
    b2 = np.random.randn(n2, 1)

    parametre = {
        'W1': W1,
        'b1': b1,
        'W2': W2,
        'b2': b2
    }

    return parametre

def forward_propagation(X, parametre):

    W1 = parametre['W1']
    b1 = parametre['b1']
    W2 = parametre['W2']
    b2 = parametre['b2']

    Z1 = W1.dot(X) + b1
    A1 = 1/(1 + np.exp(-Z1))
    Z2 = W2.dot(A1) + b2
    A2 = 1/(1 + np.exp(-Z2))

    activation = {
        'A1': A1,
        'A2': A2
    }

    return activation

def back_propagation(X, y, activation, parametre):
    
    A1 = activation['A1']
    A2 = activation['A2']
    W2 = parametre['W2']

    m = y.shape[1]

    dZ2 = A2 - y
    dW2 = 1/m * dZ2.dot(A1.T)
    db2 = 1/m * np.sum(dZ2, axis=1, keepdims=True)
    
    dZ1 = np.dot(W2.T, dZ2) * A1 * (1 - A1)
    dW1 = 1/m * dZ1.dot(X.T)
    db1 = 1/m * np.sum(dZ1, axis=1, keepdims=True)

    gradients = {
        'dW1': dW1,
        'db1': db1,
        'dW2': dW2,
        'db2': db2
    }

    return gradients

def update(gradients, parametre, learning_rate):

    W1 = parametre['W1']
    b1 = parametre['b1']
    W2 = parametre['W2']
    b2 = parametre['b2']

    dW1 = gradients['dW1']
    db1 = gradients['db1']
    dW2 = gradients['dW2']
    db2 = gradients['db2']

    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    parametre = {
        'W1': W1,
        'b1': b1,
        'W2': W2,
        'b2': b2
    }
    return parametre

def log_loss(y, A):
    return 1 / y.shape[0] * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A))

def predict(X, parametre):
    activation = forward_propagation(X, parametre)
    return activation['A2'] >= 0.5

def neur_arti_2couche(X_train, y_train, n1, learning_rate=0.1, n_iter=100):

    #initalisation
    n0 = X_train.shape[0]
    n2 = y_train.shape[0]
    parametres = init(n0, n1, n2)

    train_loss = []
    train_acc = []

    for i in range(n_iter):

        activations = forward_propagation(X_train, parametres)
        gradients = back_propagation(X_train, y_train, activations, parametres)
        parametres = update(gradients, parametres, learning_rate)

        if i % 10 == 0:
            train_loss.append(log_loss(y_train, activations['A2']))
            y_pred = predict(X_train, parametres)
            acc = accuracy_score(y_train.flatten(), y_pred.flatten())
            train_acc.append(acc)
        
    plt.figure(figsize=(14,4))

    plt.subplot(1,2,1)
    plt.plot(train_loss,label="train loss")
    plt.legend()
    
    plt.subplot(1,2,2)
    plt.plot(train_acc,label="train acc")
    plt.legend()

    plt.show()

    return parametres