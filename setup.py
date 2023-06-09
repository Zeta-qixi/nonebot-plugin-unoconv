#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
requirements = [r.strip() for r in open("requirements.txt", 'r', encoding='utf-8').readlines()]

setup(
    name='nonebot-plugin-unoconv',
    version='0.5.7',
    author='Zeta',
    author_email='',
    long_description="https://github.com/Zeta-qixi/nonebot-plugin-unoconv",
    license="MIT Licence",
    url='https://github.com/Zeta-qixi/nonebot-plugin-unoconv/',
    description='nonebot_plugin about use unoconv',
    packages=['nonebot_plugin_unoconv'],
    install_requires=requirements,

)
