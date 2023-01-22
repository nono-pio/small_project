from Player import Player
import random
import math

class Pop:
    def __init__(self, nbPlayer, brain) -> None:
        self.nbPlayer = nbPlayer
        self.pop = [Player(annexe=brain) for _ in range(nbPlayer)]
        self.popDead = []
    
    def ActionOver(self, ActionOver:function):
        for player in self.pop:
            ActionOver(player)

    def update(self, state):
        for player in self.pop:
            player.update(state)

    def newPop(self):
        self.pop += self.popDead
        self.fitness = [math.exp(player.score) for player in self.pop]
        newPop = []
        mutation_rate = 0 # start to 0 finish to 0.05
        while len(newPop) < self.nbPlayer:
            # take 2 Player
            parent1, parent2 = self.newParents()

            # Make 2 childs 
            child1, child2 = parent1.crossfit(parent2)

            # Mutate +- this childs
            newPop.append(child1.mutation(mutation_rate=mutation_rate))
            newPop.append(child2.mutation(mutation_rate=mutation_rate))

            # Up the chance to mutate
            mutation_rate += 0.001
        
        if len(newPop) == self.nbPlayer:
            self.pop = newPop
        else:
            print("Attention problème avec Pop.newPop() !")
            self.pop = newPop[:self.nbPlayer]

    def newParents(self) -> tuple[Player]:
        parent1, parent2 = random.choices(self.pop, self.fitness , k=2)
        if parent1 == parent2:
            return self.newParents()
        else:
            return parent1, parent2

if __name__ == "__main__":
    nbPlayer = 100

    brain = {
        "input":2,
        "output":1,
        "hidden_layer":(2,4,2)
    }

    pop = Pop(nbPlayer, brain)
    for player in pop.pop:
        r = random.uniform(1,100)
        player.fitness = r
        print(r)
    pop.newPop()
    print(len(pop.pop))
