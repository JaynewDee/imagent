
from setuptools import setup, find_packages


setup(name='imagent',
      version='0.1.0',
      description='_',
      author='Joshua Newell Diehl',
      author_email='jdiehl2236@gmail.com',
      url='_',
      install_requires=[
          'Click',
          'opencv-python',

      ],
      packages=find_packages(),
      include_package_data=True,
      keywords=['utility', 'images', 'editing']
      )
