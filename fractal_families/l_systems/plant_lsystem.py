import numpy as np
import matplotlib.pyplot as plt

def generate_plant_lsystem(rule='X->F+[[X]-X]-F[-FX]+X\nF->FF', axiom='X', angle=25, iterations=5, length=3):
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
    x, y, stack, angle_cur = [0], , [], 90
    for cmd in seq:
        if cmd == 'F':
            x.append(x[-1] + length*np.cos(np.deg2rad(angle_cur)))
            y.append(y[-1] + length*np.sin(np.deg2rad(angle_cur)))
        elif cmd == '+':
            angle_cur += angle
        elif cmd == '-':
            angle_cur -= angle
        elif cmd == '[':
            stack.append((x[-1], y[-1], angle_cur))
        elif cmd == ']':
            x0,y0,a0 = stack.pop()
            x.append(x0); y.append(y0); angle_cur=a0
    return np.array(x), np.array(y)

def plot_plant_lsystem(x, y, ax=None, color='green'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_title("Plant-like L-system")
    plt.show()

def info_plant_lsystem(seq):
    return {"length_steps": len(seq)}

