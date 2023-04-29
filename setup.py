from setuptools import find_packages, setup
from typing import List

var = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    it will rwtrun list of requirements
    '''
    with open (file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [line.replace("\n", "") for line in requirement] 

        if var in requirement:
            requirement.remove(var)

    return requirement



setup(
    
name = 'mlproject',
version = '0.0.1',
author = "Baidya",
author_email = "baidyanathsa@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)