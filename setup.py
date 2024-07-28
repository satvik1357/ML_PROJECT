from setuptools import find_packages,setup
from typing import List

hypen='-e .'
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
name='ml_project',
version='0.0.1',
author='Sai_Satvik',
author_email='saisatviksunkavalli@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)