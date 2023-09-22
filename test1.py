from manim import *

class class1(Scene):
    def construct(self):
        plane = NumberPlane([-10, 10], [-10, 10], x_length = 10, y_length = 10)
        vector1 = Vector([0.5 * 5, 0.5 * 3])
        self.play(GrowFromCenter(plane))
        self.wait(1)
        self.play(Create(vector1))
        self.wait(1)
