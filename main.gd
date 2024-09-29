extends Node2D

var room_scene = preload("res://room1.tscn")  # Preload the Room scene
var duplicate_players_script = preload("res://duplicatePlayer.gd")  # Preload duplicatePlayers script

func _ready():
	instance_rooms_and_players()

# Instance the room and spawn players in it
func instance_rooms_and_players():
	var room_instance = room_scene.instance()
	add_child(room_instance)  # Add the room to the scene

	# Instance the duplicatePlayers script and spawn players
	var duplicate_players_instance = duplicate_players_script.new()
	duplicate_players_instance.room_positions = [Vector2(100, 100)]  # Add room position(s)
	add_child(duplicate_players_instance)
