"""Setup configuration for Quantum Project 1."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quantum-project1',
    version='1.0.0',
    author='Quantum Project Team',
    author_email='martinlutherupa1@gmail.com',
    description='A comprehensive quantum computing library using Qiskit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/elon00/Quantum-Project1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=[
        'qiskit>=1.0.0',
        'qiskit-aer>=0.13.0',
        'numpy>=1.24.0',
        'matplotlib>=3.7.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.7.0',
            'flake8>=6.1.0',
            'mypy>=1.5.0',
            'pylint>=2.17.0',
        ],
        'docs': [
            'sphinx>=7.1.0',
            'sphinx-rtd-theme>=1.3.0',
        ],
        'jupyter': [
            'jupyter>=1.0.0',
            'ipykernel>=6.25.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'quantum-sim=examples.basic_usage:main',
        ],
    },
    keywords='quantum computing qiskit quantum-gates quantum-circuits simulation',
    project_urls={
        'Bug Reports': 'https://github.com/elon00/Quantum-Project1/issues',
        'Source': 'https://github.com/elon00/Quantum-Project1',
        'Documentation': 'https://github.com/elon00/Quantum-Project1#readme',
    },
)