class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _score (int): providing the score of the player
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            _score (int): An instance of score
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
       
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        bullet = cast.get_actors("bullets")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        #create artifacts(gems or rocks)

        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        bullets = cast.get_actors("bullets")
        artifacts = cast.get_actors("artifacts")
        

        banner.set_text("score")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        
        for artifact in artifacts:
            for bullet in bullets:
                artifact.move_next(max_x ,max_y) 
                bullet.move_next(max_x,max_y)
                if bullet.get_position().equals(artifact.get_position()):
                    if artifact.get_text() == "O": 
                        message1 = artifact.get_take_point()
                        self._score += message1    
                        cast.remove_actor("artifacts", artifact)
                        cast.remove_actor("bullets", bullet)
                    else:
                        if artifact.get_text() == "*": 
                            message1 = artifact.get_add_point()
                            self._score += message1
                            cast.remove_actor("artifacts", artifact)
                            cast.remove_actor("bullets", bullet)
                        

        banner.set_text(f'score: {self._score}')   
                
        
    def _do_outputs(self, cast): 
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()