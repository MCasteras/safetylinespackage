from distutils.core import setup

setup(
  name = 'safetylinespackage',         # How you named your package folder (MyLib)
  packages = ['safetylinespackage'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'package for safetylines test',   # Give a short description about your library
  author = 'Mathieu Casteras',                   # Type in your name
  author_email = 'mathieu.casteras@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/MCasteras/safetylinespackage',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/MCasteras/safetylinespackage/archive/0.5.tar.gz',    # I explain this later on
  keywords = ['safetylines', 'ML', 'TEST'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'sklearn',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',#Specify which pyhton versions that you want to support
  ],
)