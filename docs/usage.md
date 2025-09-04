Usage Examples Get started quickly with fractek using these example
snippets.

Basic Mandelbrot Set Generation

``` python
import fractek
from fractek.fractal_families.classic import mandelbrot

mandel = mandelbrot.mandelbrot_set(
    xmin=-2, xmax=1,
    ymin=-1.5, ymax=1.5,
    width=256, height=256,
    max_iter=50
)

print(mandel)  # NumPy array with iteration counts
```

Visualizing the Mandelbrot Set

``` python
import matplotlib.pyplot as plt

plt.imshow(mandel, cmap='hot', extent=(-2, 1, -1.5, 1.5))
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
```

Using Fractal Noise

``` python
from fractek.noise import fractal_noise

noise = fractal_noise(shape=(256, 256), octaves=5, persistence=0.6)
plt.imshow(noise, cmap='gray')
plt.title('Fractal Noise')
plt.show()
```

Calculating Fractal Dimension

``` python
from fractek.dimension import box_counting_dimension

dimension = box_counting_dimension(mandel)
print(f"Estimated box-counting fractal dimension: {dimension}")
```

