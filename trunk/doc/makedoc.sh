python intro.py
latex intro.tex; latex intro.tex;
dvips intro.dvi
#psselect -p1 intro.ps > intro1.eps
#psselect -p2 intro.ps > intro2.eps

doconce2format HTML doc.do.txt -D ADVANCED=false
doconce2format wiki doc.do.txt -D ADVANCED=false

echo '#TITLE: Latexslides tutorial\n' > _tmp.do.txt
echo '#AUTHOR: Ilmar M. Wilbers, Simula Research Laboratory, Univ. of Oslo\n' >> _tmp.do.txt
echo '#DATE: Mar 6, 2008\n' >> _tmp.do.txt
cat doc.do.txt >> _tmp.do.txt

# If no images, run create_images_exampletalk.py 1
doconce2format LaTeX _tmp.do.txt -D ADVANCED=text
preprocess -D ADVANCED=code _tmp.p.tex > _tmp2.p.tex
ptex2tex _tmp2.p.tex
mv _tmp2.tex doc.tex
if [ $? != 0 ]; then
    exit
fi
rm _tmp.p.tex
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
#scp doc.pdf ormuzd.simula.no:www_docs/latexslides
