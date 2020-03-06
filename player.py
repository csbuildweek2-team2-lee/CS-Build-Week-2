import requests as requests
import hashlib
import json
import time
from decouple import config

api_key = 'Token 340f0eab302a5dfcd3a41113296527f9db0f3c75'

headers = {
    'Authorization': api_key,
    'Content-Type': 'application/json'}

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.base_url = "https://lambda-treasure-hunt.herokuapp.com/api"

#Server
        self.cd = None  # Cooldown
        self.lc_balance = None  # Lambda Coin balance
        self.lc_mining = None  # Lambda Coin mining data
        self.lc_proof = None  # Lambda Coin last valid proof
        self.room = None  # Room data
        self.p_status = None  # Player status

#Init

    def init(self):
        endpoint = "/adv/init/"
        res = requests.get(self.base_url + endpoint, headers=headers)

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

#Treasure Hunting

    def take(self):
        endpoint = "/adv/take/"
        data = {"name": "treasure"}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} TAKING TREASURE')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])
            
    def drop(self):
        endpoint = "/adv/drop/"
        data = {"name": "treasure"}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} DROPPING TREASURE')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])

    def sell(self):
        endpoint = "/adv/sell/"
        data = {"name": "treasure"}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} SELL TREASURE')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])

    def sell_confirm(self):
        endpoint = "/adv/sell/"
        data = {"name": "treasure", "confirm": "yes"}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} SELL CONFIRM TREASURE')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])

    def pray(self):
        endpoint = "/adv/pray/"
        data = {"name": "treasure"}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} Pray')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])

# Walk About 

    def move(self, direction):
        endpoint = "/adv/move/"
        data = {"direction": direction}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        next_room = json.loads(res.text)
        self.current_room = next_room
        print(f'{next_room} Here is our new room.')
        
        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

    def wise_move(self, direction, room):
        print(f'Direction: {direction} Room: {room}')
        endpoint = "/adv/move/"
        data = {"direction": direction, "next_room": room}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

#Carry and Receive

    def carry(self, item):
        endpoint = '/adv/carry/'
        data = {"name": item}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])

    def receive(self):
        endpoint = '/adv/receive/'
        res = requests.post(self.base_url + endpoint, headers=headers)

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])

# Current Status and Examine

    def status(self):
        endpoint = "/adv/status/"
        res = requests.post(self.base_url + endpoint, headers=headers)
        print(f'------- {res.text} STATUS')

        self.p_status = json.loads(res.text)  # Parse player data
        self.cd = self.p_status['cooldown']  # Get cooldown

    def examine(self):
        endpoint = "/adv/examine/"
        data = {"name": "Wishing Well"}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} WISHING WELL INFO')

# Equipment

    def wear(self, item):
        endpoint = "/adv/wear/"
        data = {"name": item}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} WEAR')

        self.p_status = json.loads(res.text)  # Parse player data
        self.cd = self.p_status['cooldown']  # Get cooldown

        if self.p_status['errors']:
            print(self.p_status['errors'])
        else:
            print(self.p_status['messages'])

    def undress(self, item):
        endpoint = "/adv/undress/"
        data = {"name": item}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} UNDRESS')

        self.p_status = json.loads(res.text)  # Parse player data
        self.cd = self.p_status['cooldown']  # Get cooldown

        if self.p_status['errors']:
            print(self.p_status['errors'])
        else:
            print(self.p_status['messages'])

#Change Name Legally

    def change_name(self, name):
        endpoint = "/adv/change_name/"
        data = {"name": name}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} CHANGE NAME')

#Sprint

    def dash(self, direction, number_of_rooms, sequential_room_ids):
        endpoint = "/adv/dash/"
        data = {
            "direction": direction,
            "num_rooms": number_of_rooms,
            "next_room_ids": sequential_room_ids
        }
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} DASH')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

    def flight(self, direction):
        endpoint = "/adv/fly/"
        data = {"direction": direction}
        res = requests.post(self.base_url + endpoint,
                            headers=headers,
                            data=json.dumps(data))
        print(f'------- {res.text} FLY')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

# Teleport

    def warp(self):
        endpoint = "/adv/warp/"
        res = requests.post(self.base_url + endpoint, headers=headers)
        print(f'------- {res.text} WARP')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

    def recall(self):
        endpoint = "/adv/recall/"
        res = requests.post(self.base_url + endpoint, headers=headers)
        print(f'------- {res.text} RECALL')

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

# Transmorgify

    def transmogrify(self, item):
        endpoint = '/adv/transmogrify/'
        res = requests.post(self.base_url + endpoint, headers=headers)

        self.room = json.loads(res.text)  # Parse room data
        self.cd = self.room['cooldown']  # Get cooldown

        if self.room['errors']:
            print(self.room['errors'])
        else:
            print(self.room['messages'])


# The Reason I'm here: Lambda Coins

    def mine(self, new_proof):
        endpoint = '/bc/mine/'
        data = {'proof': new_proof}
        res = requests.post(
            self.base_url + endpoint, 
            headers=headers,
            data=json.dumps(data))

        self.lc_mining = json.loads(res.text)  # Parse mining data
        self.cd = self.lc_mining['cooldown']  # Get cooldown

        if self.lc_mining['errors']:
            print(self.lc_mining['errors'])
        else:
            print(self.lc_mining['messages'])

    def proof(self):
        endpoint = '/bc/last_proof/'
        res = requests.get(self.base_url + endpoint, headers=headers)

        # Parse last valid proof data
        self.lc_proof = json.loads(res.text)
        self.cd = self.lc_proof['cooldown']  # Get cooldown

    def balance(self):
        endpoint = '/bc/get_balance'
        res = requests.get(self.base_url + endpoint, headers=headers)

        # Parse Lambda Coin balance data
        self.lc_balance = json.loads(res.text)
        self.cd = self.lc_balance['cooldown']  # Get cooldown