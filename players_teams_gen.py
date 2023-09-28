import json
import random




players = []
for _ in range(40):
    player = {
        "name": f"Player{_ + 1}",
        "age": random.randint(18, 40)
    }
    players.append(player)


json_data = json.dumps(players, indent=2)


with open("players.json", "w") as json_file:
    json_file.write(json_data)