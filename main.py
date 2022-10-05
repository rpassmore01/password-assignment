#	name: Russell Passmore
#	class: ICS4U
#	assignment: password assignment
#	date: October 4, 2022


from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)