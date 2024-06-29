import arcade
import arcade.gui
import math
import matplotlib.pyplot as plt
from views.startview import MenuView

screen_width = 350
screen_height = 650
screen_title = "FoodPodApp"
curr_colour = arcade.color.TEAL_GREEN
class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()
        pass

    def setup(self):
        """Set up the app here."""
        pass

    def on_draw(self):
        #Render the screen
        self.clear()
        # set bg color
        arcade.set_background_color(curr_colour)


window = arcade.Window(screen_width, screen_height, screen_title)
menu = MenuView(MyGame())
window.show_view(menu)
arcade.run()