class Settings():
    def __init__(self):
        # screen settings
        self.screen_width = 300
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 5

        # alien settings
        self.alien_speed_factor = 5
        self.alien_interval_factor = 50

        # timer
        self.timer = 0
