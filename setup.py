from setuptools import setup, find_packages

setup(
    name='synology-api',
    version='0.0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python Synology API Wrapper',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/N4S4/synology-api',
    author='Renato Visaggio',
    author_email='renatovisaggio@gmail.com'
)
