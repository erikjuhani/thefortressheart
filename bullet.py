from pygame import draw

import math

class Bullet:
    def __init__(self, targetx, targety, x, y, speed, dmg, color, melee, size, timer):
        self.speed = speed
        self.x = int(x + 0.5)
        self.y = int(y + 0.5)
        self.tx = targetx
        self.ty = targety
        self.size = size
        self.dir_x = 0
        self.dir_y = 0
        self.calc_movement()
        self.distance = 0
        self.dmg = dmg
        self.melee = melee
        self.color = color
        self.remove = False
        self.timer = timer

    def calc_movement(self):
        xv = self.tx - self.x
        yv = self.ty - self.y
        self.distance = math.sqrt(xv*xv + yv*yv)
        if self.distance == 0:
            self.dir_x = xv
            self.dir_y = yv
        else:
            self.dir_x = xv/self.distance
            self.dir_y = yv/self.distance

    def update(self, dt):
        self.x += self.dir_x * self.speed * dt
        self.y += self.dir_y * self.speed * dt
        self.timer -= 1 * self.speed * dt

    def draw(self, screen, xoff, yoff):
        draw.ellipse(screen, self.color, ((self.x+xoff) * self.size, (self.y+yoff) * self.size, self.size//2-1, self.size//2-1))
