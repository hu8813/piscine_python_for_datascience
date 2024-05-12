# ft_package

A simple Python package for counting occurrences of an item in a list.

## Building the Package

python3 setup.py sdist bdist_wheel


## Installation

pip install ./dist/ft_package-0.0.1.tar.gz

or

pip install ./dist/ft_package-0.0.1-py3-none-any.whl


## To remove generated files after build

rm -rf build dist ft_package.egg-info


## Usage

from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  
print(count_in_list(["toto", "tata", "toto"], "tutu"))   
