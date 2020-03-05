from player import Player
import hashlib
import miner
import time

player = Player('Name', 0)
player.init()
time.sleep(player.cd)

player.proof()
time.sleep(player.cd)

lvp = player.lc_proof['proof']
difficulty = player.lc_proof['difficulty']

new_proof = miner.proof(lvp, difficulty)

player.miner(new_proof)

time.sleep(player.cd)

player.balance()

print(player.lc_balance)