from manim import *
import numpy as np
# manim scene02.py NumberLineScene02 -pql

class NumberLineScene02(Scene):
    def construct(self):
        color2 = YELLOW
        color3 = RED
        dot_color = GREEN

        # Add title
        title = Tex("Show ","$\\sqrt{2}$ and $\\sqrt{3}$", " in Number Line")
        title[1].set_color(YELLOW)
        title[1].next_to(title[0], RIGHT)
        self.play(Write(title))
        self.play(FadeOut(title))

        # Add text
        text = Tex("Where does $\\sqrt{2}$ lie in Number Line?").to_edge(UP)
        self.play(Write(text))
        # self.play(FadeOut(text))

        # Create number line
        number_line = NumberLine( x_range=[-2, 3], include_numbers=True, include_tip=True, unit_size=2)
         # shift number line
        number_line.shift(DOWN)
        self.play(Create(number_line))
        self.play(number_line.animate.to_edge(LEFT))

        # Add vertical line and label "1"
        unit_size = number_line.unit_size
        vertical_line = Line(number_line.n2p(1), number_line.n2p(1) + UP * unit_size)
        self.play(Create(vertical_line))
        text_1 = Tex("1")
        text_1.next_to(vertical_line, 0.6 * RIGHT)
        self.play(Create(text_1))

        # Add line and label "sqrt(2)"
        line_2 = Line(number_line.n2p(0), number_line.n2p(1) + UP * unit_size).set_color(color2)
        self.play(Create(line_2))
        text_2 = Tex("$\\sqrt{2}$")
        text_2.set_color(color2)
        text_2.shift(line_2.get_center())
        text_2.rotate(45 * DEGREES)
        text_2.shift(0.25 * UP, 0.25 * LEFT)
        self.play(Create(text_2))
        self.wait(2)

        # Make an arc
        center = number_line.n2p(0)
        start = number_line.n2p(1) + UP * unit_size
        end = number_line.n2p(np.sqrt(2))
        radius = np.linalg.norm(start-center)
        arc1 = Arc(
            start_angle=np.angle(complex(start[0]-center[0], start[1]-center[1])),
            angle=np.angle(complex(end[0]-center[0], end[1]-center[1])) - np.angle(complex(start[0]-center[0], start[1]-center[1])),
            radius=radius,
            arc_center=center
        )
        arc1.set_color(color2)
        dotted_arc = DashedVMobject(arc1)
        self.play(Create(dotted_arc))

        # Add dot for sqrt(2)
        dot_sqrt2 = Dot(number_line.n2p(np.sqrt(2))).set_color(dot_color)
        self.play(Create(dot_sqrt2))

       # add sqrt(3)
        text2 = Tex("Similarly we can find out the position of ","$\\sqrt{3}$").to_edge(UP)
        self.play(Transform(text, text2))

        # perpendicular line and label "1"
        unit_vect = line_2.get_unit_vector()
        perp_vect = rotate_vector(unit_vect, 90 * DEGREES)
        perp_line = Line(line_2.get_end(), line_2.get_end() + unit_size * perp_vect)
        # perp_line.set_color(YELLOW)
        self.play(Create(perp_line))
        self.wait(2)
        text_perp = Tex("1")
        text_perp.shift(perp_line.get_center())
        text_perp.rotate(45 * DEGREES)
        text_perp.shift(0.19 * UP, 0.19 * RIGHT)
        self.play(Create(text_perp))
        self.wait(2)

        
        
        # Add line and label "sqrt(3)"
        line_3 = Line(number_line.n2p(0), perp_line.get_end()).set_color(color3)
        self.play(Create(line_3))
        text_3 = Tex("$\\sqrt{3}$")
        text_3.set_color(color3)
        text_3.shift(line_3.get_center())
        text_3.rotate(80.25 * DEGREES)
        text_3.shift(0.3 * UP, 0.3 * LEFT)
        self.play(Create(text_3))
        self.wait(2)

        # Make an arc
        center = number_line.n2p(0)
        start = perp_line.get_end()
        end = number_line.n2p(np.sqrt(3))
        radius = np.linalg.norm(start-center)
        arc2 = Arc(
            start_angle=np.angle(complex(start[0]-center[0], start[1]-center[1])),
            angle= -80.5 * DEGREES,
            radius=radius,
            arc_center=center
        )
        arc2.set_color(color3)
        dotted_arc = DashedVMobject(arc2)
        self.play(Create(dotted_arc))

        # Add dot for sqrt(3)
        dot_sqrt3 = Dot(number_line.n2p(np.sqrt(3))).set_color(dot_color)
        self.play(Create(dot_sqrt3))

