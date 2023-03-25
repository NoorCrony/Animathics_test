from manim import *

# manim scene03.py NumberLineScene03 -pql

class NumberLineAnimation03(ZoomedScene):
    def __init__(self, **kwargs):
            ZoomedScene.__init__(
                self,
                zoom_factor=2,
                zoomed_display_height=4,
                zoomed_display_width=10,
                image_frame_stroke_width=1,
                zoomed_camera_config={
                    "default_frame_stroke_width": 3,
                    "background_color": WHITE,
                },
                **kwargs
        )
            

    def construct(self):
        # Create number line
        number_line = NumberLine(x_range=[-2, 5], length=10, include_numbers=True,unit_size=2, color=WHITE)
        
        
        # Create red dot at position 3
        red_dot = Dot().move_to(number_line.number_to_point(3)).set_color(RED)
        
        # Create line from 0 to 3
        line = Line(number_line.number_to_point(0), red_dot.get_center())
        
        # Create ticks on line
        factor = 0.25
        ticks = VGroup()
        for i in range(11):
            tick = VGroup(Line(factor*DOWN, factor*UP), Line(factor*LEFT, factor*RIGHT))
            tick.set_color(BLUE)
            tick.move_to(line.get_start() + i/10*line.get_vector())
            ticks.add(tick)
        
        # Highlight first tick with green dot
        green_dot = Dot().move_to(ticks[1].get_center()).set_color(GREEN)
        
        # Add objects to scene
        self.play(Create(number_line))
        
        
        # Animate objects
        self.play(FadeIn(red_dot))
        self.play(Create(line))
        self.wait()
        
        self.wait(1)
        self.play(Create(ticks), FadeIn(green_dot))
        self.wait()
