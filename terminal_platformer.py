import time
import keyboard

#game data
level = []
playerPos = [1,2]
isPlaying = True

print("_________________________")
print("Use arrows to move player")
print("Press CTRL to stop game")
print("Goal: get to the O")
print("_________________________")
print("game starting in 3 seconds")
time.sleep(3)

#game functions
def getPlayerPos():
    global playerPos
    global isPlaying
    #gravity
    if level[playerPos[1] + 1][playerPos[0]] == "   ":
        level[playerPos[1]][playerPos[0]] = "   "
        playerPos[1] += 1
    elif level[playerPos[1] + 1][playerPos[0]] == " O ":
        isPlaying = False
        print("You Won")
    #movement
    if keyboard.is_pressed("up"):
        print("up")
        if level[playerPos[1] - 1][playerPos[0]] == "   ":
           level[playerPos[1]][playerPos[0]] = "   "
           playerPos[1] -= 1
        elif level[playerPos[1] - 1][playerPos[0]] == " O ":
            isPlaying = False
            print("You Won")
    if keyboard.is_pressed("left"):
        print("left")
        if level[playerPos[1]][playerPos[0] - 1] == "   ":
           level[playerPos[1]][playerPos[0]] = "   "
           playerPos[0] -= 1
        elif level[playerPos[1]][playerPos[0] - 1] == " O ":
            isPlaying = False
            print("You Won")
    if keyboard.is_pressed("right"):
        print("right")
        if level[playerPos[1]][playerPos[0] + 1] == "   ":
           level[playerPos[1]][playerPos[0]] = "   "
           playerPos[0] += 1
        elif level[playerPos[1]][playerPos[0] + 1] == " O ":
            isPlaying = False
            print("You Won")
    if not (keyboard.is_pressed("left") or keyboard.is_pressed("right") or keyboard.is_pressed("up")):
        print("no input")
    #draw player
    level[playerPos[1]][playerPos[0]] = " ◻ "

def drawMap(frames):
    global level
    global isPlaying
    while isPlaying:
        for row in level:
            for block in row:
                print(block,end="")
            print()
        time.sleep(frames)

        getPlayerPos()

        if keyboard.is_pressed("ctrl"):
            isPlaying = False

def createLine(blocks):
    global level
    line = []
    for block in blocks:
        if block == "a":
            line.append("   ")
        elif block == "b":
            line.append(" # ")
        elif block == "s":
            line.append(" △ ")
        elif block == "e":
            line.append(" O ")
        else:
            line.append(f" {block} ")
    level.append(line)

#Level Design

# a: air | b: block | s: spike | e: end

createLine(["b","a","a","a","a","a","a","a","b","b","b"])
createLine(["b","a","a","a","a","a","a","a","a","a","b"])
createLine(["b","a","a","a","a","a","a","a","b","a","b"])
createLine(["b","a","a","s","a","a","a","b","b","e","b"])
createLine(["b","b","b","b","b","b","b","b","b","b","b"])

getPlayerPos()

#Printing the Level
drawMap(1)

#Stopped
print("Stopping Game")
time.sleep(2)