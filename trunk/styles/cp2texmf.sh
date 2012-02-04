#!/bin/sh

# Copies *all* beamer/latex style files and other required files to
# ~/texmf/tex/latex/misc on a Linux machine
# (setup.py copies the red1, red2, blue1 and blue2 styles, but not
# the special cbc, simula, hpl, umbc styles)

dir=$HOME/texmf/tex/latex/misc
if [ ! -d $dir ]; then
    mkdir -p $dir
fi

cp *.sty *.pdf *.eps $dir
cd hpl; cp *.sty *.pdf *.eps $dir
cd ../cbc/beamer; cp *.sty *.pdf *.eps $dir
cd ../math.umbc.edu-beamer; cp *.sty *.pdf *.eps $dir

# update tex style files
cd $HOME/texmf
mktexlsr .

