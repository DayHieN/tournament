import json
import random



# Generate 40 player objects with random names and ages
players = []
for _ in range(40):
    player = {
        "name": f"Player{_ + 1}",
        "age": random.randint(18, 40)
    }
    players.append(player)

# Convert the list of player dictionaries to a JSON string
json_data = json.dumps(players, indent=2)

# Save the JSON data to a file (optional)
with open("players.json", "w") as json_file:
    json_file.write(json_data)