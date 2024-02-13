import tkinter as tk
import random

# Initialize Tkinter
root = tk.Tk()
root.title("Blue Aquarium")

# Set up canvas
canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()

# Fish properties
fishList = [
    {
        "x": 60,
        "y": 300,
        "size" : 60,
        "speed" : 1,
        "color": "orange"
    },
    {
        "x": 60,
        "y": 100,
        "size" : 60,
        "speed" : 0.5,
        "color": "pink"
    },
]

# Bubble properties
bubbles = []

# Plant properties
plants = [(200, 550), (300, 550), (550, 550)]

# Function to move the fish
def move_fish(fish):
    fish["x"] += fish["speed"]
    if fish["x"] >= 800:  # Reset fish position when it reaches the right edge
        fish["x"] = fish["size"]

# Draw the fish with eyes and a smile
def draw_fish(x, y, size, color):
    canvas.create_oval(x, y, x + size, y + size, fill=color)  # Body
    canvas.create_polygon(x - size / 2 + 32, y + size / 2, x-36, y + size/ 5 - 1, x-36, y + size * 4 / 5 + 1, fill="black") # Tail Outline
    canvas.create_polygon(x - size / 2 + 30, y + size / 2, x-35, y + size/ 5, x-35, y + size * 4 / 5, fill=color) # Tail Fill
    canvas.create_oval(x + size / 4, y + size / 4, x + size / 4 + 5, y + size / 4 + 5, fill="black")  # Left eye
    canvas.create_oval(x + size / 4 * 3, y + size / 4, x + size / 4 * 3 + 5, y + size / 4 + 5, fill="black")  # Right eye
    canvas.create_arc(x + size / 4, y + size / 2, x + size / 4 * 3, y + size / 4 * 3, start=180, extent=180, style=tk.ARC)  # Smile

# Function to draw the aquarium
def draw_aquarium():
    canvas.delete("all")
    
    # Draw the aquarium background
    canvas.create_rectangle(0, 0, 800, 600, fill="lightblue")
    
    # Draw plants
    for plant_x, plant_y in plants:
        canvas.create_rectangle(plant_x, plant_y, plant_x + 20, plant_y + 50, fill="green")
    
    # Draw the fish
    for fish in fishList:
        draw_fish(fish["x"], fish["y"], fish["size"], fish["color"])
    
    # Generate random bubbles
    if random.randint(0, 100) < 5:
        bubble_size = random.randint(5, 15)
        bubble_x = random.randint(0, 800)
        bubble_y = 600
        bubbles.append((bubble_x, bubble_y, bubble_size))
    
    # Move bubbles upward
    for i in range(len(bubbles)):
        x, y, size = bubbles[i]
        y -= random.randint(0, 10) / 20  # Adjust the speed of bubbles here
        bubbles[i] = (x, y, size)
    
    # Draw bubbles
    for bubble_x, bubble_y, bubble_size in bubbles:
        canvas.create_oval(bubble_x, bubble_y, bubble_x + bubble_size, bubble_y + bubble_size, fill="white")
    
    root.update()

while True:
    # Start moving the fish
    for fish in fishList:
        move_fish(fish)

    draw_aquarium()

# Run the Tkinter event loop
root.mainloop()
