# setup.py file is basically to convert your whole project into a package that is available at Pypi for users to download and use.

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path) -> List[str]:
    '''
    This function will return a list of requirements
    
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

    




# following can be said to be metadata of the project
setup(
    name='mlproject',
    version= '0.0.1',
    author= 'Aman',
    author_email= 'amandeep1552@gmail.com',
    packages=find_packages(), # this looks for "__init__.py" files in all the folders and build those folders as packages
    install_requires= get_requirements('requirements.txt'), # this parameter is basically what packages this project will require to install when installing this project as a package



)