from setuptools import setup, find_packages

setup(
    name='synology-api',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python Synology API Wrapper',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/emelbaer/synology-api',
    author='Emel B (c) Renato Visaggio',
    author_email=''
)
