python intro.py
latex intro.tex; latex intro.tex;
dvips intro.dvi
psselect -p1 intro.ps > intro1.eps
psselect -p2 intro.ps > intro2.eps

doconce2format HTML doc.do.txt
doconce2format gwiki doc.do.txt

cp doc.do.txt _tmp.do.txt

# If no images, run create_images_exampletalk.py 1
doconce2format LaTeX doc.do.txt
ptex2tex doc
subst.py '\\begin{figure}' '\\begin{figure}[ht]' doc.tex
subst.py 'amssymb' 'amssymb,float,subfigure,graphicx,lscape' doc.tex
subst.py 'documentclass' 'documentclass[a4paper]' doc.tex
latex doc.tex
if [ $? != 0 ]; then
    exit
fi
latex doc.tex
if [ $? != 0 ]; then
    exit
fi
dvipdf doc.dvi
cp doc.pdf latexslides_doc.pdf
cp doc.html latexslides_doc.html

