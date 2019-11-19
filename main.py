import pyxel
import time

import player
import levels.test_level.test_level

class App:
    draw_delta = 0.0
    update_delta = 0.0

    draw_last_time = time.time()
    update_last_time = time.time()

    player = player.Player()
    
    level = levels.test_level.test_level.TestLevel()
    level_data = None

    def __init__(self, width, height, fps):
        pyxel.init(width, height, fps=fps)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # Delta Time Update
        current_time = time.time()
        self.update_delta = (current_time - self.update_last_time) / 1000.0

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.level_data = self.level.update()
        self.player.update(self.level_data)
        
        # Delta Time Update
        self.update_last_time = current_time

    def draw(self):
        # Delta Time Draw
        current_time = time.time()
        self.draw_delta = (current_time - self.draw_last_time) / 1000.0
        
        pyxel.cls(0)
        self.level.draw()
        self.player.draw(self.level_data)

        # Delta Time Draw
        self.draw_last_time = current_time       


App(256, 256, 24)
