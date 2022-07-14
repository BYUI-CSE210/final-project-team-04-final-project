import constants
import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast



from game.directing.director import Director


from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point






def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(constants.FONT_SIZE*2)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 20)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(constants.FONT_SIZE*2)
    robot.set_color(constants.WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    


    for n in range(constants.DEFAULT_ARTIFACTS):
        text = ["*","O"] 
        symbol = random.choice(text)
       
        

        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1,constants.ROWS - 1) 
        
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(symbol)
        artifact.set_font_size(constants.FONT_SIZE*2)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(Point(0,10))
        
        
        cast.add_actor("artifacts", artifact)
       
            
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()