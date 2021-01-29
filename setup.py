import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='PyVMwareAirWatch',
    version='1.0.3',
    description=('PyVMwareAirWatch is a Python API library for '
                 '[VMware AirWatch] (https://www.air-watch.com/) 9.1+'),
    url='https://github.com/jprichards/PyVMwareAirWatch',
    author='jprichards',
    author_email='jprichards@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
