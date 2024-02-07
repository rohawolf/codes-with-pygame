import math
from typing import Any

class BaseSetting:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

# General game settings
res_ = width_, height_ = 1600, 900
GAME = BaseSetting(
    WIDTH=width_,
    HEIGHT=height_,
    RES=res_,
    FPS=0, # FPS=60,
)

# player settings
PLAYER = BaseSetting(
    POS=(1.5, 5),
    ANGLE=0,
    SPEED=0.004,
    ROT_SPEED=0.002,
)

# ray casting settings
fov_ = math.pi / 3
num_rays_ = width_ // 2
RAYCASTING = BaseSetting(
    FOV=fov_,
    HALF_FOV=fov_ / 2,
    NUM_RAYS=num_rays_,
    HALF_NUM_RAYS=num_rays_ // 2,
    DELTA_ANGLE=fov_ / num_rays_,
    MAX_DEPTH=20,
)