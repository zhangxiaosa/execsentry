from setuptools import setup, find_packages

setup(
    name='execsentry',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'execsentry = execsentry.main:main',
        ],
    },
)

