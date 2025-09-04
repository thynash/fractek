# fractek — Modular Fractal Mathematics, Visualization, and Analysis Library

Welcome to **fractek**, a world-class Python library that offers a comprehensive, modular toolkit for generating, visualizing, and analyzing fractals and fractal noise. Designed with scientific rigor and creative flexibility, fractek empowers researchers, developers, and artists to explore the fascinating universe of fractals with ease and power.

### Why fractek?

Fractals lie at the intersection of mathematics, nature, and art, revealing complex patterns from simple rules. fractek brings cutting-edge fractal mathematics algorithms and visualization capabilities together in one unified, extensible platform:

* Generate classic fractal sets like Mandelbrot and Julia with customizable parameters.
* Create fractal noise textures that simulate natural phenomena.
* Perform fractal dimension and multifractal spectrum analyses.
* Visualize results in interactive and publication-quality plots.
* Modular design allows easy extension with new fractal families or analysis methods.

---

### Installation

Install fractek effortlessly via pip:

```bash
pip install fractek
```

Supports Python 3.8 and above.

---

### Quickstart Example

```python
import fractek
from fractek.fractal_families.classic import mandelbrot

# Generate a Mandelbrot set image
mandel = mandelbrot.mandelbrot_set(xmin=-2, xmax=1, ymin=-1.5, ymax=1.5, width=256, height=256, max_iter=50)
print(mandel)  # NumPy array representing iterations
```

Explore various fractal families, noise generators, and visualization tools through an intuitive API.

---

### Core Modules and Features

* **fractal_families:** Classic and novel fractal generators such as Mandelbrot, Julia, Burning Ship, and more.
* **noise:** Fractal noise algorithms useful for texture synthesis and modeling natural randomness.
* **visualization:** Plotting utilities built on Matplotlib for detailed fractal visuals with zoom and coloring options.
* **dimension:** Tools for fractal dimension estimation and multifractal analysis.

---

### Documentation and Resources

* Installation Guide
* User Tutorials and Examples
* API Reference

For more information and to contribute, visit our GitHub repository:
[https://github.com/thynash/fractek](https://github.com/thynash/fractek)

---

### Contributing

fractek is open-source and welcomes contributions from the community. Please see `contributing.md` for guidelines on how to report issues, request features, and submit pull requests.

---

### License

fractek is licensed under the MIT License. See the `LICENSE` file for details.

