from game.casting.actor import Actor


class Bullet(Actor):
    """
    The responsibility of a bullet is to fly across the screen.

    Attributes:
        _message (string): to display the score when the gems or rocks touch the actor player.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        self._velocity_x = 0
        self._velocity_y = 0
        
    def fire(self,robot_velocity_x, robot_velocity_y):
        self._velocity_x -= robot_velocity_x
        self._velocity_y += robot_velocity_y

     