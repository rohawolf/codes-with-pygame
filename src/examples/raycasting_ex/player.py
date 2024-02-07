import math

import pygame as pg

from setting import PLAYER

class Player:
    def __init__(self, game, cfg=PLAYER) -> None:
        self.game = game
        self.cfg = cfg
        self.x, self.y = self.cfg.POS
        self.angle = self.cfg.ANGLE

    def move(self) -> None:
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        dx, dy, d_theta = 0, 0, 0
        speed = self.cfg.SPEED * self.game.delta_time
        rotation_speed = self.cfg.ROT_SPEED * self.game.delta_time

        keys = pg.key.get_pressed()
        # default key bindings
        key_bindings = {
            pg.K_w: {'translation': (cos_a, sin_a), 'rotation': 0},
            pg.K_s: {'translation': (-cos_a, -sin_a), 'rotation': 0},
            pg.K_a: {'translation': (sin_a, -cos_a), 'rotation': 0},
            pg.K_d: {'translation': (-sin_a, cos_a), 'rotation': 0},
            pg.K_LEFT: {'translation': (0, 0), 'rotation': -1},
            pg.K_RIGHT: {'translation': (0, 0), 'rotation': 1},
        }
        for key, dynamics in key_bindings.items():
            tr = dynamics['translation']
            if keys[key]:
                dx += tr[0] * speed
                dy += tr[1] * speed
                d_theta += dynamics['rotation'] * rotation_speed
        
        self.angle += d_theta
        self.angle %= 2 * math.pi
        self.check_wall_collision(dx, dy)

    def check_wall(self, x, y) -> bool:
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy) -> bool:
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self) -> None:
        # pg.draw.line(
        #     self.game.screen,
        #     'yellow',
        #     tuple([100 * _ for _ in self.pos]),
        #     (
        #         self.x * 100 + self.game.cfg.WIDTH * math.cos(self.angle)
        #         , self.y * 100 + self.game.cfg.WIDTH * math.sin(self.angle)
        #     ),
        #     2,
        # )
        pg.draw.circle(
            self.game.screen,
            'green',
            tuple([100 * _ for _ in self.pos]),
            15,
        )
     
    def update(self) -> None:
        self.move()
    
    @property
    def pos(self) -> tuple:
        return (self.x, self.y)
    
    @property
    def map_pos(self) -> tuple:
        return (int(self.x), int(self.y))