import manim as nm
import numpy as np


def get_center(i, pos_L, pos_T):
    return (pos_L[int(i.get_value())] + pos_T[int(i.get_value())]) / 2


def coord_to_screen(coords, center, scale):
    screen_coords = (coords - center) * scale
    return [screen_coords[0], screen_coords[1], 0]


# return np.concatenate((coords - center) * scale, np.array([0]))


class MoonVisualization(nm.Scene):
    def construct(self):
        data = np.load("kepler-moon/data.npz")
        pos_T = data["pos_T"]
        pos_L = data["pos_L"]
        F_S_sur_L = data["F_S_sur_L"]
        F_T_sur_L = data["F_T_sur_L"]
        somme_F_L = data["somme_F_L"]

        scale = 1e-8

        i = nm.ValueTracker(0)

        earth = nm.always_redraw(
            lambda: nm.Circle(radius=0.5, color=nm.BLUE).move_to(
                coord_to_screen(
                    pos_T[int(i.get_value())], get_center(i, pos_L, pos_T), scale
                )
            )
        )
        moon = nm.always_redraw(
            lambda: nm.Circle(radius=0.35, color=nm.RED).move_to(
                coord_to_screen(
                    pos_L[int(i.get_value())], get_center(i, pos_L, pos_T), scale
                )
            )
        )
        self.play(nm.Create(earth), nm.Create(moon))
        self.play(
            i.animate.set_value(pos_T.shape[0] - 1), run_time=30, rate_func=nm.linear
        )
