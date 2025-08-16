import numpy as np
import matplotlib.pyplot as plt

def generate_box_fractal(order=3, x=0.5, y=0.5, size=0.5):
    squares = [(x, y, size)]
    for _ in range(order):
        new_squares = []
        for (x, y, size) in squares:
            half = size / 3
            for dx, dy in [(-half, -half), (-half, half), (half, -half), (half, half)]:
                new_squares.append((x+dx, y+dy, half))
        squares = new_squares
    return squares

def plot_box_fractal(squares):
    plt.figure()
    for (x, y, size) in squares:
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, fill=None, edgecolor='brown'))
    plt.axis('equal')
    plt.axis('off')
    plt.title("Box Fractal")
    plt.show()

def info_box_fractal(order):
    return {'order': order, 'squares': 4**order}

