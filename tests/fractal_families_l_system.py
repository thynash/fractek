from fractek.fractal_families.l_systems.koch_snowflake import generate_koch_snowflake, plot_koch_snowflake

vtx = generate_koch_snowflake(order=4)
plot_koch_snowflake(vtx)
from fractek.fractal_families.l_systems.dragon_curve import generate_dragon_curve, plot_dragon_curve

x, y = generate_dragon_curve(order=10)
plot_dragon_curve(x, y)
from fractek.fractal_families.l_systems.hilbert_curve import generate_hilbert_curve, plot_hilbert_curve

x, y = generate_hilbert_curve(order=5)
plot_hilbert_curve(x, y)
from fractek.fractal_families.l_systems.binary_tree import generate_binary_tree, plot_binary_tree

coords = generate_binary_tree(order=6)
plot_binary_tree(coords)
from fractek.fractal_families.l_systems.peano_curve import generate_peano_curve, plot_peano_curve

x, y = generate_peano_curve(order=2)
plot_peano_curve(x, y)
from fractek.fractal_families.l_systems.sierpinski_arrowhead import generate_sierpinski_arrowhead, plot_sierpinski_arrowhead

x, y = generate_sierpinski_arrowhead(order=6)
plot_sierpinski_arrowhead(x, y)
from fractek.fractal_families.l_systems.terdragon_curve import generate_terdragon_curve, plot_terdragon_curve

x, y = generate_terdragon_curve(order=8)
plot_terdragon_curve(x, y)
from fractek.fractal_families.l_systems.minkowski_sausage import generate_minkowski_sausage, plot_minkowski_sausage

x, y = generate_minkowski_sausage(order=3)
plot_minkowski_sausage(x, y)

from fractek.fractal_families.l_systems.mandelbrot_l_system import generate_mandelbrot_l_system, plot_mandelbrot_l_system
x, y, seq = generate_mandelbrot_l_system(axiom="A", rules={"A": "AB", "B": "A"}, iterations=7, step=5, angle=90)
plot_mandelbrot_l_system(x, y)

from fractek.fractal_families.l_systems.plant_lsystem import generate_plant_lsystem, plot_plant_lsystem
segments, seq = generate_plant_lsystem()
plot_plant_lsystem(segments)
