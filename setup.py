from setuptools import setup, find_packages

setup(
    name="my_custom_module",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
    ],
)
