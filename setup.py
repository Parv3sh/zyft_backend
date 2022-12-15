#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "beautifulsoup4==4.11.1",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Parvesh Kumar",
    author_email="parveshk2@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Take home challenge.",
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="zyft_backend",
    name="zyft_backend",
    packages=find_packages(include=["zyft_backend", "zyft_backend.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Parv3sh/zyft_backend",
    version="0.1.0",
    zip_safe=False,
)
