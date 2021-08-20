"""
projectname setup
==================================

Author: Casokaks (https://github.com/Casokaks/)
Created on: Aug 15th 2021

"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
#import os
#key = os.environ['GITHUB_TOKEN']
from setuptools import setup, find_packages
setup(
    name='projectname',
    version='0.3.1',
    author='Casokaks',
    author_email='casokaks@gmail.com',
    description='Light python template.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Casokaks/light-python-template',
    project_urls = {
        "Bug Tracker": "https://github.com/Casokaks/light-python-template/issues"
    },
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Standard python packages:
        #'package',
        # Public github repository:
        #'<reponame> @ git+https://github.com/<username>/<reponame>@main',        
        # Private github repository:
        #'reponame @ git+https://{key}@github.com/username/reponame@main'.format(key=key),
    ], 
)
