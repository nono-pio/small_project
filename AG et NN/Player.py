from Brain import brain
import numpy as np

class Player:

    x = 20
    width = 10
    height = 10
    gravity = 9.81

    def __init__(self, annexe=None, mode="random") -> None:
        # init for the game
        self.score = 0

        self.y = 0
        self.vy = 0

        self.dead = False

        # init the brain
        match mode:
            case "random":
                if annexe == None:
                    annexe = {
                        "input":2,
                        "output":1,
                        "hidden_layer":(2,4,2)
                    }
                self.brain = brain(annexe=annexe)
            
            case "brain":
                self.brain = annexe["brain"]
    
    def update(self, state:list):

        # adapt the state for the bird and choose an action
        state = [state[0], abs(state[1] - self.y), abs(state[2] - self.y)]
        action = self.make_action(state).argmax() # 0=nothing 1=jump

        # update velocity
        if action == 1:
            self.vy -= 50
        
        self.vy += self.gravity
        
        # update posY
        self.y += self.vy


    def make_action(self, state:list):
        return np.array(self.brain.predict(state)).round(0)
    
    def crossfit(self, player2):
        
        Brain1, Brain2 = self.brain.crossfit(player2.brain)

        return Player(annexe={"brain":Brain1}, mode="brain"), Player(annexe={"brain":Brain2}, mode="brain")
    
    def mutation(self, mutation_rate=0.01, mutation_force=1):
        self.brain.mutation(mutation_rate, mutation_force)

if __name__ == "__main__":
    p1 = Player()
    p2 = Player()

    state = [1,2]
    print(p1.make_action(state))
    print(p2.make_action(state))