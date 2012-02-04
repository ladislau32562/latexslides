#!/bin/sh

# Copies beamer/latex style files and other required files to
# ~/texmf/tex/latex/misc on a Linux machine

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

