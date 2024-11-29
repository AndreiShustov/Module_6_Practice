import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.05)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x

        if self.top >= SCREEN_HEIGHT or self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.1)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
            # self.ball.change_x = -self.ball.change_x

        self.ball.update()
        self.bar.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 7
        if key == arcade.key.LEFT:
            self.bar.change_x = -7

        if key == arcade.key.UP:
            if self.ball.change_x < 0:
                self.ball.change_x -= 1
                if self.ball.change_x <= -10:
                    self.ball.change_x = -10
            else:
                self.ball.change_x += 1
                if self.ball.change_x >= 10:
                    self.ball.change_x = 10

            if self.ball.change_y < 0:
                self.ball.change_y -= 1
                if self.ball.change_y <= -10:
                    self.ball.change_y = -10
            else:
                self.ball.change_y += 1
                if self.ball.change_y >= 10:
                    self.ball.change_y = 10

        if key == arcade.key.DOWN:
            if self.ball.change_x < 0:
                self.ball.change_x += 1
                if self.ball.change_x == 0:
                    self.ball.change_x = -1
            else:
                self.ball.change_x -= 1
                if self.ball.change_x == 0:
                    self.ball.change_x = 1

            if self.ball.change_y < 0:
                self.ball.change_y += 1
                if self.ball.change_y == 0:
                    self.ball.change_y = -1
            else:
                self.ball.change_y -= 1
                if self.ball.change_y == 0:
                    self.ball.change_y = 1

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
