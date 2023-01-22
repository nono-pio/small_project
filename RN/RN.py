import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from tqdm import tqdm

class Layer:
    def __init__(self, nb_neurone_Lm1:int, nb_neurone:int):
        self.n = nb_neurone
        self.W = np.random.randn(nb_neurone, nb_neurone_Lm1)
        self.b = np.random.randn(nb_neurone,1)

class RN:
    def __init__(self, input:int, output:int, hidden_layer:tuple[int]):
        self.layer = [Layer(input, hidden_layer[0])]
        
        for i in range(1, len(hidden_layer)):
            self.layer.append(Layer(hidden_layer[i-1], hidden_layer[i]))
        
        self.layer.append(Layer(hidden_layer[i], output))
        self.L = len(self.layer) - 1

    def predict(self, X:np.ndarray):
        self.A = [X]

        for layer in self.layer:
            Z = layer.W.dot(self.A[-1]) + layer.b
            self.A.append( 1/(1+np.exp(-Z)) )
        
        return self.A[-1]
    
    '''
    A :
    0) X
    1) layer 0
    2) layer 1
    ...
    L) layer L-1
    L+1) layer L
    
    '''

    def update(self, Y:np.ndarray, lr:float=0.1):
        m = Y.shape[1]

        dZ = self.A[-1] - Y

        for c in reversed(range(len(self.layer))): # c = L, L-1, ..., 2, 1, 0
            
            dW =  1/m * np.dot(dZ, self.A[c].T) 
            db =  1/m * np.sum(dZ, axis=1, keepdims=True)
            if c > 1:
                dZ = np.dot(self.layer[c].W.T, dZ) * self.A[c] * (1 - self.A[c])
            
            self.layer[c].W -= lr*dW
            self.layer[c].b -= lr*db
    

    def loss(self, Y:np.ndarray, eps:float=1e-15):
        return 1 / len(Y) * np.sum(-Y * np.log(self.A[-1] + eps) - (1 - Y) * np.log(1 - self.A[-1] + eps))
    

    def train(self,X:np.ndarray, Y:np.ndarray, n_iter:int=100, lr:float=0.1):
        train_loss = []
        train_acc = []

        for i in tqdm(range(n_iter)):

            Ypredict = self.predict(X) >= 0.5 #predict and forward_propagation 
            self.update(Y, lr=lr)

            if i%10 == 0:
                train_loss.append(self.loss(Y))

                cur_acc = accuracy_score(Y.flatten(), Ypredict.flatten())
                train_acc.append(cur_acc)
        
        self.accuracy = train_acc
        self.loss = train_loss

        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18,4))
        ax[0].plot(train_loss, label="train loss")
        ax[0].legend()

        ax[1].plot(train_acc, label="train acc")
        ax[1].legend()

        plt.show()