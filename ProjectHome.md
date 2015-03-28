## What Is Latexslides? ##

Latexslides is a tool that allows you to write slides in Python:
each slide is a Python object, and a talk is a list of such objects.
This list can converted to LaTeX beamer or prosper code.
One can compose talks by importing slide objects from Python modules
and hence reuse individual slides.

Latexslides simplifies many of the constructions in LaTeX beamer.
For example, a figure can be placed to the right, left, under or over
a bullet list by simply specifying its position as n, s, e, w (north,
south, east, or west). Each slide object is composed of various Python
objects reflecting basic building blocks in slides: text block,
bullet block, figure, etc. Take a look at a
[sample talk](https://latexslides.googlecode.com/svn/trunk/doc/exampletalk.pdf),
which explains the basics of Latexslides, and compare this PDF file
with the Latexslides
[source](https://latexslides.googlecode.com/svn/trunk/doc/exampletalk.py)
in Python. A more manual-style documentation is also available as a
[wiki](http://code.google.com/p/latexslides/wiki/Tutorial), a
[web page](https://latexslides.googlecode.com/svn/trunk/doc/latexslides_doc.html)
or as a
[PDF](https://latexslides.googlecode.com/svn/trunk/doc/latexslides_doc.pdf) file.