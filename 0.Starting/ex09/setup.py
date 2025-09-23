from setuptools import setup, find_packages

setup(
    name="ft_package_janeway",
    version="0.0.1",
    author="janeway",
    author_email="janeway@example.com",
    description="A small example package",
    readme="README.md",
    packages=find_packages(),
    license="MIT",
    url="https://github.com/janeway/ft_package",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ]
)