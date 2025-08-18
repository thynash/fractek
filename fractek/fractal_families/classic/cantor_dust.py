import numpy as np
import matplotlib.pyplot as plt

def generate_cantor_dust(order=4, x=0, y=0, size=1):
    squares = [(x, y, size)]
    for _ in range(order):
        new_squares = []
        for (x, y, size) in squares:
            step = size / 3
            for dx in [0, 2]: # 0, 2 keeps only the square in left or right
                for dy in [0, 2]:
                    new_squares.append((x + dx*step, y + dy*step, step))
        squares = new_squares
    return squares

def plot_cantor_dust(squares):
    plt.figure()
    for (x, y, size) in squares:
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color='navy', alpha=0.7))
    plt.axis('equal')
    plt.axis('off')
    plt.title("Cantor Dust")
    plt.show()

def info_cantor_dust(order):
    count = 4**order
    return {'order': order, 'num_squares': count}

