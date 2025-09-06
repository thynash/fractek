# Contributing to Fractek

Thank you for your interest in contributing to Fractek! We welcome contributions from mathematicians, developers, artists, and anyone passionate about fractal geometry. This guide will help you get started and ensure your contributions align with our project goals.

---

## 🌟 Ways to Contribute

### Code Contributions
- **New fractal algorithms** and mathematical implementations
- **Performance optimizations** and algorithm improvements
- **Visualization enhancements** and new plotting features
- **Bug fixes** and stability improvements
- **Documentation improvements** and code examples

### Non-Code Contributions
- **Mathematical validation** and accuracy testing
- **Documentation writing** and tutorial creation
- **Example galleries** and use case demonstrations
- **Bug reporting** and issue reproduction
- **Feature requests** and design discussions

---

## 🚀 Getting Started

### 1. Development Setup

Fork and clone the repository
git clone https://github.com/thynash/fractek.git
cd fractek

Create a development environment
python -m venv fractek-dev
source fractek-dev/bin/activate # Windows: fractek-dev\Scripts\activate

Install in development mode with test dependencies
pip install -e .[dev]

Verify installation
python -c "import fractek; print(fractek.version)"


### 2. Development Dependencies

pip install -r requirements-dev.txt

This includes:
- `pytest` - Testing framework
- `black` - Code formatting
- `flake8` - Code linting
- `mypy` - Type checking
- `sphinx` - Documentation generation
- `jupyter` - Interactive development and examples

---

## 📝 Development Workflow

### 1. Create a Feature Branch

git checkout -b feature/your-feature-name

### 2. Make Your Changes

Follow these guidelines:
- Write clear, descriptive commit messages
- Keep changes focused and atomic
- Add tests for new functionality
- Update documentation as needed
- Follow our coding standards (see below)

### 3. Test Your Changes

Run the full test suite
pytest

Run specific test categories
pytest tests/test_fractals.py
pytest tests/test_noise.py
pytest tests/test_visualization.py

Check code formatting
black --check .
flake8 .

Type checking
mypy fractek/


### 4. Submit a Pull Request

1. Push your changes to your fork
2. Create a pull request with a clear title and description
3. Link any related issues
4. Wait for review and address feedback

---

## 🎯 Coding Standards

### Code Style

We use **Black** for code formatting and **flake8** for linting:

Format code
black .

Check linting
flake8 .



### Key Principles

- **Readability first**: Code should be self-documenting
- **Mathematical accuracy**: Implement algorithms faithfully to mathematical definitions
- **Performance awareness**: Consider computational complexity and memory usage
- **Modular design**: Keep functions focused and classes cohesive
- **Error handling**: Provide clear error messages and handle edge cases

### Documentation Standards

- **Docstrings**: Use Google-style docstrings for all public functions and classes
- **Type hints**: Include type annotations for function parameters and returns
- **Examples**: Provide usage examples in docstrings where helpful


---

## 🧪 Testing Guidelines

### Test Structure

- Place tests in the `tests/` directory
- Mirror the package structure: `tests/test_fractals.py` for `fractek/fractals.py`
- Use descriptive test names: `test_mandelbrot_set_generates_correct_shape()`

### Test Categories

Unit tests - test individual functions
def test_mandelbrot_point_calculation():
"""Test Mandelbrot iteration for a single point."""

Integration tests - test module interactions
def test_fractal_visualization_pipeline():
"""Test complete fractal generation and visualization."""

Mathematical validation tests
def test_hausdorff_dimension_known_fractals():
"""Test dimension calculation against known theoretical values."""


### Writing Good Tests

- **Test edge cases**: Empty inputs, boundary conditions, extreme values
- **Validate mathematical properties**: Known theoretical results, symmetries
- **Use fixtures**: Share setup code between related tests
- **Assert with precision**: Use appropriate tolerances for floating-point comparisons

import pytest
import numpy as np

def test_koch_snowflake_area_convergence():
"""Test that Koch snowflake area converges to expected value."""
snowflake = koch_snowflake(iterations=10)
expected_area = (2 * np.sqrt(3) / 5) * (initial_triangle_area)

assert abs(snowflake.area - expected_area) < 1e-10

---

## 📚 Documentation Guidelines

### Writing Documentation

- **Clear and concise**: Explain concepts without unnecessary jargon
- **Visual examples**: Include fractal images and plots where relevant
- **Mathematical context**: Provide theoretical background when helpful
- **Code examples**: Show practical usage with expected outputs
   
---

## 🐛 Reporting Issues

### Bug Reports

Include the following information:
- **Fractek version** and Python version
- **Operating system** and environment details
- **Minimal code example** that reproduces the issue
- **Expected vs. actual behavior**
- **Error messages** and stack traces (if any)

### Feature Requests

- **Clear description** of the proposed feature
- **Use case explanation** - why would this be useful?
- **Mathematical background** (for algorithm requests)
- **Implementation ideas** (if you have them)

---

## 🏆 Recognition

Contributors who make significant contributions will be:

- **Acknowledged** in the project README and documentation
- **Listed** in the contributors file
- **Credited** in release notes for major contributions
- **Invited** to join the core maintainer team (for sustained contributors)

---

## 📞 Communication

### Getting Help

- **GitHub Discussions**: Ask questions and discuss ideas
- **GitHub Issues**: Report bugs and request features  
- **Email**: Contact maintainer at [pantnityansh@gmail.com](mailto:pantnityansh@gmail.com)

### Code Review Process

- All pull requests require review before merging
- Focus on constructive feedback and learning
- Reviewers will check: code quality, tests, documentation, mathematical accuracy
- Be patient and responsive to feedback

---

## 📋 Contribution Checklist

Before submitting a pull request:

- [ ] Code follows project style guidelines (Black formatting, flake8 compliance)
- [ ] All tests pass locally (`pytest`)
- [ ] New functionality includes appropriate tests
- [ ] Documentation is updated (docstrings, tutorials if needed)
- [ ] Mathematical implementations are accurate and well-commented
- [ ] Commit messages are clear and descriptive
- [ ] Pull request description explains the changes and rationale

---

## 📜 License

By contributing to Fractek, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

---

**Thank you for helping make Fractek the world's best fractal mathematics library! 🌟**

*"In mathematics you don't understand things. You just get used to them."* — **John von Neumann**

