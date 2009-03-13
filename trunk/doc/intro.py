from latexslides import *

author_and_inst = [("John Doe", "Royal University of Nothing")]

slides = BeamerSlides(title="Short Introduction",
                      titlepage=False,
                      toc_heading=None,
                      author_and_inst=author_and_inst,)

slide1 = Slide("Slide 1",
               content=[TextBlock(r"""
Program for computing the height of a ball thrown up in the air:
$y=v_0t- {1\over 2} gt^2$""") ,
                        Code(file='code.py')],
               figure='brainhurts.ps',
               figure_pos='w',
               figure_fraction_width=0.4,
               left_column_width=0.3,
               )

slide2 = BulletSlide("Slide 2",
                     ["Latexslides is flexible:",
                      ["One can create slides based on Python elements",
                       r"\LaTeX~code can be inserted directly in the code"],
                      "Latexslides means less code and less time used:",
                      ["The code is generated automatically",
                       r"One does not need to learn \LaTeX"],
                      "The package is easily installed by typing" +
                      Code("python setup.py install"),],
                     block_heading="Advantages of latexslides",
                     )
                     
collection = [slide1, slide2]
slides.add_slides(collection)

# Dump to file:
slides.write("intro.tex")
