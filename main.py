"""
Title: 2 Player Pong
Name: Jonah Honsberger
Date: 12/23/2022
"""

"""
How to Play: move your paddle to block the ball from reaching you wall
and bounce it off your paddle onto the other players wall to score a point

Controls:
WS = Player 1, Green Paddle
Arrow Up Arrow Down = Player 2, Blue Paddle
"""

import arcade, random

SCREENWIDTH, SCREENHEIGHT = arcade.get_display_size()
SCREENTITLE = "2 Player Pong - Jonah H"

MOVEMENT_SPEED = 5

randCount = random.randrange(0, 2)

class TitleView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("2 Player Pong", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("By Jonah H", self.window.width / 2, self.window.height / 2 - 75, arcade.color.WHITE, font_size=35, anchor_x="center")
        arcade.draw_text("Click Enter to Start", self.window.width / 2, self.window.height / 2 - 150, arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            gameview = GameView()
            gameview.__init__()
            self.window.show_view(gameview)

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        colorList = [arcade.color.AMETHYST,
                     arcade.color.AMAZON,
                     arcade.color.AIR_SUPERIORITY_BLUE,
                     arcade.color.ATOMIC_TANGERINE]

        # Choose random background color from colorList
        arcade.set_background_color(random.choice(colorList))

        # Create Player 1
        self.p1 = arcade.Sprite("p1.png", 1)
        self.p1.center_x = 50
        self.p1.center_y = SCREENHEIGHT / 2

        # Create Player 2
        self.p2 = arcade.Sprite("p2.png", 1)
        self.p2.center_x = 1850
        self.p2.center_y = SCREENHEIGHT / 2

        self.score = 0
        self.score_p1 = 0
        self.score_p2 = 0

        # Create Ball
        self.ball = arcade.Sprite("ball.png", 0.2)
        self.ball.center_x = SCREENWIDTH / 2
        self.ball.center_y = SCREENHEIGHT / 2

    def on_draw(self):
       # Start render
        self.clear()
        arcade.start_render()

        # Draw the sprites to the screen
        self.p1.draw()
        self.p2.draw()
        self.ball.draw()

        #p1Text = f"P1 Score: {self.score_p1}"
        #p2Text = f"P2 Score: {self.score_p2}"
        #arcade.draw_text(p1Text, self.window.width - 1800, self.window.height - 50, arcade.color.WHITE, font_size=30, anchor_x="center")
        #arcade.draw_text(p2Text, self.window.width - 130, self.window.height - 50, arcade.color.WHITE, font_size=30, anchor_x="center")

       # if self.ball.center_x == SCREENWIDTH:
       #     print("test")
       #     arcade.draw_text("Balls", self.window.width - 130, self.window.height - 50, arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_update(self, delta_time):
        self.p1.update()
        self.p2.update()
        self.ball.update()

        if randCount == 0:
            self.ball.center_x += 5
        elif randCount == 1:
            self.ball.center_x -= 5

        # Stop P1 from going off screen
        if self.p1.left < 0:
            self.p1.left = 0
        elif self.p1.right > SCREENWIDTH - 1:
            self.p1.right = SCREENWIDTH - 1

        if self.p1.bottom < 0:
            self.p1.bottom = 0
        elif self.p1.top > SCREENHEIGHT - 1:
            self.p1.top = SCREENHEIGHT - 1

        # Stop P2 from going off screen
        if self.p2.left < 0:
            self.p2.left = 0
        elif self.p2.right > SCREENWIDTH - 1:
            self.p2.right = SCREENWIDTH - 1

        if self.p2.bottom < 0:
            self.p2.bottom = 0
        elif self.p2.top > SCREENHEIGHT - 1:
            self.p2.top = SCREENHEIGHT - 1

    def on_key_press(self, key, modifiers):
        # Player 1 Controls
        if key == arcade.key.W:
            self.p1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.p1.change_y = -MOVEMENT_SPEED

        # Player 2 Controls
        if key == arcade.key.UP:
            self.p2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.p2.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
       # Player 1 Controls
        if key == arcade.key.W:
            self.p1.change_y = 0
        elif key == arcade.key.S:
            self.p1.change_y = 0

       # Player 2 Controls
        if key == arcade.key.UP:
            self.p2.change_y = 0
        elif key == arcade.key.DOWN:
            self.p2.change_y = 0

def main():
    window = arcade.Window(SCREENWIDTH, SCREENHEIGHT, SCREENTITLE)
    start_view = TitleView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()