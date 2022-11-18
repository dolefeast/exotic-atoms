from manim import *

class Onio(Scene):
    def construct(self):
        title = Tex(r"\huge{Onios}", color=MAROON).move_to(3*UP)
        sub = MarkupText(
            "Sistemas ligados formados por una \n\t<span fgcolor='YELLOW'>partícula</span> y su <span fgcolor='PURPLE'>antipartícula</span>.").scale(0.8).next_to(title, 2*DOWN)

        blist = MarkupText("<span fgcolor='RED'>Positronio:</span>\n<span fgcolor='GREEN'>Pionio:</span>\n<span fgcolor='BLUE'>Cuarkonio:</span>").next_to(sub, 2*DOWN + LEFT).shift(RIGHT)
#        blist.set_color_by_tex("Positronio:", RED)
#        blist.set_color_by_tex("Pionio:", GREEN)
#        blist.set_color_by_tex("Quarkonio:", BLUE)
        particulas = Tex(r"\begin{flushleft} $e^+$ y un $e^-$\\Un $\pi^+$ y un $\pi^-$\\Un cuark y su anti cuark\end{flushleft}").next_to(blist, 9*RIGHT).scale(1.3)

#        Pionio = Tex("Un $e^+$ y un $e^-$").next_to(blist, RIGHT)
#        Positronio = Tex("Un $\pi^+$ y un $\pi^-$").next_to(Pionio, 2*UP)
#        Quarkonio = Tex("\tUn cuark y su anti cuark").next_to(Pionio, 2*DOWN)

        title.move_to(DOWN - DOWN)
        self.play(Write(title))
        self.play(title.animate.shift(3*UP))
        self.play(Write(sub))
        self.play(Write(blist))
        self.play(Write(particulas))

        #self.play(Write(Positronio), Write(Pionio),Write(Quarkonio))

    


        

