class Block:
    def __init__(self, block_type, doors):
        self.type = block_type
        self.doors = doors

class Person:
    def __init__(self, person_type, position_x, position_y):
        self.type = person_type
        self.position_x = position_x
        self.position_y = position_y
        self.status = "Alive"
        self.last_position = (position_x, position_y)

    def move(self, direction):
        if direction == 'N':
            self.position_y -= 1
        elif direction == 'S':
            self.position_y += 1
        elif direction == 'E':
            self.position_x += 1
        elif direction == 'W':
            self.position_x -= 1

    def die(self):
        self.status = "Dead"

    def safe(self):
        self.status = "Safe"

class Exit:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
