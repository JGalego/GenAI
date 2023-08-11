"""
Animated scenes for 'A Tour of GenAI'

Want to learn more about Manim CE? See
https://www.manim.community/
"""

from manim import *  # pylint: disable=unused-wildcard-import,wildcard-import

class BayesModels(Scene):
    """
    Explains how Bayes rule connects the two types of statistical models

    Adapted from UMichigan's EECS 498.008 / 598.008 Deep Learning for Computer Vision
    https://www.youtube.com/watch?v=Q3HU2vEhD5Y
    """
    def construct(self):
        self.camera.background_color = WHITE
        bayes_rule=MathTex(
            "P(x|y)", "=", "{P(y|x)", "\\over", "P(y)}", "P(x)",
            color = BLACK
        )
        self.play(Write(bayes_rule))

        font_size = 20
        cg_model_rec = SurroundingRectangle(bayes_rule[0], buff = .1, color=BLUE)
        cg_model_txt = Text("Conditional\nGenerative Model", color=BLUE, font_size=font_size)
        d_model_rec = SurroundingRectangle(bayes_rule[2], buff = .1, color=ORANGE)
        d_model_txt = Text("Discriminative\nModel", color=ORANGE, font_size=font_size)
        prior_rec = SurroundingRectangle(bayes_rule[4], buff = .1, color=GREEN)
        prior_txt = Text("Prior over labels", color=GREEN, font_size=font_size)
        ug_model_rec = SurroundingRectangle(bayes_rule[5], buff = .1, color=PURPLE)
        ug_model_txt = Text("(Unconditional)\nGenerative Model", color=PURPLE, font_size=font_size)

        self.play(
            Create(cg_model_rec),
            Write(cg_model_txt.next_to(cg_model_rec, LEFT)),
        )
        self.wait()

        self.play(
            Unwrite(cg_model_txt),
            Uncreate(cg_model_rec),
            Create(d_model_rec),
            Write(d_model_txt.next_to(d_model_rec, UP)),
        )
        self.wait()

        self.play(
            Unwrite(d_model_txt),
            Uncreate(d_model_rec),
            Create(prior_rec),
            Write(prior_txt.next_to(prior_rec, DOWN)),
        )
        self.wait()

        self.play(
            Unwrite(prior_txt),
            Uncreate(prior_rec),
            Create(ug_model_rec),
            Write(ug_model_txt.next_to(ug_model_rec, RIGHT)),
        )
        self.wait()
