extends Node2D

var player_scene = preload("res://player.tscn")

# This variable should hold an array of room positions
var room_positions = []  # You will need to pass room positions from your room layout

func _ready():
	spawn_players_in_rooms()

# Function to spawn players in each room (20 players per room)
func spawn_players_in_rooms():
	for room_position in room_positions:
		spawn_players_in_room(room_position, 20)  # Spawn 20 players in each room

# Spawns a specified number of players in a given room
func spawn_players_in_room(room_position: Vector2, num_players: int):
	for i in range(num_players):
		var new_player = player_scene.instance()
		# Random position within the room bounds (64x64 for each room)
		new_player.position = room_position + Vector2(randf_range(16, 80), randf_range(16, 80))
		add_child(new_player)
