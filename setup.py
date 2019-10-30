from setuptools import setup, find_packages

setup(
    name='python_examples',
    description='Scratch lib for simple code and test examples',
    version='0.0.1',
    author='Alex Garland',
    author_email='agarland@hotels.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[],
    extras_require={},
    packages=find_packages(exclude=['tests'])
)
