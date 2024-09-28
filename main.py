from building import Block, Person, Exit
from Simulation import simulate


def distributeVictims(building):
    victims = []
    room_positions = []
    total_victims_per_room=20

    # Identify room positions
    for x in range(len(building)):
        for y in range(len(building[0])):
            if building[x][y].type == "Room":
                room_positions.append((x, y))

    # Distribute victims
    for room in room_positions:
        room_x, room_y = room
        for _ in range(total_victims_per_room):
            if len(victims) < 100:  # Total number of victims
                victims.append(Person("Victim", room_x, room_y))

    return victims
# Initialize the building
rows, cols = 4, 3
building = [[None for _ in range(cols)] for _ in range(rows)]
building[0][0] = Block("Room", ["S"])
building[0][1] = Block("Room", ["S"])
building[0][2] = Block("Room", ["S"])
building[1][0] = Block("Hall", ["W"])
building[1][1] = Block("Hall", [])
building[1][2] = Block("Hall", ["E"])
building[2][0] = Block("Room", ["E"])
building[2][1] = Block("Hall", ["E", "W"])
building[2][2] = Block("Room", ["W"])
building[3][0] = Block("Hall", ["E"])
building[3][1] = Block("Hall", ["S", "E", "W"])
building[3][2] = Block("Hall", ["W"])

# Initialize victims
victims = distributeVictims(building)

shooter = Person("Shooter", 1, 1)

# Initialize exits
exits = [Exit(1, 0), Exit(1, 2), Exit(3, 1)]

# Run the simulation
total_deaths = simulate(building, exits, victims, shooter)
print(f"Total Deaths: {total_deaths}")