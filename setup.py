from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='synology-api',
    version='0.6.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python Synology API Wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'appdirs',
        'click',
        'dataclass_factory',
        'requests',
        'rich',
        'urllib3',
        'setuptools'],
    url='https://github.com/N4S4/synology-api',
    author='Renato Visaggio',
    author_email='synology.python.api@gmail.com',
    entry_points={
        'console_scripts': [
            'synoapi = synology_cli.cli_webapi:main',
            'synocli = synology_cli.cli:main',
            'synophotos = synology_cli.cli_photos:main',
        ],
    }
)
