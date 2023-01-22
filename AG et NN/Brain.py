import numpy as np
import random
from Layer import Layer

class brain:
    def __init__(self, annexe=None, mode="random") -> None:

        self.layer = []
        match mode:
            case "random":
                input, output, hidden_layer = annexe["input"], annexe["output"], annexe["hidden_layer"]
                
                self.nbLayer = len(hidden_layer) + 1

                self.layer.append(Layer(dim = hidden_layer[0], last_dim = input))

                self.layer.extend([Layer(dim=hidden_layer[indexLayer], last_dim=hidden_layer[indexLayer - 1]) for indexLayer in range(1, len(hidden_layer))])
                
                self.layer.append(Layer(dim = output, last_dim = hidden_layer[-1]))
            
            case "layer":
                self.nbLayer, self.layer = len(annexe["layer"]), annexe["layer"]

    def predict(self, X:np.ndarray):

        A = X

        for layerIndex in range(self.nbLayer):
            A = self.layer[layerIndex].predict(A)

        return np.array(A)
    
    def crossfit(self, Brain2):
        randomIndex = random.randint(0, self.nbLayer)
        Brain1Layers = self.layer[:randomIndex] + Brain2.layer[randomIndex:]
        Brain2Layers = Brain2.layer[:randomIndex] + self.layer[randomIndex:]

        newBrain1 = brain(annexe={"layer":Brain1Layers},mode="layer")
        newBrain2 = brain(annexe={"layer":Brain2Layers},mode="layer")
        
        return newBrain1, newBrain2
    
    def mutation(self,mutation_rate, mutation_force):
        for layer in self.layer:
            layer.mutation(mutation_rate, mutation_force)

    
if __name__ == "__main__":
    annexe = {
        "input":2,
        "output":1,
        "hidden_layer":(2,4,2)
    }
    x = brain(annexe=annexe)
    print(x.layer)