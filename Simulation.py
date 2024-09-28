from pathfinding import optimalPath
import random
from building import Person

def getIsDead(victim, intruder, building):
    #check if victim made it out of building
    if(victim.position_x > len(building) or victim.position_x < 0 or victim.position_y > len(building[0]) or victim.position_y < 0):
       return False
    #victim and intruder same position
    if(victim.position_x == intruder.position_x and victim.position_y == intruder.position_y):
       return True
    #victim or intruder in a room
    if(building[victim.position_x][victim.position_y].type == "Room" or building[intruder.position_x][intruder.position_y].type == "Room"):
       return False
    
    if(intruder.position_y == victim.position_y): #same y plane
       dist = intruder.position_y - victim.position_y
       if(dist < 0): #intruder is north
          for i in range(intruder.position_y, victim.position_y):
            if(building[intruder.position_x][i].type == "Room"):
                return False
          return True
       else: #intruder is south
          for i in range(victim.position_y, intruder.positiony):
            if(building[intruder.position_x][i].type == "Room"):
                return False
          return True

def checkDeaths(victims, shooter, building):
    deadVictims = []
    for victim in victims:
        if(getIsDead(victim, shooter, building)):
           deadVictims.append(victim)
           victim.die()
    return deadVictims

def move_shooter(shooter, building):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E
    possible_moves = []

    for dx, dy in directions:
        nx, ny = shooter.position_x + dx, shooter.position_y + dy
        if 0 <= nx < len(building) and 0 <= ny < len(building[0]):
            # Allow movement into both halls and rooms
            possible_moves.append((nx, ny))

    if possible_moves:
        # Randomly choose a move from the available options
        shooter.last_position = (shooter.position_x, shooter.position_y)  # Update last position before moving
        shooter.position_x, shooter.position_y = random.choice(possible_moves)
    else:
        # Move backward if there are no possible moves
        shooter.position_x, shooter.position_y = shooter.last_position

def simulate(building, exits, victims, shooter):
    total_deaths = 0
    turn_limit = 10  # Set a limit to avoid infinite loops

    for turn in range(turn_limit):
        
        # Move the shooter
        move_shooter(shooter, building)

        # Evacuate victims
        for victim in victims:
            if victim.status == "Alive":
                path_to_exit = optimalPath(victim, building, exits)
                if path_to_exit:
                    next_pos = path_to_exit[0]  # Get the next position on the path
                    if len([v for v in victims if (v.position_x, v.position_y) == next_pos]) < 20:
                        victim.position_x, victim.position_y = next_pos

        # Check for deaths
        dead_victims = checkDeaths(victims, shooter, building)
        total_deaths += len(dead_victims)
        
        # Remove dead victims from the list
        victims = [v for v in victims if v.status == "Alive"]

        # Print current positions
        for v in victims:
            print(f"{v.type} at ({v.position_x}, {v.position_y})")
        print(f"Shooter at ({shooter.position_x}, {shooter.position_y})")
        print(f"Total deaths so far: {total_deaths}\n")
        print(f"still alive:  {len(victims)}\n")

        # End simulation if all victims are dead or evacuated
        if not victims:
            print("All victims are dead.")
            break

    return total_deaths

