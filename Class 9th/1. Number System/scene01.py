from manim import *

# manim scene01.py NumberLineScene01 -pql
# manim scene01.py NumberLineScene01 -r 1080p60 -t high_quality

SPEED_FAST = 1/1.02 # make run_time faster wherever needed

def animate_arcs_on_number_line(scene, number_line, start_num, end_num):
    flag = 1
    if start_num > end_num:
        flag = -1
    elif start_num < end_num:
        flag = 1
    else:
        flag = 0

    # Convert start_num and end_num to points on the number line
    start_point = number_line.number_to_point(start_num)
    end_point = number_line.number_to_point(end_num)

    # Create a list of arcs with unit size of 1
    arcs = []
    for i in range(start_num, end_num, 1*flag):
        start_point = number_line.number_to_point(i)
        end_point = number_line.number_to_point(i + 1*flag)
        arcs.append(Dot(start_point, color=GREEN))
        arc = ArcBetweenPoints(start_point, end_point,  stroke_color=YELLOW) # radius=0.5, angle=-PI*0.85,
        arcs.append(arc)
    end_point = number_line.number_to_point(end_num)   
    arcs.append(Dot(end_point, color=RED))
   
    # Create a list of Create animations for the arcs
    animations = [Create(arc) for arc in arcs]
    # Animate the arcs
    # scene.play(*arcs)
    return animations

class NumberLineScene01(Scene):
    def construct(self):
         # Add title text
        title = Tex("Rational Numbers in number line").scale(1.5)
        self.play(Write(title))

         # Remove title
        self.wait(1)
        self.play(FadeOut(title))


        number_line = NumberLine(
            x_range=[-1, 16], 
            include_numbers=True
            )
       
        self.play(Create(number_line))
        self.play(number_line.animate.scale(0.8).to_edge(LEFT))

        # Locate point 1
        text1 = Text("We want to locate point 1 in number line").to_edge(UP)
        self.play(Write(text1))
        self.wait(1)
        # Create arc1 from 0 to 1
        arc1 = animate_arcs_on_number_line(self, number_line, 0, 1)
        self.play(Succession(*arc1))
        self.wait(1)
        # remove the arc1
        arc1_remove = [arc.mobject for arc in arc1]
        self.play(FadeOut(*arc1_remove))
        self.wait(1)

        # Locate point 10
        text2 = Text("We want to locate point 10 in number line").to_edge(UP)
        self.play(Transform(text1, text2))
        # Create arc2 from 0 to 10
        arc2 = animate_arcs_on_number_line(self, number_line, 0, 10)
        self.play(Succession(*arc2))
        self.wait(1)
        # remove the arc2
        arc2_remove =  [arc.mobject for arc in arc2]
        self.play(FadeOut(*arc2_remove))
        self.wait(1)

        # Extend number line
        text3 = Text("But what about negative numbers?").to_edge(UP)
        self.play(Transform(text1, text3))
        number_line2 = NumberLine(x_range=[-13, 13, 1], include_numbers=True, include_tip=True, tip_length=0.2).scale(0.5)
        
        self.play(Transform(number_line, number_line2))
        self.wait(1)

        # Locate point -2
        text4 = Text("We want to locate point -2 in number line").to_edge(UP)
        self.play(Transform(text1, text4))
        # Create arc3 from 0 to -2
        arc3 = animate_arcs_on_number_line(self, number_line2, 0, -2)
        self.play(Succession(*arc3))
        self.wait(1)
        # remove the arc3 
        arc3_remove = [arc.mobject for arc in arc3]
        self.play(FadeOut(*arc3_remove))
        self.wait(1)

        # Locate point -11
        text5 = Text("We want to locate point -11 in number line").to_edge(UP)
        self.play(Transform(text1, text5))
        # Create arc3 from 0 to -11
        arc4 = animate_arcs_on_number_line(self, number_line2, 0, -11)
        self.play(Succession(*arc4))
        self.wait(1)
        # remove the arc4 and dot4
        arc4_remove = [arc.mobject for arc in arc4]
        self.play(FadeOut(*arc4_remove))
        self.wait(3)

        # Fade out the text and number line at the end of the scene
        self.play(FadeOut(text1), FadeOut(number_line))
        self.wait(3)

# with tempconfig({"quality": "medium_quality", "preview": True}):
#     # scene = ToyExample()
#     scene = NumberLineScene2()
#     scene.render()


class NumberLineWithArrows(NumberLine):
    def __init__(self, x_range=[-1, 1, 1], length=10, **kwargs):
        self.x_min, self.x_max, self.x_step = x_range
        self.length = length

        super().__init__(
            x_range=[self.x_min, self.x_max],
            length=self.length,
            include_numbers=True,
            include_tip=False,
            **kwargs
        )

        self.arrow_left = Arrow(self.get_left, self.get_right, tip_length=0.2, max_stroke_width_to_length_ratio=10000)
        self.arrow_right = Arrow(self.get_right, self.get_left, tip_length=0.2, max_stroke_width_to_length_ratio=10000)
        self.add(self.arrow_left, self.arrow_right)


class NumberLineScene2(Scene):
    def construct(self):
        # Create number line with arrows
        number_line = NumberLineWithArrows(x_range=[0, 15, 1], length=10)
        self.play(Create(number_line))

        self.wait(2)


