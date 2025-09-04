# Installation Guide

This document provides detailed instructions for installing fractek,
ensuring you get up and running smoothly on various platforms and
environments.

------------------------------------------------------------------------

## Requirements

-   Python 3.8 or higher
-   pip package manager

fractek relies on the following core dependencies, which are installed
automatically:

-   numpy (\>=1.19)
-   matplotlib (\>=3.4)
-   scipy (\>=1.7)
-   noise (\>=1.2.2)

------------------------------------------------------------------------

## Installing fractek

### Simple Installation (recommended)

The easiest way to install fractek is via PyPI using pip:

``` bash
pip install fractek
```

This command will download and install fractek and its dependencies
automatically.

------------------------------------------------------------------------

## Upgrading fractek

To upgrade fractek to the latest version, run:

``` bash
pip install --upgrade fractek
```

------------------------------------------------------------------------

## Installation in Different Environments

### Virtual Environment (recommended)

Using a virtual environment isolates your fractek installation and
dependencies from other Python projects.

``` bash
python -m venv fractek-venv
source fractek-venv/bin/activate # Windows: fractek-venv\Scripts\activate
pip install fractek
```

------------------------------------------------------------------------

### Google Colab

fractek is fully compatible with Google Colab. Install it by running:

``` python
!pip install fractek
```

Then, import and use fractek as usual.

> **Note:** After installing new packages in Colab notebooks, it is
> often necessary to restart the runtime to ensure imports work
> correctly.

------------------------------------------------------------------------

## Troubleshooting

### Module Not Found after installation

-   Ensure you restarted the Python environment or Jupyter kernel.
-   Check your Python environment where fractek was installed.
-   Verify the installation path:

``` python
import fractek
print(fractek.__file__)
```

### SSL or connection errors

-   Upgrade pip and certifi:

``` bash
pip install --upgrade pip certifi
```

-   Use trusted hosts option if behind a proxy:

``` bash
pip install fractek --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

For detailed issues, check our [FAQ](faq.md) or open an issue on GitHub.

------------------------------------------------------------------------

## Uninstalling fractek

Removing fractek from your system is straightforward:

``` bash
pip uninstall fractek
```

------------------------------------------------------------------------

Thank you for using fractek! If you encounter any issues related to
installation, please report them on our GitHub repository.

