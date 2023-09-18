import setuptools
from setuptools import find_packages

setuptools.setup(name='mad-whatsapp',
                 version='0.1',
                 description='Parses Whatsapp conversations',
                 long_description=open('README.md').read().strip(),
                 author='Dan Dobrescu',
                 author_email='d4n.dobrescu@gmail.com',
                 url='https://github.com/dobrescu/mad-whatsapp',
                 install_requires=[],
                 license='MIT License',
                 packages=find_packages(),
                 keywords='parse whatsapp conversations',
                 classifiers=[
                    "Programming Language :: Python",
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent"
                 ])
