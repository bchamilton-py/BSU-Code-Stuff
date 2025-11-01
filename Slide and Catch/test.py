import pygame, simpleGE, random

def saveScore(bestScore):
    outFile = open("score.json", "w")
    json.dump(bestScore, outFile, indent = 2)
    outFile.close()
    print(json.dumps(bestScore, indent = 2))
    
def loadScore():
    inFile = open("score.json", "r")
    bestScore = json.load(infile)
    inFile.close()
    if bestScore == []:
        bestScore = 0
    return bestScore

class Shark(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Shark.png")
        self.setSize(50,50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Ocean.png")
        
        self.sndFish = simpleGE.Sound("crunch.mp3")
        self.sndBomb = simpleGE.Sound("explosion.mp3")
        
        self.Shark = Shark(self)
        self.Fish = Fish(self)
        self.Bomb = Bomb(self)
        
        self.sprites = [self.Shark,
                        self.Fish,
                        self.Bomb]
            
            
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()