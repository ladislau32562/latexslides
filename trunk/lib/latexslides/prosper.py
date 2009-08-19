from core import *
import os

class ProsperSlides(Slides):
    """ Class for creating a presentation using the Prosper LaTeX package.
    """
    def __init__(self, *args, **kwargs):
        Slides.__init__(self, *args, **kwargs)
        Content.fig_scale = 0.8
        Content.font_scale = True
        # Fix \emp such that the font is smaller
        # (adjusted for hplplainsmall)
        self.newcommands[0] = r"{\emp}[1]{{\relsize{-3}\texttt{#1}}}"
        # Or relsize{-4} to match the \tiny fontsize in verbatim
        # fix style:
        self.prosper_style = 'hplplainsmall'
                
    # Document header
    def _header(self):
        self.buf.write(r'\documentclass[%')
        if self.colour:
            self.buf.write('\npdf,colorBG,slideColor,\n')
        else:
            self.buf.write('\nps,slideBW,nocolorBG,\n')
        self.buf.write(self.prosper_style + '\n]{prosper}\n')

        self.buf.write(r"""
\usepackage{relsize,fancybox,epsfig}
\usepackage{subfigure}
\usepackage{color}  % may be problematic
\usepackage{moreverb,graphics,amsmath}
\usepackage{fancyvrb,slidesec,lscape}
\usepackage{pstricks,pst-node,pst-text,pst-3d}
\usepackage{amsmath}
\usepackage[latin1]{inputenc}
\usepackage[english]{babel}

\newcommand{\newpart}[2]{%
\slideCaption{#1}
\begin{slide}{}
\ \ \\
\vspace{2cm}
\vfill
\begin{center}
\fontTitle{#1}
\end{center}
\vfill
\end{slide}
}
""")

    # Title page
    def _titlepage(self):
        if self.titlepage:
            titlepage = r"\maketitle"
        else:
            titlepage = ""
        authors = [a for a, i in self.author_and_inst]
        authors_cmd = '\\\\\n'.join(authors)
        insts_cmd = '\\\\\n'.join(self.insts)
        self.buf.write(r"""

\title{%s}
\author{%s\\
\  \\
%s
}

%s
""" % (self.title, authors_cmd, insts_cmd, titlepage))
        if self.copyright_text:
            self.buf.write("""
\Logo{\footnotesize \copyright\hspace*{0.2mm} %s}
""" % self.copyright_text)
        self._ltx = self.buf.getvalue()

    def _renderSlide(self, slide):
        if slide.hidden:
            return

        if isinstance(slide, RawSlide):
            c = slide.content[0]
            self.renderContent[type(c)](c)
            return
        
        self.buf.write(r"""\begin{slide}{%s}

""" % (slide.title))

        # If figure is to the north:
        if slide._fig and slide._fig_pos == 'n':
            width = 1./len(slide._fig)
            self.buf.write(r"""
\begin{tabular}{l}
""")
            for i in slide._fig:
                self.buf.write(r"""
\begin{minipage}{%g\textwidth}
%s
\end{minipage}
""" % (width, i))
            self.buf.write(r"""
\end{tabular}
""")
        # If figure is to the west:
        if slide._fig and slide._fig_pos == 'w':
            self.buf.write(r"""
\begin{minipage}[t]{%g\textwidth}
\begin{figure}[ht]
""" %(0.95*slide._left_column_width))
            for i in slide._fig:
                self.buf.write(r"""
\mbox{
\subfigure{%s}
}
""" %(i))
            self.buf.write(r"""
\end{figure}
\end{minipage}
\begin{minipage}{%g\textwidth}
""" %(0.95*slide._right_column_width))

        # If figure is to the east:
        if slide._fig and slide._fig_pos == 'e':
            self.buf.write(r"""
\begin{minipage}[t]{%g\textwidth}
""" %(0.95*slide._left_column_width))

        for c in slide.content:
            self.renderContent[type(c)](c)

        # If figure is to the east:
        if slide._fig and slide._fig_pos == 'e':
            self.buf.write(r"""
\end{minipage}
\begin{minipage}[t]{%g\textwidth}
\begin{figure}[ht]
""" %(0.95*slide._right_column_width))
            for i in slide._fig:
                self.buf.write(r"""
\mbox{
\subfigure{%s}
}
""" %(i))
            self.buf.write(r"""
\end{figure}
\end{minipage}
""")
        # If figure is to the west:
        if slide._fig and slide._fig_pos == 'w':
            self.buf.write(r"""
\end{minipage}
""")

        # If figure is to the south:
        if slide._fig and slide._fig_pos == 's':
            width = 1./len(slide._fig)
            self.buf.write(r"""
\begin{tabular}{l}
""")
            for i in slide._fig:
                self.buf.write(r"""
\begin{minipage}{%g\textwidth}
%s
\end{minipage}
""" % (width, i))
            self.buf.write(r"""
\end{tabular}
""")
            
        self.buf.write(r"""
\end{slide}
""")
                
    def _renderSection(self, section):
        self.buf.write("\n")
        self.buf.write(r"""\newpart{%s}{}
""" % (section._title))
        # Top-level slides
        for s in section.slides:
            self.buf.write("\n")
            self._renderSlide(s)
        # Nested slides
        for s in section.subsections:
            self.buf.write("\n")
            self._renderSubsection(s)

    def _renderSubsection(self, subsection):
        self.buf.write(r"""\newpart{%s}{}
""" % (subsection._title))
        for s in subsection.slides:
            self.buf.write("\n")
            self._renderSlide(s)
                       
    def _renderBulletList(self, bulletlist):
        self.buf.write("\n" + r"""\begin{itemize}
""")
        for b in bulletlist.bullets:
            if isinstance(b, list):
                b = BulletList(b)
                self.renderContent[type(b)](b)
            elif isinstance(b, BulletList):
                pass
                # Nested list
            else:
                self.buf.write(r"\item ")
                if isinstance(b, basestring):
                    b = Text(b)
                self.renderContent[type(b)](b)

        self.buf.write(r"""\end{itemize}""" + "\n")

    def _renderBlock(self, block):
        if block.heading:
            self.buf.write('\n\n'+ block.heading + '\n\n')

        if isinstance(block, TableBlock):
            if block.center:
                self.buf.write(r"""\begin{center}""")
        for c in block.content:
            if isinstance(c, basestring):
                c = Text(c)
            self.renderContent[type(c)](c)

        if isinstance(block, TableBlock):
            if block.center:
                self.buf.write(r"""\end{center}""")

    def _renderTextBlock(self, textblock):
        self._renderBlock(textblock)

    def _renderBulletBlock(self, bulletblock):
        self._renderBlock(bulletblock)
        
    def _renderCodeBlock(self, codeblock):
        self._renderBlock(codeblock)

    def _renderTableBlock(self, tableblock):
        self._renderBlock(tableblock)

    def write(self, filename):
        Slides.write(self, filename)
        filename = os.path.splitext(filename)[0]
        print 'latex %s.tex; latex %s.tex;' %(filename, filename),
        print 'dvipdf %s.dvi' %(filename)
