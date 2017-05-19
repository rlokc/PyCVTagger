#from distutils.core import setup
#import py2exe
#setup(console=['tagger.py'])

import sys
from cx_Freeze import setup, Executable

build_exe_option = {"packages": ["lxml"], "includes": ["lxml", "lxml.etree", "lxml._elementpath", "lxml.ElementInclude"]}

setup( name = "CVTagger",
       version = "0.1",
       description = "Image tagger via Clarifai",
       options = {"build_exe": build_exe_option},
       executables = [Executable("tagger.py")])
