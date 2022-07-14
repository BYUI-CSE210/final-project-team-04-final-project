from game.casting.actor import Actor


class Artifact(Actor):
    """
    The responsibility of an Artifact is to provide points.

    Attributes:
        _message (string): to display the score when the gems or rocks touch the actor player.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
     
    def get_add_point(self):
        """Adds the score by 1
        
        Returns:
            string: The message.
        """
        self._score += 10
        return self._score

    def get_take_point(self):
        """reduces the score by 1.
        
        Returns:
            string: The message.
        """
        self._score -= 5
        return self._score