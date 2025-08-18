from setuptools import setup, find_packages

setup(
    name='fractek',
    version='0.1.0',
    description='A world-class modular fractal mathematics, visualization, and analysis library',
    author='Nityansh Pant',
    author_email='pantnityansh@gmail.com',
    url='https://github.com/thynash/fractek',
    packages=find_packages(where="fractek"),  # <-- look in ./fractek for packages
    package_dir={"": "fractek"},              # <-- root package source is in ./fractek
    install_requires=[
        'numpy>=1.19',
        'matplotlib>=3.4',
        'scipy>=1.7',
        'noise>=1.2.2',
        # 'pytest>=6.2',  # Only needed for development, not install_requires for end users
        # Add 'plotly', 'pywt', 'scikit-learn', 'torch', etc. if needed
    ],
    python_requires='>=3.8',
    include_package_data=True,
    license='MIT',
    keywords='fractal mathematics visualization analysis dimensional fractal-noise',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)

