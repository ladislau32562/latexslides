#!/usr/bin/env python
# -*- coding: latin-1 -*-
"""Example presentation using latexslides."""

from latexslides import *

# Set institutions
sim, uio = "Simula Research Laboratory", "Department of Latexslides"

# Set authors
authors = [("Ilmar M. Wilbers", sim), ("Tickle-me Elmo", sim, uio),]

# Create slides, exchange 'Beamer' with 'Prosper' for Prosper
slides = BeamerSlides(title="""Easy Presentation Generation""",
                      author_and_inst=authors,
                      #date="Today",
                      #titlepage=False,
                      #titlepage_figure="brainhurts.ps",
                      #titlepage_figure_fraction_width=0.5,
                      #titlepage_left_column_width=0.7,
                      #short_title="Easyslides",
                      #short_author="Elmo et al.",
                      #toc_heading="Heading for TOC", 
                      #toc_figure="brainhurts.ps",
                      #toc_figure_fraction_width=0.5,
                      #theme="Darmstadt",                      
                      #colour=False,
                      #colour_theme="seahorse",
                      #newcommands=(r"{\OBS}[1]{\marginpar{\scriptsize##1}}",),
                      #header_footer=False,
                      )

# Test for BulletSlide:
bslide = BulletSlide("Title", ["Test", ["Subtest1", "Subtest2"],
                                       "Test2"], block_heading="Block heading", dim='single_then_all')

# Create table:
table = latextable([('x', 'x**2'), (3, 9), (5, 25)], column_headline_pos = 'r', column_pos='l')

# Create Text object:
block1 = Text(table)

# Create code Object:
block2 = Code(file='code.py', from_regex='import', to_regex='fileheader')

# Add two previous objects to a slide:
genslide = Slide(content=[block1, block2])

# Add a slide with pure text:
tslide = TextSlide("Not much")

# All elements on one line:
onelineslide = Slide(content=[BulletList(["Bullet1", "Bullet2", ["Subbullet1", "Subbullet2"],],)], dim='progressive')

# Add section
sect = Section("Problem")

# Pure text:
txt0 = Text("This is easy.")

# Bullets and subbullets:
blk0 = BulletBlock(
    [
        "Intro programming course = three new courses",
        ['Classical "IN105" with OO and Java',
         '"Informatics without tears" (minor programming)',
         'INF1100: scientific programming with Python',
         ],
        "C, C++, F77, F95, MPI, profiling, Matlab",
        ],)

# Do not dim this block:
blk1 = BulletBlock(heading="Challenges:",
                   bullets=["These courses need a variety of software packages!",
                            "Students have laptops (Linux, Windows, Mac)!",
                            "Fresh students know little about software installation"],
                   dim=False,
                   )

# Add blocks to slide:
bbslide = Slide(title=r"",dim='progressive',
                     content=[txt0, blk0, blk1,],)

# Add subsection:
subsect = SubSection("Native Installers")

block0 = TextBlock("""Where available, the use of native installers such as
APT, Fink, Darwinports and YUM, is often the easiest way of installing the necessary
software, as the dependencies are taken care of.""")

nslide = Slide("Native installers often solves the problem, but not always", content=[block0,])

sect1 = Section("Discussion")

block = TextBlock(r"""{\tiny
\begin{tabular}{|l|l|l|l|l|l|}
\hline
&Conduit&BYOS&WinInstall&VMware&Native\\
\hline
Pro&All OS,&Well tested&Based on&Controlled&Easy to use,\\
&easy to use&packages,&original installation&environment,&native to OS\\
&and add updates&easy to debug&packages&will always work&\\
&&(for maintainer)&&&\\
&&&&&\\
\hline
Con&In development,&May break,&Only Windows,&Large files,&Limited to\\
&not all Linux dists,&hard to debug,&a lot of clicking,&inflexible&some OS,\\
&complex system&(for user),&old versions&&not all packages\\
&&no Windows&(no 64-bit)&&available\\
&&&&&\\
\hline
\end{tabular}
}
""")

lastslide = Slide("Methods pros/ cons", content=[block,])

for i in [bslide, genslide, tslide, onelineslide, sect, bbslide, subsect,
          nslide, sect1, lastslide]:
    slides.add_slide(i)

# Dump to file:
f = file("presentation.tex", "w")
f.write(slides.get_latex())
f.close()
