from room import Room
from player import Player
from world import World
import random
from ast import literal_eval
from graph import Graph

player = Player('Name', 0)
player.init()
time.sleep(player.cd)
graph = dict()
mapped = []
traversal_path = []
reverse_path = []
visited_rooms = set()