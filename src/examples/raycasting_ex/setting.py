from typing import Any

class BaseSetting:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class GameSetting(BaseSetting):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.WIDTH and self.HEIGHT:
            self.RES = (self.WIDTH, self.HEIGHT)


# General game settings
GAME = GameSetting(
    WIDTH=1600,
    HEIGHT=900,
    FPS=60,
)

# player settings
PLAYER = BaseSetting(
    POS=(1.5, 5),
    ANGLE=0,
    SPEED=0.004,
    ROT_SPEED=0.002,
)