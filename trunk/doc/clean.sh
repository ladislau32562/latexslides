#!/bin/sh
files="*.pyc *.aux *.dvi *.html *.log *.out doc.pdf doc.tex intro.tex *.nav intro.ps *.snm *.toc *.vrb _tmp* tmp* *~ doc.p.tex doc.gwiki doc.txt doc.idx tmp_*"
echo "Removing:"
ls $files 2> /dev/null
rm -rf $files
