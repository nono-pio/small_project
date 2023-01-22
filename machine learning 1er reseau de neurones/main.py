from neur_arti_2couche import neur_arti_2couche
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

X, y = make_circles(n_samples=100, noise=0.1, factor=0.3, random_state=0)
X = X.T
y = y.reshape((1, y.shape[0]))

#plt.scatter(X[0, :], X[1, :], c=y, cmap='summer')
#plt.show()

parametre = neur_arti_2couche(X, y, n1=2, n_iter=1000, learning_rate=0.1)
print(parametre)