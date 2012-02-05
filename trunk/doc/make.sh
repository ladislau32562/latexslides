#!/bin/sh

python exampletalk.py
ptex2tex -DMINTED tmp_exampletalk
latex -shell-escape tmp_exampletalk
dvipdf tmp_exampletalk
mv tmp_exampletalk.pdf exampletalk.pdf

python intro.py
ptex2tex intro
latex intro
dvips intro
psselect -p1 intro.ps > intro1.eps
psselect -p2 intro.ps > intro2.eps

doconce format HTML doc.do.txt
doconce format gwiki doc.do.txt
doconce subst '\(the URL of the image file intro1.png must be inserted here\)' 'https://latexslides.googlecode.com/svn/trunk/doc/intro1.png' doc.gwiki
doconce subst '\(the URL of the image file intro2.png must be inserted here\)' 'https://latexslides.googlecode.com/svn/trunk/doc/intro2.png' doc.gwiki

cp doc.do.txt _tmp.do.txt

# If no images, run create_images_exampletalk.py 1
doconce format latex doc.do.txt
ptex2tex -DLATEX_HEADING=traditional doc
doconce subst '\\begin{figure}' '\\begin{figure}[ht]' doc.tex
doconce replace 'amssymb' 'amssymb,float,subfigure,graphicx,lscape' doc.tex
doconce replace 'documentclass' 'documentclass[a4paper]' doc.tex
latex doc
if [ $? != 0 ]; then
    exit
fi
latex doc.tex
if [ $? != 0 ]; then
    exit
fi
dvipdf doc
cp doc.pdf latexslides_doc.pdf
cp doc.html latexslides_doc.html

