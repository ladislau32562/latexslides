#!/usr/bin/env python

import os, subprocess, glob, sys
if len(sys.argv) < 2:
    print 'Usage: %s 0/1 for generating png files from Beamer talk' %sys.argv[0]
    print 'Assuming 0'
    generate = False
else:
    generate = bool(int(sys.argv[1]))

filename = 'textexampletalk'
# First, convert Beamer talk to images
gs_args = ['gs', '-dNOPAUSE', '-dSAFER', '-dBATCH', '-sDEVICE=pngalpha',
           '-r300', '-sOutputFile=exampletalktmp%03d.png', 'exampletalk.pdf']

if generate:
    result = subprocess.Popen(['python', 'exampletalk.py'])
    result.wait()
    result = subprocess.Popen(['latex', 'exampletalk.tex'])
    result.wait()
    result = subprocess.Popen(['latex', 'exampletalk.tex'])
    result.wait()
    result = subprocess.Popen(['dvipdf', 'exampletalk.dvi'])
    result.wait()
    result = subprocess.Popen(gs_args)
    if result.wait():
        print '\nRunning gs failed with the error above, exiting.'
        sys.exit(1)
#    for i in range(1, 52):
#        result = subprocess.Popen(['psselect', '-p%s' %i, 'exampletalk.ps'], stdout=subprocess.PIPE)
#        of = open('exampletalktmp%03d.eps' %i, 'w')
#        of.write(result.stdout.read())
#        of.close()
    for i in range(1, 52):
        print 'converting slide ', i
        result = subprocess.Popen(['bmeps', '-a', '-leps',
                                   'exampletalktmp%03d.png' %i])
        result.wait()

#files = glob.glob('exampletalktmp*.ps')
#length = len(files)

outfile = open(filename + '.py', 'w')
outfile.write("""
from latexslides import *

slides = ProsperSlides(title="Exampletalk",
                       prosper_style='exampletalk',
                       titlepage=False,
                       toc_heading=None,)
""")
outfile.write(r"""
slide1 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # First set a few@# Exemplify
''', fontsize='tiny')])
""")
outfile.write(r"""
slide3 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # Exemplify raw@# The talk
''', fontsize='tiny')])
""")
outfile.write(r"""
slide4 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # The talk can be@what_is
''', fontsize='tiny')])
""")
outfile.write(r"""
slide5 = Slide(content=[Code(r'''
@@@CODE exampletalk.py what_is@subsec
''', fontsize='tiny')])
""")
outfile.write(r"""
slide6 = Slide(content=[Code(r'''
@@@CODE exampletalk.py subsec_p@ex1
''', fontsize='tiny')])
""")
outfile.write(r"""
slide7 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex1 =@structure
''', fontsize='tiny')])
""")
outfile.write(r"""
slide8 = Slide(content=[Code(r'''
@@@CODE exampletalk.py structure =@blocks
''', fontsize='tiny')])
""")
outfile.write(r"""
slide9 = Slide(content=[Code(r'''
@@@CODE exampletalk.py blocks =@classes
''', fontsize='tiny')])
""")
outfile.write(r"""
slide10 = Slide(content=[Code(r'''
@@@CODE exampletalk.py classes =@dimming
''', fontsize='tiny')])
""")
outfile.write(r"""
slide16 = Slide(content=[Code(r'''
@@@CODE exampletalk.py dimming =@why =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide22 = Slide(content=[Code(r'''
@@@CODE exampletalk.py why =@# Short form
''', fontsize='tiny')])
""")
outfile.write(r"""
slide31 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # Short form@figures =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide32 = Slide(content=[Code(r'''
@@@CODE exampletalk.py figures =@ex_fig = 
''', fontsize='tiny')])
""")
outfile.write(r"""
slide33 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_fig =@ex_fig2 =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide34 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_fig2 =@ex_fig3
''', fontsize='tiny')])
""")
outfile.write(r"""
slide35 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_fig3 =@multiple_figs =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide36 = Slide(content=[Code(r'''
@@@CODE exampletalk.py multiple_figs =@subsec_code = 
''', fontsize='tiny')])
""")
outfile.write(r"""
slide37 = Slide(content=[Code(r'''
@@@CODE exampletalk.py subsec_code =@code_obj = 
''', fontsize='tiny')])
""")
outfile.write(r"""
slide38 = Slide(content=[Code(r'''
@@@CODE exampletalk.py code_obj =@code_obj_result = 
''', fontsize='tiny')])
""")
outfile.write(r"""
slide39 = Slide(content=[Code(r'''
@@@CODE exampletalk.py code_obj_result =@sec_specials =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide40 = Slide(content=[Code(r'''
@@@CODE exampletalk.py sec_specials =@sections =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide41 = Slide(content=[Code(r'''
@@@CODE exampletalk.py sections =@navigation = 
''', fontsize='tiny')])
""")
outfile.write(r"""
slide42 = Slide(content=[Code(r'''
@@@CODE exampletalk.py navigation =@ex_header =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide43 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_header =@prosper =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide44 = Slide(content=[Code(r'''
@@@CODE exampletalk.py prosper =@ex_titlepage =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide45 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_titlepage =@emacs =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide46 = Slide(content=[Code(r'''
@@@CODE exampletalk.py emacs =@# Note
''', fontsize='tiny')])
""")
outfile.write(r"""
slide47 = Slide(content=[Code(r'''
@@@CODE exampletalk.py slide_obj1 =@slide_obj2 =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide48 = Slide(content=[Code(r'''
@@@CODE exampletalk.py slide_obj2 =@compiling =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide49 = Slide(content=[Code(r'''
@@@CODE exampletalk.py compiling =@maths =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide50 = Slide(content=[Code(r'''
@@@CODE exampletalk.py maths =@learning =
''', fontsize='tiny')])
""")
outfile.write(r"""
slide51 = Slide(content=[Code(r'''
@@@CODE exampletalk.py learning =@# Make
''', fontsize='tiny')])
""")
outfile.close()

