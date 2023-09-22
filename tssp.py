from manim import *

points = [
    [1.5, 2],
    [2, 1.5]
]

class anime(Scene):
    def construct(self):
        plane = NumberPlane()
        vector1 = Vector(points[0])
        vector2 = Vector(points[1])
        result_vector = Vector([points[0][0] + points[1][0], points[0][1] + points[1][1]], color=RED, stroke_width=6)

        #projections of first vector
        projection_x = Line(([0, 0, 0]), ([points[0][0], 0, 0]), color = RED, stroke_width = 5)
        projection_y_start = Line(([points[0][0], 0, 0]), ([points[0][0], points[0][1], 0]), color=RED, stroke_width=5)
        projection_y_end = Line(([0, 0, 0]), ([0, points[0][1], 0]), color=RED, stroke_width=5)

        #projections of second vector
        projection2_x = Line(([0, 0, 0]), ([points[1][0], 0, 0]), color = GREEN, stroke_width = 5)
        projection2_y_start = Line(([points[1][0], 0, 0]), ([points[1][0], points[1][1], 0]), color=GREEN, stroke_width=5)
        projection2_y_end = Line(([0, 0, 0]), ([0, points[1][1], 0]), color=GREEN, stroke_width=5)

        total_projection_x = Line(([0, 0, 0]), ([points[0][0] + points[1][0], 0, 0]), color = YELLOW, stroke_width = 8)
        total_projection_y_start = Line(([0, 0, 0]), ([0, points[0][1] + points[1][1], 0]), color=YELLOW, stroke_width=8)
        total_projection_y_end = Line(([points[0][0] + points[1][0], 0, 0]), ([points[0][0] + points[1][0], points[0][1] + points[1][1], 0]), color=YELLOW, stroke_width=8)

        self.play(GrowFromCenter(plane))
        self.wait(1.5)
        self.play(Create(vector1))
        self.wait(1.5)
        self.play(Create(projection_x), Create(projection_y_start))
        self.wait(1.5)
        self.play(Transform(projection_y_start, projection_y_end))
        self.wait(2)
        self.play(Create(vector2))
        self.wait(1.5)
        self.play(Create(projection2_x), Create(projection2_y_start))
        self.wait(1.5)
        self.play(Transform(projection2_y_start, projection2_y_end))
        self.wait(1.5)
        self.play(Transform(projection_y_end, total_projection_y_start), Uncreate(projection2_y_end),
                  Transform(projection2_x, total_projection_x), Uncreate(projection_x))
        self.wait(1.5)
        self.play(Transform(total_projection_y_start, total_projection_y_end), Uncreate(projection_y_end),
                  Uncreate(projection2_y_start), Uncreate(projection_y_start))
        self.wait(1.5)
        self.play(Create(result_vector), Uncreate(vector1), Uncreate(vector2))
        self.wait(1.5)