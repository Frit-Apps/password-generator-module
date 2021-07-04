from setuptools import setup, find_packages

__version__ = '0.3.0'

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name="password-generator-module",
    version=__version__,
    description="Generate strong passwords quickly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mazzya",
    author_mail="whissan01@gmail.com",
    license="MIT",
    url="https://github.com/Mazzya/password-generator-module",
    packages=find_packages(),
    keywords=['python', 'password'],
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
        "Topic :: Software Development :: Version Control :: Git",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Unix"
    ]
)