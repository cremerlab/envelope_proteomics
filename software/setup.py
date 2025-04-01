from setuptools import setup, find_packages
from os import path

__version__ = "0.0.01"

setup(
    name="size",
    version=__version__,
    description="Various python utilities used for studies on envelope proteome.",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    author="Griffin Chure",
    author_email="griffinchure@gmail.com",
    install_requires=[
        "matplotlib>=3.7.0",
        "numpy>=1.24.4",
        "pandas>=2.0.3",
        "scipy>=1.10.0",
        "seaborn>=0.12.2",
        "termcolor>=2.3.0",
        "tqdm>=4.64.1",]
)