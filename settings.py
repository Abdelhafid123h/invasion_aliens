class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width=1000
        self.screen_height=700
        self.bg_colors=(230,230,230)
        # Ship settings
        self.ship_speed_factor = 1.5
        self.bullet_speed_fact=1
        self.bullet_width=3
        self.bullet_height=18
        self.bullet_colors=(80,80,80)
        self.bullets_allowed=4
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
