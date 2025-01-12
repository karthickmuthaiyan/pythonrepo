import math

# Initial position
x, y = 0, 0

# Movements
movements = [
    ("UP", 5),
    ("DOWN", 3),
    ("LEFT", 3),
    ("RIGHT", 2)
]

# Process each movement
for direction, steps in movements:
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

# Calculate the distance from the origin
print(x,y)
distance = math.sqrt(x**2 + y**2)

print(f"The distance from the origin is {distance}")