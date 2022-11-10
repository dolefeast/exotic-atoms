from manim import * 

class Lagrangian(Scene):
    def construct(self):
        L = Tex("$L = -F^{\\mu \\nu}F_{\\mu \\nu} + \\overline{\\psi} \\left( i \\gamma ^\\mu D_\\mu - m)\\psi$")
        text = Tex("Eso fue el lagrangiano de la QED")

        L.shift(2*UP)
        self.play(Write(L))
        self.wait()
        self.play(Write(text))


        #self.play(
