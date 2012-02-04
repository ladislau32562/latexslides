from latexslides

# Define latex newcommands
newcommands = r"""
\newcommand{\dx}{\, \mathrm{d}x}
\newcommand{\ds}{\, \mathrm{d}s}
\renewcommand{\u}{\pmb{u}}
\renewcommand{\v}{\pmb{v}}
\newcommand{\f}{\pmb{f}}
\newcommand{\strainr}{{1\over2}(\nabla\u + \nabla\u^T)}
"""

mapping_slide3 = \
MappingSlide([
    ('Why Python?', 'clipart/python1.png'),
    ('FEniCS PDE tools', 'clipart/fenics_logo.png', 0.8),
    ('PDE systems tools', 'figs-pdesys/mechanics_eqs_white.jpg', 1.5),
              ])

from Why_Python import wip_lots

RANS_modeling \
= Slide('What are the problems with computing turbulent flows?',
 content=[BulletBlock(heading='Three classes of models:',
 bullets=[
 'Direct Numerical Simulation',
 'Large Eddy Simulation',
 r'The jungle of \textcolor{red}{Reynolds-Averaged Navier-Stokes (RANS)} models: $k$-$\epsilon$, $k$-$\omega$, $v^2$-$f$, various tensor models, ...',
  ]),  # end bullets and BulletBlock
BulletBlock(heading='Should be easy to implement and compare...', bullets=[
 'Various models',
 'Various linearizations',
 'Coupled vs.~segregated solution',
 'Picard vs.~Newton iteration',
     ]),  # end bullets and BulletBlock
],   # end content
figure='clipart/smoke1.jpg',
figure_pos='e',
figure_fraction_width=0.4,
left_column_width=0.6)


RANS_eqs1 \
= Slide('Example: $k$-$\epsilon$ model (unknowns: $\u$, $p$, $k$, $\epsilon$)',
 content=[TextBlock(text=r"""
{  %\footnotesize
\[
     \frac{\partial \u} {\partial t}
     + \u \cdot \nabla\u
      = - \frac{1} {\varrho}\nabla p   + \nu \nabla^{2} \u  + \f
-\nabla\cdot\overline{\u'\u'}
\]
\[ \nabla \cdot \u = 0 \]
\[ \nabla\cdot\overline{\u'\u'} = -2{k^2\over\epsilon}\strainr + {2\over3}k\mathbfx{I} \]
\[ {\partial k\over\partial t}
+ \u\cdot\nabla k = \nabla \cdot (\nu_k  \nabla k) +P_k-\epsilon-D,\label{k:eq:LS}\]
\[ {\partial\epsilon\over\partial t} + \u\cdot\nabla\epsilon =
\nabla \cdot ( \nu_\epsilon
\nabla \epsilon ) +\left( C_{\epsilon 1} P_k - C_{\epsilon 2} f_2 \epsilon \right) \frac{\epsilon}{k}+E\]
\[ \epsilon = 2\nu \overline{\s:\s}, \quad \s = {1\over2}
(\nabla\u' + (\nabla\u')^T)\]
\[\nu_k = \nu + \frac{\nu_T}{\sigma_k} \]
\[ ... \]
}
"""),
],   # end content
)

linearization_idea \
= Slide(r'Linearization, i.e., implicit vs explicit treatment is a matter of inserting or removing an underscore',
 content=[
TextBlock(heading=r'Implicit treatment of $\epsilon$ in coupled $k$-$\epsilon$ system:',
text=r"""$F_k = ... + \int_\Omega \textcolor{red}{\epsilon} v_k\dx \quad\rightarrow\quad$ \texttt{e*v\_k*dx}"""),
TextBlock(heading=r'Explicit treatment of $\epsilon$:',
text=r"""$F_k = ... + \int_\Omega \textcolor{red}{\epsilon_{-}} v_k\dx \quad\rightarrow\quad$ \texttt{e\_*v\_k*dx}"""),
TextBlock(heading=r'Explicit treatment of $\epsilon$, but implicit term in $k$ eq.:',
text=r"""$F_k = ... + \int_\Omega \textcolor{red}{\epsilon_{-}\frac{k}{k_{-}}} v_k\dx \quad\rightarrow\quad$ \texttt{e\_*k/k\_*v\_k*dx}"""),
TextBlock(heading=r'Weighted combination:',
text=r"""$F_k = ... + \int_\Omega \textcolor{red}{((1-w)\epsilon_{-}k + w\epsilon k_{-})\frac{1}{{k_{-}}}} v_k\dx \quad\rightarrow\quad$ \texttt{(1/k\_)*((1-w)*e\_*k + w*e*k\_)*v\_k*dx}"""),
],   # end content
dim='blocks')


