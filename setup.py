from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read line from file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty line and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Abhishek Shroff",
    author_email="abhishekshroff1802@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)