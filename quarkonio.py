from manim import *

class Quarkonio(Scene): 
    def construct(self):
        title = Title("Onios")
        subtitle = Tex("Quarkonio", color=BLUE).move_to(2*UP).scale(1.3)


        descripcion = MarkupText("Formados por un par <span fgcolor='YELLOW'>cuark</span> <span fgcolor='PURPLE'>anticuark</span>").next_to(subtitle, DOWN)

        posibilidades = Tex("Se habla generalmente de $J/\psi$ y Y").next_to(descripcion, DOWN)
        realmente = Tex("El mesón $J/\psi$ es el primer estado excitado del charmonio").next_to(posibilidades, DOWN)
        junto_a = Tex(r"Permiten el estudio del plasma de quarks-gluones \\del universo temprano", color=ORANGE).next_to(realmente, DOWN)
        a_traves = Tex("A través de la Cromodinámica Cuántica").next_to(junto_a, DOWN).set_color_by_gradient(BLUE, ORANGE)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(descripcion))
        self.wait()
        self.play(Write(posibilidades))
        self.play(Write(realmente))
        self.wait()
        self.play(Write(junto_a))
        self.play(Write(a_traves))
        self.wait()
