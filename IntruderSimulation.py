class Block:
  def __init__(self, type, doors):
    self.type = type
    self.doors = doors

class Person:
    def __init__(self, type, positionx, positiony):
        self.type = type
        self.positionx = positionx
        self.positiony = positiony
        self.status = "Alive"

    def move(direction):
        if dir == 'N':
          positiony -= 1
        elif dir == 'S':
            positiony += 1
        elif dir == "E":
           positionx += 1
        elif dir == "W":
           positionx -= 1
    def died():
       status = "Dead"
    def safe():
       status = "Safe"
class Exit:
    def __init__(self, positionx, positiony):
        self.positionx = positionx
        self.positiony = positiony
   
def getIsDead(victim):
    #check if victim made it out of building
    if(victim.positionx > Building.length or victim.positionx < 0 or victim.positionY > Building[0].length or victim.positionY < 0):
       return False
    #victim and intruder same position
    if(victim.positionx == intruder.positionx and victim.positiony == intruder.positionY):
       return True
    #victim or intruder in a room
    if(Building[victim.positionx][victim.positiony].type == "Room" or Building[intruder.positionx][intruder.positiony].type == "Room"):
       return False
    
    if(intruder.postiony == victim.positiony): #same y plane
       dist = intruder.positiony - victim.posittiony
       if(dist < 0): #intruder is north
          for i in range(intruder.positiony, victim.positiony):
            if(Building[intruder.positionx][i].type == "Room"):
                return False
          return True
       else: #intruder is south
          for i in range(victim.positiony, intruder.positiony):
            if(Building[intruder.positionx][i].type == "Room"):
                return False
          return True
       

    elif(intruder.positionx == victim.positionx): # same x plane
        dist = intruder.distancex - victim.distancex
        if(dist < 0): #intruder is west
            for i in range(intruder.positionx, victim.positionx):
                if(Building[i][intruder.positiony].type == "Room"):
                    return False
            return True
        else: #intruder is east
            for i in range(victim.positionx, intruder.positionx):
                if(Building[i][intruder.positiony].type == "Room"):
                    return False
            return True
    return False

Building = [4][3]
Building[0][0] = Block("Room", ["S"])
Building[0][1] = Block("Room", ["S"])
Building[0][2] = Block("Room", ["S"])
Building[1][0] = Block("Hall", ["W"])
Building[1][1] = Block("Hall", [])
Building[1][2] = Block("Hall", ["E"])
Building[2][0] = Block("Room", ["E"])
Building[2][1] = Block("Hall", ["E", "W"])
Building[2][2] = Block("Room", ["W"])
Building[3][0] = Block("Hall", ["E"])
Building[3][1] = Block("Hall", ["S", "E", "W"])
Building[3][2] = Block("Hall", ["W"])

victims = []
for i in 15:
   victims[i] = Person("Victim", 0, 0)
for i in range(15,30):
   victims[i] = Person("Victim",0,1)
for i in range(30,45):
   victims[i] = Person("Victim",0,2)
for i in range(45,60):
   victims[i] = Person("Victim",2,0)
for i in range(60,75):
   victims[i] = Person("Victim",2,2)
for i in range(75,90):
   victims[i] = Person("Victim",3,0)
for i in range(90,105):
   victims[i] = Person("Victim",3,2)

intruder = Person("Intruder", 2, 1)

Exits = []
Exits[0] = Exit(1,0)
Exits[1] = Exit(1,2)
Exits[2] = Exit(3,1)



