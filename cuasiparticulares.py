from manim import *

class Quasiparticle(Scene):
    def construct(self):
        title = Tex("Átomos Cuasiparticulares: Excitón", color=LIGHT_BROWN).scale(1.3) #Color?
        self.play(Write(title))
        self.play(title.animate.shift(2*UP))

        subtitle = Tex("Estado ligado entre un electrón y un agujero", tex_to_color_map={'electrón':YELLOW, 'agujero':PURPLE}).next_to(title, 1*DOWN)
        self.play(Write(subtitle))

        proceso = Tex("Aparece al excitar un electrón de \\\ la capa de valencia a la capa de conducción").next_to(subtitle,1.5*DOWN)
        self.play(Write(proceso))

        aparece = Tex(r"El electrón deja tras de sí un agujero de \\ carga positiva que lo atrae y causa una órbita").next_to(proceso, DOWN)
        self.play(Write(aparece))
        self.wait(2)

        self.play(Unwrite(aparece), Unwrite(subtitle), Unwrite(proceso))

        distingue = Tex(r"Distinguimos entre excitón de Wannier-Mott y de Frenkel", tex_to_color_map={'Wannier-Mott':RED_B, 'Frenkel':GOLD_B})
        wannier = Tex(r"Wannier-Mott: Aparece en sustancias conductoras", tex_to_color_map={'Wannier-Mott':RED_B}).next_to(distingue, DOWN)
        frenkel = Tex(r"Frenkel: Aparece en sustancias aislantes", tex_to_color_map={'Frenkel':GOLD_B}).next_to(wannier, DOWN)
        wannier2 = Tex(r"Wannier-Mott: Órbitas en varias celdas", tex_to_color_map={'Wannier-Mott':RED_B}).next_to(distingue, DOWN)
        frenkel2 = Tex(r"Frenkel: Órbitas en una celda", tex_to_color_map={'Frenkel':GOLD_B}).next_to(wannier, DOWN)

        self.play(Write(distingue))
        self.play(Write(wannier2))
        self.play(Write(frenkel2))

        self.wait()

        self.play(Transform(wannier2, wannier), Transform(frenkel2, frenkel))
        self.wait()
