from manimlib import*
script = '''
已知非负数x、y、z满足x+2y-3z=1，x+y-z=2，求S=x+y+z的取值范围.
'''
sip = '''
解：以z为主元
'''


class tm(Scene):
    def construct(self):
        Ques = Text(
            script,
            font='Source Han Sans'
        )
        Ques.scale(0.5)
        self.play(Write(Ques))
        self.play(Ques.animate.move_to(np.array([0, 3, 0])))
        rcg1 = Rectangle(color=GREEN, stroke_width=0.5)
        rcg2 = Rectangle(color=GREEN, stroke_width=0.5)
        rcg1.surround(Ques[13:22], buff=0)
        rcg2.surround(Ques[23:30], buff=0)
        self.play(
            Write(rcg1), Write(rcg2),
            Ques.animate.set_color_by_t2c({
                'x+2y-3z=1': GREEN,
                'x+y-z=2': GREEN
            }),
            run_time=2
        )
        self.wait(0.5)
        equ1 = VGroup(
            Tex("x", "+2y", "-3z", "=", "1"),
            Tex("x", "+y", "-z", "=", "2"),
            Tex("x", "+2y", "=", "3z+1"),
            Tex("x", "+y", "=", "z+2"),
            Tex("x", "=", "-z+3"),
            Tex("y", "=", "2z-1")
        )
        equ1.set_color(GREEN)
        equ1[0].move_to(np.array([0, 0.5, 0]))
        equ1[2].move_to(equ1[0])
        equ1[4].move_to(equ1[2])
        equ1[1].move_to(np.array([0, -0.5, 0]))
        equ1[3].move_to(equ1[1])
        equ1[5].move_to(equ1[3])
        self.play(
            ReplacementTransform(rcg1, equ1[0]),
            ReplacementTransform(rcg2, equ1[1]),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(equ1[0], equ1[2]),
            ReplacementTransform(equ1[1], equ1[3]),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(equ1[2], equ1[4]),
            ReplacementTransform(equ1[3], equ1[5]),
            run_time=2.5
        )
        self.wait(0.5)
        equ2 = VGroup(
            Tex("x", "\\geq", "0"),
            Tex("-z", "+3", "\\geq", "0"),
            Tex("-z", "\\geq", "-3"),
            Tex("z", "\\leq", "3"),
            Tex("y", "\\geq", "0"),
            Tex("2z", "-1", "\\geq", "0"),
            Tex("z", "\\geq", "\\frac12"),
            Tex("\\frac12", "\\leq", "z")
        )
        equ2.set_color(RED)
        equ2[0].move_to(np.array([2, 1, 0]))
        equ2[1].move_to(equ2[0])
        equ2[2].move_to(equ2[1])
        equ2[3].move_to(equ2[2])
        equ2[4].move_to(np.array([-2, 1, 0]))
        equ2[5].move_to(equ2[4])
        equ2[6].move_to(equ2[5])
        equ2[7].move_to(equ2[6])
        self.play(
            equ1[4].animate.next_to(equ2[0], DOWN),
            equ1[5].animate.next_to(equ2[4], DOWN),
            run_time=2
        )
        self.wait(0.5)
        rcg3 = Rectangle(color=RED, stroke_width=0.5)
        rcg3.surround(Ques[3:6], buff=0)
        self.play(
            Write(rcg3),
            Ques.animate.set_color_by_t2c({
                '[3:6]': RED
            }),
            run_time=2.5
        )
        self.play(
            ReplacementTransform(rcg3, equ2[0]),
            ReplacementTransform(rcg3.copy(), equ2[4]),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            Uncreate(equ1[4]),
            Uncreate(equ1[5]),
            Ques.animate.set_color_by_t2c({
                'x+2y-3z=1': WHITE,
                'x+y-z=2': WHITE
            }),
            ReplacementTransform(equ2[0], equ2[1]),
            ReplacementTransform(equ2[4], equ2[5]),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(equ2[1], equ2[2]),
            ReplacementTransform(equ2[5], equ2[6]),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(equ2[2], equ2[3]),
            TransformMatchingTex(equ2[6], equ2[7], path_arc=PI),
            run_time=2.5
        )
        equ3 = VGroup(
            Tex("\\frac12", "\\leq", "z", "\\leq", "3"),
            Tex("1", "\\leq", "2z", "\\leq", "6"),
            Tex("3", "\\leq", "S", "\\leq", "8"),
            Tex("S=", "x+y+z"),
            Tex("S=", "2z+2"),
            Tex("x+y-z=2"),
            Tex("x+y=z+2")
        )
        equ3[0].move_to(UP)
        equ3[1].move_to(equ3[0])
        equ3[2].move_to(equ3[1])
        equ3[5].move_to(DOWN)
        equ3[6].move_to(DOWN)
        equ3.set_color(BLUE)
        self.play(
            Ques.animate.set_color_by_t2c({
                '[3:6]': WHITE
            }),
            ReplacementTransform(VGroup(equ2[3], equ2[7]), equ3[0]),
            run_time=2.5
        )
        self.wait(0.5)
        rcg4 = Rectangle(color=BLUE, stroke_width=0.5)
        rcg4.surround(Ques[32:39], buff=0)
        self.play(
            Write(rcg4),
            Ques.animate.set_color_by_t2c({
                "S=x+y+z": BLUE
            }),
            run_time=2
        )
        self.play(
            ReplacementTransform(rcg4, equ3[3]),
            run_time=2.5
        )
        self.wait(0.5)
        rcg4 = Rectangle(color=BLUE, stroke_width=0.5)
        rcg4.surround(Ques[23:30], buff=0)
        self.play(
            Write(rcg4),
            Ques.animate.set_color_by_t2c({
                "x+y-z=2": BLUE
            }),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(rcg4, equ3[5]),
            run_time=2.5
        )
        self.play(
            ReplacementTransform(equ3[5], equ3[6]),
            run_time=2.5
        )
        self.play(
            ReplacementTransform(equ3[3], equ3[4]),
            Uncreate(equ3[6]),
            Ques.animate.set_color_by_t2c({
                "x+y-z=2": WHITE
            }),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(equ3[0], equ3[1]),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(equ3[1], equ3[2]),
            Uncreate(equ3[4]),
            Ques.animate.set_color_by_t2c({
                "S=x+y+z": WHITE
            }),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(
            equ3[2].animate.move_to(np.array([4.5, -2.5, 0])),
            run_time=2
        )
        self.wait(0.5)
        self.play(Uncreate(equ3[2]))
        equ1 = VGroup(
            Tex("\\begin{cases}x+2y-3z=1\\\\x+y-z=2\\end{cases}"),
            Tex("x+2y=3z+1"),
            Tex("x+y=z+2"),
            Tex("x=-z+3"),
            Tex("y=2z-1")
        )
        equ1.set_color(GREEN)
        equ2 = VGroup(
            Tex("x\\geq0"),
            Tex("-z+3\\geq0"),
            Tex("-z\\geq-3"),
            Tex("z\\leq3"),
            Tex("y\\geq0"),
            Tex("2z-1\\geq0"),
            Tex("z\\geq\\frac12"),
        )
        equ2.set_color(RED)
        equ3 = VGroup(
            Tex("S=x+y+z"),
            Tex("x+y-z=2"),
            Tex("x+y=z+2"),
            Tex("S=2z+2"),
            Tex("\\frac12\\leq z\\leq3"),
            Tex("1\\leq2z\\leq6"),
            Tex("3\\leq S\\leq8")
        )
        equ3.set_color(BLUE)
        slo = Text(sip, font='Source Han Sans',
                   t2c={'[3:8]': GREEN}).scale(0.75)
        slo.move_to(np.array([-4.5, 2, 0]))
        equ1[0].next_to(slo, DOWN)
        equ1[1].next_to(equ1[0], DOWN)
        equ1[2].next_to(equ1[1], DOWN)
        equ1[3].next_to(equ1[2], DOWN)
        equ1[4].next_to(equ1[3], DOWN)
        equ2[0].move_to(np.array([0, 2, 0]))
        equ2[1].next_to(equ2[0], DOWN)
        equ2[2].next_to(equ2[1], DOWN)
        equ2[3].next_to(equ2[2], DOWN)
        equ2[4].next_to(equ2[3], DOWN)
        equ2[5].next_to(equ2[4], DOWN)
        equ2[6].next_to(equ2[5], DOWN)
        equ3[0].move_to(np.array([4.5, 2, 0]))
        equ3[1].next_to(equ3[0], DOWN)
        equ3[2].next_to(equ3[1], DOWN)
        equ3[3].next_to(equ3[2], DOWN)
        equ3[4].next_to(equ3[3], DOWN)
        equ3[5].next_to(equ3[4], DOWN)
        equ3[6].next_to(equ3[5], DOWN)
        self.play(
            Write(slo),
            Write(equ1),
            Write(equ2),
            Write(equ3),
            run_time=2
        )
        self.wait(4)
        self.play(
            Uncreate(Ques),
            Uncreate(slo),
            Uncreate(equ1),
            Uncreate(equ2),
            Uncreate(equ3),
            run_time=2.5
        )
        tfw = Text(
            "Thanks for watching!",
            font='Source Han Sans',
            t2c=({
                'T': PURPLE_A,
                'f': PURPLE_A,
                'w': PURPLE_A
            })
        )
        bgm = Text(
            "BGM:PKey Sounds Label-Adagio for Summer Wind",
            font='Source Han Sans',
            t2c=({
                'BGM': ORANGE,
                'Adagio for Summer Wind': BLUE_B
            })
        ).scale(0.5)
        bgm.move_to(np.array([0, -0.5, 0]))
        self.play(Write(tfw))
        self.play(
            tfw.animate.move_to(np.array([0, 0.5, 0])),
            Write(bgm)
        )
        self.wait(5)
