import pyxel

class Level:
    resource_name = ''
    level = None

    def __init__(self):
        pass

    def update(self):
        return self.level

    def draw(self):
        pyxel.load(self.resource_name)
        if self.level is not None:
            for y in range(0, len(self.level)):
                for x in range(0, len(self.level[0])):
                    pyxel.blt(x*16, y*16, 0, self.level[y][x]*16, 0, 16, 16, 0)