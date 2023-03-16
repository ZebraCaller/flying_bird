import arcade
import random
import time as t

# устанавливаем константы
SCREEN_WIDTH = 1000

SCREEN_HEIGHT = 680
SCREEN_TITLE = "Шаблон"
change_y = 2

# класс с игрой
class BottomColumns(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.right <= 0:
            self.center_x = 1000
            self.center_y = random.randint(0, 140)
            window.score += 1
            

class TopColumns(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x        
        if self.right <= 0:
            self.center_x = 1000
            self.center_y = random.randint(540, 680)
            window.score += 1
            
            
class Penguin(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.25
        self.change_angle -= 0.19
        if self.angle <=-40:
            self.angle = -40
        if self.change_angle <=-5:
            self.change_angle = -5     
        if self.center_y <= 30:
            self.center_y = 30
        self.angle += self.change_angle
        if self.angle >=40:
            self.angle = 40
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = True
        self.background = arcade.load_texture('space.png')
        self.background1 = arcade.load_texture('space1.png')
        self.columns = arcade.SpriteList()
        self.columns1 = arcade.SpriteList()

        self.score = 0
        self.center_x = 0
        self.center_x1 = 1000
        self.change_x = 4
        self.start = t.time()
        self.penguin = Penguin(2)
        self.penguin.texture = arcade.load_texture('penguin1.png')
        self.penguin.textures = []
        self.penguin.textures.append(arcade.load_texture('penguin1.png'))
        self.penguin.textures.append(arcade.load_texture('penguin1.png'))
        self.penguin.textures.append(arcade.load_texture('penguin1.png'))
        self.penguin.textures.append(arcade.load_texture('penguin2.png'))
        self.penguin.textures.append(arcade.load_texture('penguin2.png'))
        self.penguin.textures.append(arcade.load_texture('penguin2.png'))
        self.penguin.textures.append(arcade.load_texture('penguin3.png'))
        self.penguin.textures.append(arcade.load_texture('penguin3.png'))
        self.penguin.textures.append(arcade.load_texture('penguin3.png'))
        self.penguin.center_x = 150
        self.penguin.center_y = 400
#верх + check_for_collision_with_list...
    # начальные значения
    def setup(self):
        for i in range(10):
            column_bottom = BottomColumns('column_bottom.png', 1)
            column_bottom.center_y = random.randint(0, 140)
            column_bottom.center_x = 100*i+1000
            column_bottom.change_x = 4
            self.columns.append(column_bottom)
            column_top = TopColumns('column_top.png', 1)
            column_top.center_y = random.randint(540, 680)
            column_top.center_x = 100*i+1000
            column_top.change_x = 4
            self.columns.append(column_top)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(self.center_x, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_texture_rectangle(self.center_x1, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background1)
        self.penguin.draw()
        self.columns.draw()
        self.columns1.draw()
        if not self.game:
            arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, 50, arcade.color.GRAY)
            arcade.draw_text('RESTART', SCREEN_WIDTH/2 - 31, SCREEN_HEIGHT/2 - 10, arcade.color.WHITE, 15)

        arcade.draw_text(f'score: {int(self.score)}', 900, 650, arcade.color.RED, 20)
            
    def on_mouse_press(self, x, y, button, modifiers):    
        if SCREEN_WIDTH/2 - 50 <= x <= SCREEN_WIDTH/2 + 50 and SCREEN_HEIGHT/2 - 25 <= y <= SCREEN_HEIGHT/2 + 25:
            self.columns = arcade.SpriteList()
            self.setup()
            self.score = 0
#            for collumn in self.columns:
#                collumn.kill()
                
#            for collumn in self.columns1:
#                collumn.kill()
            self.game = True    
        
    # игровая логика
    def update(self, delta_time):
        if self.game:
            self.currient_time = t.time() - self.start
            hits = arcade.check_for_collision_with_list(self.penguin, self.columns)
            if len(hits)>=1:
                self.game = False
            hits = arcade.check_for_collision_with_list(self.penguin, self.columns1)
            if len(hits)>=1:
                self.game = False
            self.center_x -= self.change_x
            self.center_x1 -= self.change_x
            if self.center_x <= -500:
                self.center_x = 1500
            if self.center_x1 <= -500:
                self.center_x1 = 1500    
            self.penguin.update()
            self.penguin.update_animation()
            self.columns.update()
            self.columns1.update()

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.penguin.change_y = 5
            self.penguin.change_angle = 5



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
