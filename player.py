import pyxel

import math

class Player:
    player_frame = 0

    x = 0
    y = 0

    direction = 1
    moving = False

    jumping = False
    jump_timer = 0

    def __init__(self):
        pass

    def update(self, level):
        if level is not None:
            if self.x + 8 + 3 < 255 and level[math.floor((self.y + 8)/16)][int((self.x + 8 + 5)/16)] == 0:
                if pyxel.btn(pyxel.KEY_RIGHT):
                    self.direction = 1
                    self.moving = True
                    self.x += 2
                elif not pyxel.btn(pyxel.KEY_LEFT):
                    self.moving = False
            elif not pyxel.btn(pyxel.KEY_LEFT):
                self.moving = False
            if self.x + 8 - 5 >= 0 and level[math.floor((self.y + 8)/16)][int((self.x + 8 - 6)/16)] == 0:
                if pyxel.btn(pyxel.KEY_LEFT):
                    self.direction = -1
                    self.moving = True
                    self.x -= 2
                elif not pyxel.btn(pyxel.KEY_RIGHT):
                    self.moving = False
            elif not pyxel.btn(pyxel.KEY_RIGHT):
                self.moving = False
            
            if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_LEFT):
                self.moving = False
            
            if pyxel.btnr(pyxel.KEY_RIGHT) or pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_LEFT):
                self.player_frame = 0
            
            if self.y + 8 + 5 < 255:
                if level[math.floor((self.y + 8 + 5)/16)][int((self.x + 8)/16)] == 0:
                    if not self.jumping:
                        self.y += 2
                else:
                    if pyxel.btnp(pyxel.KEY_UP):
                        self.jumping = True
                        self.jump_timer = 0
            else:
                self.x = 0
                self.y = 0

            if self.y + 8 - 5 >= 0:
                if self.jumping is True and self.jump_timer <= 3:
                    self.y -= 4
                    self.jump_timer += 1
                elif self.jumping is True and self.jump_timer <= 6:
                    self.y -= 3
                    self.jump_timer += 1
                elif self.jumping is True and self.jump_timer <= 9:
                    self.y -= 2
                    self.jump_timer += 1
                elif self.jumping is True and self.jump_timer <= 12:
                    self.y -= 1
                    self.jump_timer += 1
                else:
                    self.jump_timer = 0
                    self.jumping = False
            else:
                self.jump_timer = 0
                self.jumping = False

    def draw(self, level):
        pyxel.load("player.pyxres")

        if not self.moving:
            if self.direction > 0:
                if self.player_frame == 0:
                    pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
                elif self.player_frame == 1:
                    pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)
                elif self.player_frame == 2:
                    pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16, 0)
                elif self.player_frame == 3:
                    pyxel.blt(self.x, self.y, 0, 48, 0, 16, 16, 0)
                elif self.player_frame == 4:
                    pyxel.blt(self.x, self.y, 0, 64, 0, 16, 16, 0)
                elif self.player_frame == 5:
                    pyxel.blt(self.x, self.y, 0, 80, 0, 16, 16, 0)
                elif self.player_frame == 6:
                    pyxel.blt(self.x, self.y, 0, 96, 0, 16, 16, 0)
                    self.player_frame = 0
            elif self.direction < 0:
                if self.player_frame == 0:
                    pyxel.blt(self.x, self.y, 0, 0, 0, -16, 16, 0)
                elif self.player_frame == 1:
                    pyxel.blt(self.x, self.y, 0, 16, 0, -16, 16, 0)
                elif self.player_frame == 2:
                    pyxel.blt(self.x, self.y, 0, 32, 0, -16, 16, 0)
                elif self.player_frame == 3:
                    pyxel.blt(self.x, self.y, 0, 48, 0, -16, 16, 0)
                elif self.player_frame == 4:
                    pyxel.blt(self.x, self.y, 0, 64, 0, -16, 16, 0)
                elif self.player_frame == 5:
                    pyxel.blt(self.x, self.y, 0, 80, 0, -16, 16, 0)
                elif self.player_frame == 6:
                    pyxel.blt(self.x, self.y, 0, 96, 0, -16, 16, 0)
                    self.player_frame = 0
        else:
            if self.direction > 0:
                if self.player_frame == 0:
                    pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, 0)
                elif self.player_frame == 1:
                    pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16, 0)
                elif self.player_frame == 2:
                    pyxel.blt(self.x, self.y, 0, 32, 16, 16, 16, 0)
                elif self.player_frame == 3:
                    pyxel.blt(self.x, self.y, 0, 48, 16, 16, 16, 0)
                elif self.player_frame == 4:
                    pyxel.blt(self.x, self.y, 0, 64, 16, 16, 16, 0)
                elif self.player_frame == 5:
                    pyxel.blt(self.x, self.y, 0, 80, 16, 16, 16, 0)
                elif self.player_frame == 6:
                    pyxel.blt(self.x, self.y, 0, 96, 16, 16, 16, 0)
                    self.player_frame = 0
            elif self.direction < 0:
                if self.player_frame == 0:
                    pyxel.blt(self.x, self.y, 0, 0, 16, -16, 16, 0)
                elif self.player_frame == 1:
                    pyxel.blt(self.x, self.y, 0, 16, 16, -16, 16, 0)
                elif self.player_frame == 2:
                    pyxel.blt(self.x, self.y, 0, 32, 16, -16, 16, 0)
                elif self.player_frame == 3:
                    pyxel.blt(self.x, self.y, 0, 48, 16, -16, 16, 0)
                elif self.player_frame == 4:
                    pyxel.blt(self.x, self.y, 0, 64, 16, -16, 16, 0)
                elif self.player_frame == 5:
                    pyxel.blt(self.x, self.y, 0, 80, 16, -16, 16, 0)
                elif self.player_frame == 6:
                    pyxel.blt(self.x, self.y, 0, 96, 16, -16, 16, 0)
                    self.player_frame = 0

        self.player_frame += 1
