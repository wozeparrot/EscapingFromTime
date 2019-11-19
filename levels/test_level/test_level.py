import levels.level
import levels.test_level.test_level_data

class TestLevel(levels.level.Level):
    def __init__(self):
        self.resource_name = 'test_level/test_level.pyxres'
        self.level = levels.test_level.test_level_data.data
        super().__init__()
    
    def update(self):
        return super().update()
    
    def draw(self):
        return super().draw()