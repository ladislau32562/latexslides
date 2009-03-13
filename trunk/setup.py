#!/usr/bin/env python

"""Distutils setup script for 'latexslides'."""

import sys, os, shutil, glob
from distutils.core import setup
# setuptools not a good idea because of style files

name = 'latexslides'
styles = os.path.join('styles', '*.sty')
styles_files = glob.glob(styles)

# The next line should probably have a Windows alternative:
styles_dir = os.path.join('share', 'texmf', 'tex', 'latex', name)

data_files = [(styles_dir, styles_files)]

out = setup(name=name,
            #dry_run=True,
            version="0.3",
            description="A package for writing slides using Python",
            author="Ilmar M. Wilbers",
            author_email="ilmarw@simula.no",
            url="http://latexslides.googlecode.com",
            license="BSD",
            platforms=["Linux", "Mac OSX", "Unix", "Windows"],
            package_dir={'':'lib'},            
            packages = ['latexslides'],
            keywords=["latexslides", "beamer", "prosper"],
            data_files=data_files,
            scripts=[os.path.join("bin", "latexslides"),
                     os.path.join("bin", "extract_slidenames"),
                     os.path.join("bin", "create_slidenames"),
                     os.path.join("bin", "pdf2odp"),
                     ],
            )

try:
    install_data = out.get_command_obj('install').install_data
    if install_data:
        print '\n*** LaTeX style files are located in:'
        print '    %s' %(os.path.join(install_data, styles_dir))
        print '    Please make sure the latex command can'
        print '    locate them, see the README file.'
except:
    print '\n*** Please make sure the latex command can locate'
    print '    the LaTeX style files, see the README file.'
    
