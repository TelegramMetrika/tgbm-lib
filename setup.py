#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tgbm_lib',
    description='Aiogram bot metrika.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.0.1',
    url='https://github.com/TelegramMetrika/tgbm-lib',
    author='vsecoder',
    author_email='kreepmeister@yandex.ru',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(include=['tgbm-lib', 'tgbm-lib.*']),
    install_requires=[
        'aiogram<3',
    ],
    python_requires=">=3.6",
)