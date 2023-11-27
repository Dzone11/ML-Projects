from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements.txt file and returns a list of required packages
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if not req.startswith('-e')]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Shahabas',
    author_email='shahabassha12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
