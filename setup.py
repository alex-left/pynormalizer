#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='pynormalizer',
    description='Normalize filenames replacing conflictive characters',
    author='Alex Left',
    author_email='alejandro.izquierdo.b@gmail.com',
    url='https://github.com/alex-left/pynormalizer',
    version='0.2',
    scripts=['pynormalizer'],
    license='GPL-v3',
    long_description=open('README.md').read(),
)
