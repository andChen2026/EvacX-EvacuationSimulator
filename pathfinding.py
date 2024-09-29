from collections import deque

def optimalPath(victim, building, exits):
    rows, cols = len(building), len(building[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # NSWE

    for exit in exits:
            x,y= victim.position_x, victim.position_y
            if exit.position_x == x and exit.position_y == y:
                victim.safe()
                exitD = exit.side
                expos = []
                if exitD == "S":
                    expos = [(x,y+1)]
                elif exitD == "N":
                    expos = [(x,y-1)]
                elif exitD == "E":
                    expos = [(x+1, y)]
                elif exitD == "W":
                    expos = [(x-1,y)]
                return [(x, y)] + expos

    queue = deque([(victim.position_x, victim.position_y, [])])
    visited = set((victim.position_x, victim.position_y))

    while queue:
        x, y, path = queue.popleft()

        # Check to see if exit is in the current position
        for exit in exits:
            if exit.position_x == x and exit.position_y == y:
                exitD = exit.side
                expos = []
                if exitD == "S":
                    expos = [(x,y+1)]
                elif exitD == "N":
                    expos = [(x,y-1)]
                elif exitD == "E":
                    expos = [(x+1, y)]
                elif exitD == "W":
                    expos = [(x-1,y)]
                return path + [(x, y)] + expos
            
        # Check other movements
        for dx, dy in directions:
            fx, fy = x + dx, y + dy
            if 0 <= fx < rows and 0 <= fy < cols and (fx, fy) not in visited:
                if building[fx][fy].type != "Room":
                    visited.add((fx, fy))
                    queue.append((fx, fy, path + [(x, y)]))
                    
    return []