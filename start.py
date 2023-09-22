from manim import *

class test_graph(Scene):
    def construct(self):
        graph = FunctionGraph(lambda x: pow(x, 2), color = RED)
        #graph = Vector([0.5 * 5, 0.5 * 3])
        number_plane = NumberPlane()
        self.play(GrowFromCenter(number_plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
