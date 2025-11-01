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

def updateBestScore(newScore):
    best = loadScore()
    if newScore > best:
        best = newScore
        saveScore(best)
    return best

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
        
        self.hearts = 3
        self.score = 0
        
        self.sndFish = simpleGE.Sound("crunch.mp3")
        self.sndBomb = simpleGE.Sound("explosion.mp3")
        
        self.Shark = Shark(self)
        self.Fish = []
        for i in range(5):
            self.Fish.append(Fish(self))
        self.Bomb = []
        for i in range(3):
            self.Bomb.append(Bomb(self))
            
        self.lblScore = LblScore()
        self.lblHearts = LblHearts()
        
        self.sprites = [self.Shark,
                        self.Fish,
                        self.Bomb,
                        self.lblScore,
                        self.lblHearts]
    def process(self):
        for fish in self.Fish:
            if self.Shark.collidesWith(fish):
                self.sndFish.play()
                fish.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
        
        for bomb in self.Bomb:
            if self.Shark.collidesWith(bomb):
                self.sndBomb.play()
                bomb.reset()
                self.hearts -= 1
                self.lblHearts.text = f"Lives: {self.hearts}"
        
        if self.hearts == 0:
            print(f"Final Score: {self.score}")
            newScore = self.score
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("Ocean.png")
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
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
    best = loadScore()
    while keepGoing:
        instructions = Instructions(best)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            newScore = game.score
            best = updateBestScore(newScore)
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()
    