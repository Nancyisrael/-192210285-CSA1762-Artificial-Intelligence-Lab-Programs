import random
room = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
vacuum_position = [0, 0]

def clean_room(vacuum, room):
    x, y = vacuum
    if room[x][y] == 1:
        room[x][y] = 0
        print(f"Cleaned position ({x}, {y})")
    x = random.randint(0, len(room) - 1)
    y = random.randint(0, len(room[0]) - 1)
    vacuum[0], vacuum[1] = x, y
    print(f"Moved to ({x}, {y})")

for _ in range(5):  
    clean_room(vacuum_position, room)

print("Final room state:")
for row in room:
    print(row)
