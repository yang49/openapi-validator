from setuptools import setup, find_packages

setup(
    name='openapi-validator',
    version='0.0.1',
    packages=find_packages(),
    license='Your License',
    author='Yang Li',
    description='Short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "requests==2.26.0",
    ],
    tests_require=[
        "pytest==6.2.5",
    ]
)