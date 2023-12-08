from setuptools import setup, find_packages

setup(
    name="wlgen-lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "simpy",
        "loguru",
        "omegaconf",
        "numpy",
        "setuptools",
    ],
)
