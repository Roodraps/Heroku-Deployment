from setuptools import setup
from typing import List

# declaring variables for setup function
PROJECT_NAME = "housing-prediction"
VERSION = "0.0.1"
AUTHOR = "Roodra pratap singh parihar"
DESCRIPTION = "machine learning project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    description : this function going to return list of requirements
    mentioned in the requirements.txt file

    return this function going to return the list which contained name of the libraries mentioned in the requirements.txt 
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

    
    if __name__ == "__main__":
        print(get_requirements_list())


setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = PACKAGES,
install_requires = get_requirements_list()
)     