from setuptools import find_packages, setup
from typing import List


requirement_list:List[str]	=[]
def get_requirements() -> List[str]:
    try:
        with open("requirements.txt",'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirements.txt not found')

    return requirement_list

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Murillo Lécio",
    author_email = "leciopmurillo@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
        