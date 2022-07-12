from game.casting.actor import Actor
class Bullet(Actor):
    """
    The responsibility of a bullet is to shoot.

    Attributes:
        _message (string): to display the score when the gems or rocks touch the actor player.
    """
    def __init__(self):
        super().__init__()
        self._x_direction = 0.0
        self._y_direction = 0.0
        
        self._velocity._x = 0
        self._velocity._y = 0
        

   # def shoot(self, robot_x, robot_y):
        #self._velocity._x -= robot_x * BULLET_SPEED
      #  self._velocity._y += robot_y * BULLET_SPEED