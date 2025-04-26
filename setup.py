"""
Setup script for the Baseball Stats project.
"""
from setuptools import setup, find_packages

setup(
    name='baseball_stats',
    version='0.1.0',
    description=' Simple package to fetch Mlb Games',
    author='Scott Stefanoski',
    author_email='scottstefanoski@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas'
    ],
    python_requires='>=3.8',
)
