import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='safetylinespackage',
     version='0.1',
     scripts=['safetylinespackage'] ,
     author="Mathieu Casteras",
     author_email="mathieu.casteras@gmail.com",
     description="a package for safetylines test",
     long_description_content_type='',
     #long_description=long_description,


     url="https://github.com/lcetinsoy/tech-debt",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.5",
         "Operating System :: OS Independent",
     ],
     install_requires=['sklearn', 'numpy','json'],

 )