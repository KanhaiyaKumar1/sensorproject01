from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    return requirements    

    if HYPEN_E_DOT in requirements:
        requrement.remove(HYPEN_E_DOT)

setup(
    name='Fault detection',
    version='0.0.1',
    author='Kanhaiya',
    author_mail='patelkanhaiya.4523@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()

)