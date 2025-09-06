# Fractek - Advanced Fractal Mathematics & Visualization Library

## Welcome to Fractek

Fractek is a comprehensive Python library that brings the mesmerizing world of fractals to your fingertips. Whether you're a mathematician exploring self-similar structures, a data scientist seeking fractal analysis tools, or an artist creating stunning generative visuals, Fractek provides the mathematical foundation and visualization capabilities you need.

Built with modern Python practices and designed for both beginners and experts, Fractek transforms complex fractal mathematics into intuitive, accessible tools that unlock the infinite beauty and practical applications of fractal geometry.

## What Are Fractals?

Fractals are mathematical sets that exhibit self-similarity at every scale - patterns that repeat themselves infinitely as you zoom in or out. Found everywhere in nature from coastlines and clouds to blood vessels and lightning, fractals bridge the gap between mathematics and the organic world. They're characterized by:

- **Self-similarity**: Similar patterns at all scales
- **Infinite complexity**: Boundless detail at every magnification
- **Fractional dimensions**: Geometric dimensions between integers
- **Mathematical beauty**: Stunning visual patterns from simple equations

## Features

### 🎨 Fractal Generation
- **Classic Fractals**: Mandelbrot sets, Julia sets, Sierpinski carpets, Koch curves
- **L-System Fractals**: Dragon curves, Hilbert curves, tree-like structures  
- **Stochastic Fractals**: Perlin noise-based landscapes, plasma fractals
- **Custom Fractals**: Build your own fractal generators with extensible framework

### 📊 Analysis & Computation
- **Dimensional Analysis**: Hausdorff dimension, box-counting methods, lacunarity
- **Fractal Metrics**: Statistical measures and complexity analysis
- **Performance Optimized**: Vectorized NumPy operations for fast computation
- **Memory Efficient**: Smart algorithms for large-scale fractal generation

### 🎯 Visualization
- **Interactive Plotting**: Matplotlib integration with zoom and exploration tools
- **Color Mapping**: Customizable color schemes and gradient mappings
- **Export Options**: High-resolution images, animations, and data formats
- **Real-time Generation**: Live parameter adjustment and visualization

### 🔧 Scientific Tools
- **Noise Generation**: Multi-octave Perlin noise, fractional Brownian motion
- **Pattern Recognition**: Fractal analysis of real-world data
- **Educational Resources**: Examples and tutorials for learning fractal mathematics

## Quick Start

Get started with Fractek in just a few lines:

import fractek
from fractek.fractal_families.classic import mandelbrot
from fractek.visualization import plot_fractal

Generate a Mandelbrot set
mandel = mandelbrot.mandelbrot_set(-2, 1, -1.5, 1.5, 800, 600, max_iter=100)

Visualize with custom colormap
plot_fractal(mandel, colormap='hot', title='Mandelbrot Set')

Analyze fractal properties
from fractek.dimension_calculations import hausdorff_dimension
dimension = hausdorff_dimension(mandel)
print(f"Estimated fractal dimension: {dimension}")



## Installation

Install Fractek from PyPI:

pip install fractek



Or for the latest development version:

git clone https://github.com/thynash/fractek.git
cd fractek
pip install -e .



## Requirements

- Python 3.8+
- NumPy >= 1.19
- Matplotlib >= 3.4
- SciPy >= 1.7

## Community & Support

- **Documentation**: Comprehensive guides and API reference
- **Examples**: Jupyter notebooks with step-by-step tutorials  
- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: Community Q&A and showcase gallery

## License

Fractek is released under the MIT License. See LICENSE file for details.

---

*Explore the infinite. Visualize the impossible. Create with mathematics.*
