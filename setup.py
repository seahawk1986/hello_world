#!/usr/bin/python3
from setuptools  import setup
setup(name="hello_world",
      version='0.0.1',
      py_modules=['hello_world'],
      entry_points = {
              'console_scripts': [
                  'hello_world = hello_word:print_hello_world',                  
              ],              
          },
)
