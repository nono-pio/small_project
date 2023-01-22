from Env import Game

maxGen = 10
nbPlayer = 100

# Player brain
brain = {
    "input":2,
    "output":1,
    "hidden_layer":(2,4,2)
}

env = Game(nbPlayer, brain)

for gen in range(1, maxGen + 1):
    env.reset(gen)
    done = False
    
    while not done:
        done = env.play_step()
    
    print(env.best_player())
