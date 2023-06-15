from setuptools import setup, find_packages

setup(
    name='two-factor-auth',
    version='1.0',
    description='Django two-step authentication app.',
    author='Pkfilho95',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
)
