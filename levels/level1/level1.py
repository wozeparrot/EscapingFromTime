import levels.level
import levels.level1.level1_data

class Level1(levels.level.Level):
    def __init__(self):
        self.resource_name = 'level1/level1.pyxres'
        self.level = levels.level1.level1_data.data
        super().__init__()
    
    def update(self):
        return super().update()
    
    def draw(self):
        return super().draw()