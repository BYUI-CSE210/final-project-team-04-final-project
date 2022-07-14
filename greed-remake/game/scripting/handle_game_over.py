from game.casting.cast import Cast
from game.scripting.action import Action
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.shared.point import Point
import constants
class HandleGameOver(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when a snake collides with its segments and the segments of the other snake, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._artifact= Artifact()

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes white if the game is over.
    
        Args:
        cast (Cast): The cast of Actors in the game.
        """
        pass
