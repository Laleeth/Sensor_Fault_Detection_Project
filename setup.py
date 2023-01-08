from setuptools import find_packages, setup
from typing import List

""" This function returns the list of requirement.txt"""


def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    return requirement_list


setup(
    name="sensor",
    version="0.0.8",
    author="lalith",
    author_email="thomalalalithsai@gmail.com",
    packages=find_packages(),
    install_requires=[],
)
