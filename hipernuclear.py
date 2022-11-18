from manim import *

class Hypernuclear(Scene):
    def construct(self):
        title = Tex("Átomos hipernucleares", color=RED).scale(1.3)
        subtitle = Tex(r"Un núcleo estándar, cambiando un nucleón por \\un barión de extrañeza no nula (hiperón)")


        # --- ANIMATIONS ---
        self.play(Write(title))
        self.play(title.animate.shift(3*UP))
        self.play(Write(subtitle))
