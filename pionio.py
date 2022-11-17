from manim import *

class Pionio(Scene):
    def construct(self):
        title = Title("Onios")
        subtitle = Tex("Pionio", color=GREEN).move_to(2*UP).scale(1.3)

        descripcion = MarkupText("Estado ligado entre un mesón <span fgcolor='YELLOW'></span><span fgcolor='YELLOW'>&#x3C0;⁺ </span> y <span fgcolor='PURPLE'> &#x3C0;⁻ </span>").next_to(subtitle, DOWN)

        text = Text("Interacción a través de la cromodinámica cuántica:").scale(0.8)
        L_sup = Tex(r"$\mathcal{L}_\text{QCD} = -\frac{1}{4}F^\alpha_{\mu\nu}F^{\mu\nu}_\alpha - \Sigma_n \bar{\psi_n} \gamma^\mu \left[ \partial\mu - igA^\alpha_\mu t_\alpha\right]\psi_n -$").next_to(text, DOWN).set_color_by_gradient(RED, BLUE)
        L_sub = Tex(r"$- \sum_n m_n \bar{\psi}_n\psi_n$").next_to(L_sup, DOWN).shift(2*LEFT).set_color_by_gradient(RED, BLUE) #Ya encontraré forma de ponerlo bonito

        text2 = Text("Ponemos a prueba su precisión mediante mediciones").scale(0.7).next_to(L_sub, DOWN).shift(2*RIGHT)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(descripcion))
        self.wait()


        self.play(Write(text))
        self.play(Write(L_sup), Write(L_sub))
        self.wait()
        self.play(Write(text2))
