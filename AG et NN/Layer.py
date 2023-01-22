import numpy as np
import random
class Layer:
    
    def __init__(self, dim = None, last_dim = None, mode="random"):

        match mode:
            case "random":
                self.W = np.random.randn(dim, last_dim)
                self.b = np.random.randn(dim)

    def predict(self, last_A):
        Z = self.W.dot(last_A) + self.b
        return ( 1/(1 + np.exp(-Z)) )
    
    def mutation(self, mutation_rate, mutation_force):
        def mutate(value, mutation_rate, mutation_force):
            if random.random() <= mutation_rate:
                #return value + random.uniform(-1,1) * mutation_force
                return value + random.gauss() * mutation_force
            else:
                return value
        
        self.W = mutate(self.W, mutation_rate, mutation_force)
        self.b = mutate(self.b, mutation_rate, mutation_force)

