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
        "requests==2.31.0",
        "openapi-core==0.19.1",
    ],
    tests_require=[
        "pytest==8.2.0",
    ]
)