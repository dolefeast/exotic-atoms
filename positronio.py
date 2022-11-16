from manim import *


class Positronio(Scene):
    def construct(self):
        title = Title("Onios")
        subtitle = Tex("Positronio [Ps]", color=RED).move_to(2*UP).scale(1.2)

        descripcion = MarkupText("Formado por un <span fgcolor='YELLOW'>electrón</span> y un <span fgcolor='PURPLE'>positrón</span>").next_to(subtitle, DOWN).scale(0.7)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(descripcion))


        energia = Tex(r"""\begin{flushleft}
                      Con un comportamiento similar al del Hidrógeno
                      pero una masa reducida \\$\mu = \frac{m_e}{2}$ se 
                      tiene un espectro de emisión con la mitad de 
                      la frecuencia
                      \end{flushleft}""").scale(0.7)
        En = Tex(r"$E_n [Ps] = - \frac{1}{2} \frac{m_e e^4}{8h^2 \varepsilon_0^2}\frac{1}{n^2} = \frac{E_n[H]}{2}$").next_to(energia, 2*DOWN)


        self.play(Write(energia))
        self.play(Write(En))
        
        self.wait()

        self.play(Unwrite(subtitle), Unwrite(energia), Unwrite(En), Unwrite(descripcion))

        L = Tex("$\mathcal{L}_\\text{QED} = -F^{\\mu \\nu}F_{\\mu \\nu} + \\overline{\\psi} \\left( i \\gamma ^\\mu D_\\mu - m)\\psi$", color=GREEN).move_to(UP).scale(1.3)

        interaccion = Tex(r"La interacción se media por la QED \\ $\implies$ Puesta a prueba de la precisión de QED").next_to(L, DOWN)

        medicion = Tex("Podemos medir y calcular el tiempo de desintegración").next_to(interaccion, DOWN)

        self.play(Write(L))
        self.play(Write(interaccion))
        self.play(Write(medicion))
        self.wait(2)

        self.play( Unwrite(interaccion), Unwrite(medicion), L.animate.shift(UP))

        blanco = Tex("Para Ps 1s0").move_to(3*LEFT)
        para = Tex("Para Ps $^1S_0$: ", color=BLUE).next_to(blanco, 0.8*DOWN) 
        orto = Tex("Orto Ps $^3S_1$: ", color=BLUE).next_to(para,DOWN)

        teo = Tex("Teórico").next_to(blanco, RIGHT + 0*DOWN)
        exp = Tex("Experimental").next_to(teo, RIGHT)
        
        res_para_teo = Tex("0.142ns").next_to(teo, DOWN)
        res_para_exp = Tex("0.125ns").next_to(exp, DOWN)

        res_orto_teo = Tex("142ns").next_to(res_para_teo, DOWN*1.6)
        res_orto_exp = Tex("141ns").next_to(res_para_exp, DOWN*1.6)

        self.play(Write(para), Write(orto))
        self.play(Write(teo), Write(res_para_teo), Write(res_orto_teo))
        self.play(Write(exp), Write(res_para_exp), Write(res_orto_exp))
        self.wait()

        
