#!/bin/sh

themes="blue1 blue2 red1 red2 cbc simula simulaold umbc1 umbc2 umbc2"
for theme in $themes; do
python demo.py $theme
pdflatex demo
#ptex2tex -DMINTED tmp_themedemo
ptex2tex tmp_themedemo
pdflatex tmp_themedemo
mv tmp_themedemo.pdf tmp_demo_$theme.pdf
done