# Extract the slidenames
result = subprocess.Popen(['extract_slidenames', filename + '.py'],
                          stdout=subprocess.PIPE)
outfile = open(filename + '.py', 'a')
outfile.write('\n' + result.stdout.read())
outfile.write(r"""
slides.add_slides(collection)
slides.write('%s')
""" %(filename + '.p.tex'))
outfile.close()

# Run latexslides
result = subprocess.Popen(['python', filename + '.py'],
                          stdout=subprocess.PIPE)
command = result.stdout.read()

# Run ptex2tex
result = subprocess.Popen(['ptex2tex', filename + '.p.tex'], stdout=subprocess.PIPE)
print result.stdout.read()

# Run LaTeX
result = subprocess.Popen(['latex', filename + '.tex'])
result.wait()
result = subprocess.Popen(['latex', filename + '.tex'])
result.wait()
result = subprocess.Popen(['dvipdf', filename + '.dvi'])
result.wait()

# Second, convert Prosper talk to images
gs_args = ['gs', '-dNOPAUSE', '-dSAFER', '-dBATCH', '-sDEVICE=pngalpha',
           '-r300', '-sOutputFile=textexampletalktmp%03d.png', 'textexampletalk.pdf']

if generate:
    result = subprocess.Popen(gs_args)
    if result.wait():
        print '\nRunning gs failed with the error above, exiting.'
        sys.exit(1)
#    result = subprocess.Popen(['dvips', '-Ppdf', 'textexampletalk.dvi'])
#    result.wait()
#    for i in range(1, 33):
#        result = subprocess.Popen(['psselect', '-p%s' %i, 'textexampletalk.ps'], stdout=subprocess.PIPE)
#        of = open('textexampletalktmp%03d.eps' %i, 'w')
#        of.write(result.stdout.read())
#        of.close()
    for i in range(1, 33):
        print 'converting slide ', i
        result = subprocess.Popen(['bmeps', '-a', '-leps',
                                   'textexampletalktmp%03d.png' %i])
        result.wait()

os.system('mv *exampletalk*.eps *exampletalk*.png figs')
