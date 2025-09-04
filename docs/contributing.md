# Contributing to fractek

Thank you for your interest in contributing to fractek! Your
contributions help make fractek better for everyone. This document
outlines guidelines and best practices for contributing code, reporting
issues, and suggesting features.

------------------------------------------------------------------------

## How to Contribute

### 1. Reporting Issues

If you find a bug or want to request a feature:

-   Check existing [issues](https://github.com/thynash/fractek/issues)
    to avoid duplicates.
-   Open a new issue with a clear title and detailed description.
-   Include steps to reproduce the issue, expected behavior, and your
    environment details.

------------------------------------------------------------------------

### 2. Submitting Code Contributions

We welcome code contributions via pull requests (PRs).

#### Steps to contribute code:

1.  **Fork the repository** on GitHub.
2.  **Clone your forked repo** locally:

``` bash
git clone https://github.com/<your-username>/fractek.git
cd fractek
```

3.  **Create a feature branch**:

``` bash
git checkout -b feature/your-feature-name
```

4.  **Make your changes and commit them**:

-   Follow the existing code style and conventions.
-   Write clear, concise commit messages.

5.  **Test your changes** locally.

6.  **Push your branch** to GitHub:

``` bash
git push origin feature/your-feature-name
```

7.  **Open a pull request** on the original `thynash/fractek`
    repository.
8.  Engage in discussion and make requested changes as needed.

------------------------------------------------------------------------

### 3. Code Style and Testing

-   Follow PEP 8 style guidelines.
-   Include unit tests for new features or bug fixes.
-   Run tests locally before submitting PRs.
-   We recommend using `pytest` for running tests.

------------------------------------------------------------------------

### 4. Development Environment Setup

To set up a local development environment:

``` bash
python -m venv env
source env/bin/activate # Windows: env\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

------------------------------------------------------------------------

### 5. Branching and Versioning

-   Work on feature branches named clearly (e.g.,
    `feature/add-julia-set`).
-   Pull requests should target the `main` branch.
-   Versioning follows [Semantic Versioning](https://semver.org/).

------------------------------------------------------------------------

### 6. Code of Conduct

Please adhere to the [Contributor Covenant Code of
Conduct](CODE_OF_CONDUCT.md) to foster an open and welcoming community.

------------------------------------------------------------------------

## Thank You!

Your contributions are invaluable in making fractek better. We
appreciate your time and effort!

For questions or help, reach out via GitHub discussions or the issue
tracker.

