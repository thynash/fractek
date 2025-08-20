import numpy as np
import matplotlib.pyplot as plt

def generate_plant_lsystem(rule='X->F+[[X]-X]-F[-FX]+X\nF->FF',
                           axiom='X', angle=25, iterations=5, length=3):
    rules_map = {}
    for line in rule.split('\n'):
        if '->' in line:
            k, v = line.split('->')
            rules_map[k] = v
    seq = axiom
    for _ in range(iterations):
        next_seq = ""
        for c in seq:
            next_seq += rules_map.get(c, c)
        seq = next_seq

    # To support branches, store lines as segment list
    segments = []
    x, y = 0.0, 0.0
    stack = []
    angle_cur = 90.0
    for cmd in seq:
        if cmd == 'F':
            x_new = x + length * np.cos(np.deg2rad(angle_cur))
            y_new = y + length * np.sin(np.deg2rad(angle_cur))
            segments.append(((x, y), (x_new, y_new)))
            x, y = x_new, y_new
        elif cmd == '+':
            angle_cur += angle
        elif cmd == '-':
            angle_cur -= angle
        elif cmd == '[':
            stack.append((x, y, angle_cur))
        elif cmd == ']':
            x, y, angle_cur = stack.pop()
    return segments, seq

def plot_plant_lsystem(segments, color='forestgreen'):
    plt.figure(figsize=(6,10))
    for (x0, y0), (x1, y1) in segments:
        plt.plot([x0, x1], [y0, y1], color=color, linewidth=1)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.title("Plant-like L-System")
    plt.show()

def info_plant_lsystem(seq):
    return {"length_steps": len(seq)}

