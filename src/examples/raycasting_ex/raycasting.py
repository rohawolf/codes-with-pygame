import math

import pygame as pg

from setting import RAYCASTING

class RayCasting:
    def __init__(self, game, cfg=RAYCASTING):
        self.game = game
        self.cfg = cfg

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - self.cfg.HALF_FOV + 0.0001
        for ray in range(self.cfg.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)


            # horizontals
            y_horz, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_horz = (y_horz - oy) / sin_a
            x_horz = ox + depth_horz * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(self.cfg.MAX_DEPTH):
                tile_horz = (int(x_horz), int(y_horz))
                if tile_horz in self.game.map.world_map:
                    break
                x_horz += dx
                y_horz += dy
                depth_horz += delta_depth
            
            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(self.cfg.MAX_DEPTH):
                tile_vert = (int(x_vert), int(y_vert))
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
            
            depth = min(depth_horz, depth_vert)

            # draw the debug
            pg.draw.line(
                self.game.screen,
                'yellow',
                (ox * 100, oy * 100),
                (
                    100 * ox + 100 * depth * cos_a,
                    100 * oy + 100 * depth * sin_a,
                ),
                2,
            )
            ray_angle += self.cfg.DELTA_ANGLE


    def update(self):
        self.ray_cast()