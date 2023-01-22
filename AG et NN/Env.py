from Pop import Pop
from Pipe import Pipe
class Game:

    spaceBetween2PairOfPipe = 150

    def __init__(self, nbPlayer, brain, dimention:tuple) -> None:
        self.players = Pop(nbPlayer, brain)

        self.width = dimention[0]
        self.height = dimention[1]
    
    def reset(self, gen):
        # reset players
        if gen != 0:
            self.players = self.players.newPop()
        
        # reset pipes
        self.pipes:list[Pipe] = []
        self.distanceFromLastPipe = self.width

    def play_step(self) -> bool:

        # add pipes
        if self.distanceFromLastPipe > self.distanceFromLastPipe:
            self.pipes.append(Pipe(self.width, self.height))
        self.distanceFromLastPipe += 1 #velocityOfpipes

        # delete pipe
        if self.pipes[0].x + self.pipes[0].width < 0:
            self.pipes.pop(0)
        
        # update pipes and take the pipe in front players
        pipeTaked = False
        for pipe in self.pipes:
            pipe.update()
            if not pipeTaked and pipe.x + pipe.width > 20 : # 20 = x of players
                pipeInFront = pipe
                pipeTaked = True

        # create state of the game for give to the IA
        state = [pipeInFront.x - 20, pipeInFront.y, pipeInFront.y2] # [distance entre player et pipe, y de la pipe haute, y de la pipe basse]

        # update players with the state
        self.players.update(state)

        # test if a player die
        for player in self.players.pop:
            isDead = pipeInFront.collision((player.x, player.y, player.width, player.height))
            if isDead:
                player.dead = True
                self.players.popDead.append(player)
                self.players.pop.remove(player)

        # test if all player die and set done to true
        done = False
        if len(self.players.pop) == 0:
            done = True
        
        return done


    def best_player(self):
        pass