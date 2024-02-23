import math
from typing import Any

class Config:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

# General game settings
res_ = width_, height_ = 1600, 900
half_width_, half_height_ = width_ // 2, height_ // 2

GAME = Config(
    WIDTH=width_,
    HEIGHT=height_,
    HALF_WIDTH=half_width_,
    HALF_HEIGHT=half_height_,
    RES=res_,
    FPS=0, # FPS=60,
)

# player settings
PLAYER = Config(
    POS=(1.5, 5),
    ANGLE=0,
    SPEED=0.004,
    ROT_SPEED=0.002,
)

# ray casting settings

# 
fov_ = math.pi / 3
half_fov_ = fov_ / 2
num_rays_ = width_ // 2
scale_ = width_ // num_rays_
RAYCASTING = Config(
    FOV=fov_,
    HALF_FOV=half_fov_,
    NUM_RAYS=num_rays_,
    HALF_NUM_RAYS=num_rays_ // 2,
    DELTA_ANGLE=fov_ / num_rays_,
    MAX_DEPTH=20,
    SCREEN_DIST=half_width_ / math.tan(half_fov_),
    SCALE=scale_,
)