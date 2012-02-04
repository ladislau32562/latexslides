#!/bin/sh

# just ignore simula style error...

themes="blue1 blue2 red1 red2 cbc simula simulaold umbc1 umbc2 umbc2 umbc3 umbc4"
for theme in $themes; do
python demo.py $theme cod
ptex2tex -DMINTED tmp_themedemo
#ptex2tex tmp_themedemo
pdflatex -shell-escape tmp_themedemo
mv tmp_themedemo.pdf tmp_demo_$theme.pdf
done

echo
echo Here are the demos:
ls tmp_demo_*.pdf

