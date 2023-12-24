from setuptools import setup, find_packages

setup(
    name='cmdwrapper',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cmdwrapper = cmdwrapper.main:main',
        ],
    },
    # 其他可选信息，如作者、许可证、描述等
)

