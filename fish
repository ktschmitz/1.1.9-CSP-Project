import tkinter as tk
import random

# Initialize Tkinter
root = tk.Tk()
root.title("Blue Aquarium")

# Set up canvas
canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()

# Fish properties
fish_size = 60
fish_x, fish_y = 0, 300
fish_speed = 4

# Bubble properties
bubbles = []

# Plant properties
plants = [(200, 550), (300, 550), (550, 550)]

# Function to move the fish
def move_fish():
    global fish_x, fish_y, fish_speed
    fish_x += fish_speed
    if fish_x >= 800:  # Reset fish position when it reaches the right edge
        fish_x = fish_size
    draw_aquarium()
    canvas.after(30, move_fish)  # Move the fish every 30 milliseconds

# Draw the fish with a tail
def draw_fish(x, y, size):
    canvas.create_oval(x, y, x + size, y + size, fill="orange")

    # Draw the fish with eyes and a smile
def draw_fish(x, y, size):
    canvas.create_oval(x, y, x + size, y + size, fill="orange")  # Body
    canvas.create_polygon(x - size / 2, y + size / 2, x, y + size / 4, x, y + size * 3 / 4, fill="orange")
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
    draw_fish(fish_x, fish_y, fish_size)
    
    # Generate random bubbles
    if random.randint(0, 100) < 5:
        bubble_size = random.randint(5, 15)
        bubble_x = random.randint(0, 800)
        bubble_y = 600
        bubbles.append((bubble_x, bubble_y, bubble_size))
    
    # Move bubbles upward
    for i in range(len(bubbles)):
        x, y, size = bubbles[i]
        y -= 6  # Adjust the speed of bubbles here
        bubbles[i] = (x, y, size)
    
    # Draw bubbles
    for bubble_x, bubble_y, bubble_size in bubbles:
        canvas.create_oval(bubble_x, bubble_y, bubble_x + bubble_size, bubble_y + bubble_size, fill="white")
    
    root.update()

# Start moving the fish
move_fish()

# Run the Tkinter event loop
root.mainloop()