second_rank_tensor_PDE \
= Slide(r'18 highly coupled nonlinear PDEs',
    content=[
        TextBlock(heading=r'The elliptic relaxation model',
        text=r"""\begin{align}
         \frac{\partial R_{ij}} {\partial t} + u_k \frac{\partial R_{ij}}{\partial x_k} +
          \frac{\partial T_{kij}}{\partial x_k}  &= G_{ij} + P_{ij} - \varepsilon_{ij} \nonumber \\
          L^2 \nabla^2 f_{ij} - f_{ij} &=  -\frac{G_{ij}^h}{k} - \frac{2 A_{ij}}{T} \nonumber\\
          \hbox{+ standard eqs. for} & {\bf u}, p, k, \epsilon
          \end{align}"""),
        CodeBlock(heading='Coupled implementation of variational forms:',
        code=
r"""
class Steady_RF_1(TurbModel):

    def form(self, R, R_, v_R, k_, e_, P_, nu, u_, F, F_, v_F,
             A_, Gh, Cmu, T_, L_, **kwargs):  # variational form

        Fr = inner(dot(grad(R), u_), v_R)*dx + nu*inner(grad(R), grad(v_R))*dx  \
             + inner(Cmu*T_*dot(grad(R), R_), grad(v_R) )*dx
             - inner(k_*F, v_R)*dx - inner(P_, v_R )*dx + inner(R*e_*(1./k_), v_R)*dx \

        Ff = inner(grad(F), grad(L_**2*v_F))*dx + inner(F , v_F)*dx \
             - (1./k_)*inner(Gh , v_F)*dx - (2./T_)*inner(A_ , v_F)*dx

        return Fr + Ff
        """, fontsize=r'\tiny')
        ],
)


pdesys_slides = [
mapping_slide3,
wip_lots,
RANS_modeling,
RANS_eqs1,
linearization_idea,
second_rank_tensor_PDE,
]

# The rest is normally in a separate file so that slide objects are
# in a module that can be imported in several "talk" files.

# Convenient variables for institutions
simula = r'Center for Biomedical Computing\\ Simula Research Laboratory'
mi = r'Dept.~of Mathematics, University of Oslo'
ffi = r'Norwegian Defence Research Establishment (FFI)'

authors = [
    ("Hans Petter Langtangen", simula, ifi),
    ("Mikael Mortensen", mi, simula),
    ]

def make_talk(slides, title, date, handout=False, theme='blue2'):
    collection = BeamerSlides(
        title=title,
        author_and_inst=authors,
        date=date,
        handout=handout,
        #toc_heading='Outline',
        toc_heading='',  # turn off toc in the beginning
        #beamer_theme='hpl1',
        #beamer_theme='cbc',
        beamer_theme=theme,
        header_footer=False,  # navigation bars etc.
        #prosper_style='ffipres',
        newcommands=newcommands,
        latexpackages=r'\usepackage{tikz}',
        #titlepage_figure=('figs-pdesys/diffusor_R12.png'),
        #titlepage_figure=('figs-pdesys/diffusor_R11.png'),
        titlepage_figure=('figs-pdesys/turbulent_flow1.jpg'),
        titlepage_figure_fraction_width=0.5,
        titlepage_figure_pos='s',
        toc_figure='clipart/fenics_logo.png',
        toc_figure_fraction_width=1.0,
        toc_left_column_width=0.5,
        )

    for s in slides:
        collection.add_slide(s)

    # Dump to file:
    filename = 'themedemo'
    filename = 'tmp_%s' % filename
    f = file(filename + '.p.tex', "w")
    f.write(collection.get_latex())
    f.close()
    print "pdflatex %s.tex" % filename
    print '# Handout:\npdfnup --nup 2x3 --frame true --delta "1cm 1cm" --scale 0.9 %s.pdf' % filename


if __name__ == '__main__':
    import sys
    try:
        theme = sys.argv[1]
    except IndexError:
        theme = 'red2'
    try:
        ptenvir = sys.argv[2]  # ptex2tex code envir
    except IndexError:
        ptenvir = None
    Code.ptex2tex_envir = ptenvir
    
    make_talk(slides=pdesys_slides,
              title="Flexible Specification of Large Systems of Nonlinear PDEs",
              date='KAUST, Feb 6, 2012',
              handout='--handout' in sys.argv,
              theme=theme
              )


