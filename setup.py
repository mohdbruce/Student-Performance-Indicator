from setuptools import find_packages, setup
from typing import List

HYPEN_REQUIREMENT = '-e .'
def get_requires(file_path:str)->List[str]:
    """
    This function returns a list of requirements from a given file.
    :param file_path: Path to the requirements file
    :return: List of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_REQUIREMENT in requirements:
            requirements.remove(HYPEN_REQUIREMENT)
    
    return requirements


setup(
    name='StudentPerformanceIndicator',
    version='0.1',
    author='Mohd Bruce',
    author_email='mohdbrucelee@gmail.com',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt')
)

