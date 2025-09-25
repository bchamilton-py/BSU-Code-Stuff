#Ben Hamilton
#Adventure Game
#September 25, 2025
#This is a basic choose your own adventure game.

game = {
      "start": ["You arrive at the opening of a mysterious portal.", "Enter the mysterious portal", "enter", "Deny the call to adventure", "deny"], 
      "enter": ["You enter the portal to find a musty castle with two doors guarded by knights. You can't understand what they're saying.", "Enter the door to the left", "left", "Enter the door to the right", "right"], 
      "deny": ["Someone understands the hero's journey! Unfortunately, I'm bad writer.", "Return to start", "start", "Quit like a coward", "quit"], 
      "left": ["Apparently the guard was telling you to go through the right door. You open the door and plummet to your death.", "Return to start", "start", "Quit like a coward", "quit"], 
      "right": ["The door reveals a pirate themed children's birthday party. There's cake and presents.", "Get a slice of cake", "cake", "Open a present", "present"], 
      "cake": ["You eat your slice of cake and shrink to the size of a mouse. This is great fun until a rather snotty toddler chews on you.", "Return to start", "start", "Quit like a coward", "quit"], 
      "present": ["You open a present that contains a real life scimitar. This is very good because an irate birthday boy who saw you steal his present also has a real life scimitar.", "Fight the child", "fightChild", "Leap out the window", "leap"], 
      "fightChild": ["I'm not going to dignify this choice with a story based response... He's a child, man. Have some class.", "Return to start", "start", "Quit like a coward", "quit"], 
      "leap": ["You leap out the window and grab hold of a conviently placed rope to swing to an opposing parapet. Guards approach, swords in hand.", "Fight the Guards", "fightGuards", "Explain the Situation", "explain"], 
      "fightGuards": ["You easily handle the guards, slashing and swinging your sword until they've all fallen before you. You see five archers preparing to fire upon you from other walls.", "Climb down the nearby ladder", "ladder", "Catch the arrows", "catch"], 
      "explain": ["I applaud your diplomatic intentions, unfortunately you still can't understand what anyone is saying and they cut you down.", "Return to start", "start", "Quit like a coward", "quit"], 
      "ladder": ["You quickly climb down the ladder and find yourself in a courtyard near the armory and stables.", "Run to the stables", "stables", "Run to the armory", "armory"], 
      "catch": ["You successfully catch two of the arrows, unfortunately all five archers fired at once. ", "Return to start", "start", "Quit like a coward", "quit"], 
      "stables": ["You enter the stables hop on a horse and ride your way out of the castle. You find a portal and are freed from this nightmare.", "Return to start", "start", "Quit like a coward", "quit"], 
      "armory": ["Good idea, run to the area filled with guards with sharp weapons. They quickly dispatch you.", "Return to start", "start", "Quit like a coward", "quit"], 
 }

def main():
    keepGoing = True
    node = "start"
    while(keepGoing):
        if node != "quit":
            node = playNode(node)
            
def playNode(node):
    print(game[node][0])
    print("1) ", game[node][1])
    print("2) ", game[node][3])
    response = input("Your choice (1/2): ")
    if response == "1":
        return game[node][2]
    if response == "2":
        return game[node][4]
    else:
        print("This is not a valid answer.")
        return node

#def getGame(node, response):
    
main()