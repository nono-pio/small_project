import numpy as np

def init(X):
    W = np.random.randn(X.shape[1],1)
    b = np.random.randn(1)
    return W, b

def model(X, W, b):
    Z = X.dot(W) + b
    A = 1 / (1 + np.exp(-Z))
    return A

def logLoss(A,y):
    eps = 1e-15
    return 1/len(y) * np.sum(-y * np.log(A + eps) - (1 - y) * np.log(1 - A + eps))

def gradients(A,X,y):
    dW = 1/len(y) * np.dot(X.T, A - y)
    db = 1/len(y) * np.sum(A - y)
    return dW, db

def update(dW, db, W, b, learning_rate):
    W = W - learning_rate*dW
    b = b - learning_rate*db
    return W, b

def predict(X, W, b):
    A = model(X, W, b)
    return A >= 0.5

def neur_arti(X, y, learning_rate = 0.1 , n_iteration = 100):
    # init
    W, b = init(X)

    Loss = []

    for i in range(n_iteration):
        A = model(X, W, b)
        Loss.append(logLoss(A, y))
        dW, db = gradients(A, X, y)
        W, b = update(dW, db, W, b, learning_rate)
    
    y_pred = predict(X, W, b)

    return Loss, y_pred, W, b