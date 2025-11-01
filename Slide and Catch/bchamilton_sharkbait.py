import pygame, simpleGE, random, json

def saveScore(bestScore):
    outFile = open("score.json", "w")
    json.dump(bestScore, outFile, indent = 2)
    outFile.close()
    print(json.dumps(bestScore, indent = 2))
    
def loadScore():
    inFile = open("score.json", "r")
    bestScore = json.load(inFile)
    inFile.close()
    if bestScore == []:
        bestScore = 0
    return bestScore

def bestScore(newScore):
    bestScore = loadScore()
    if bestScore >= newScore:
        bestScore = bestScore
    else:
        bestScore = newScore
    return bestScore

class Fish(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fish.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
    
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class Bomb(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("tnt.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
    
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
    
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
    
class LblHearts(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Lives: 3"
        self.center = (500, 30)
    
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
    
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

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("Ocean.png")
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textlines = [
            "You are a shark.",
            "Your goal is to eat lots of fish,",
            "and avoid dynamite. Move with left and right keys",
            "You only get three lives."]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)
        
        self.bestScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Best Score: {self.bestScore}"
        self.lblScore.center = (320, 400)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (550, 400)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnPlay,
                        self.btnQuit]
            
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        
    
def main():
    keepGoing = True
    newScore = 0
    score = bestScore(newScore)
    while keepGoing:
        instructions = Instructions(score)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            newScore = game.score
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()
    