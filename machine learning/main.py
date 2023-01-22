import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score

from neur_arti import neur_arti, predict

X, y = make_blobs(n_samples=100,n_features=2,centers=2,random_state=0)
#normalisation de X
X = X / abs(X).max()
y = y.reshape((y.shape[0],1))

#graph x1 x2 couleur green/yellow
#plt.scatter(X[:,0],X[:,1],c=y, cmap='summer')
#plt.show()

#entrainement
#Loss, y_pred, W, b = neur_arti(X,y, learning_rate=0.01)

#graph de l'apprentissage
#plt.plot(Loss)
#plt.show()

#precision du neurone
#print(accuracy_score(y, y_pred))

#prediction d'une nouvelle valeur
#new_value = np.array([x1, x2])
#print(predict(new_value, W, b))