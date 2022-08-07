from dataclasses import dataclass

from pygame import Surface
from pygame.image import load


class spriteSheet:
    """ Load and use spritesheets with a json and png file """
    def __init__(self, filename):
        """ Sprite constructor contains spriterect dataclass """
        self.filename = filename
        self.sprites = image.load(filename).convert_alpha()
    

    def retrieve_sprite(self, rect):
        """
            gets a sprite from a .png file 
            rect takes in [x, y, width, height]
        """
        pass


@dataclass(frozen=True)
class Sprite:
    """
        Similar to pygame.Rect however, with less properties
    """
    x: int
    y: int
    width: int
    height: int
    surface: Surface
    transparent: bool
    center: int
    topleft: int
    topmid: int
    topright: int
    midleft: int
    midright: int
    botleft: int
    botmid: int
    botright: int

    def size(self) -> tuple:
        """ get the size with a different datatype in merging the dimensions """
        return (self.width, self.height)

    def center(self) -> int:
        """ Get the center of a sprite by using its dimensions """
        return (width / 2, height / 2)

    def topleft(self) -> tuple:
        """ topleft position of sprite """
        return (0, 0)
 
    def topmid(self) -> tuple:
        """ top middle position of sprite """
        return (width / 2, 0)

    def topright(self) -> tuple:
        """ top right position of sprite """
        return (width, 0)

    def midleft(self) -> tuple:
        """ middle left position of sprite """
        return (0, height / 2)

    def midright(self) -> tuple:
        """ middle right position of sprite """
        return (width, height/2)
 
    def botleft(self) -> tuple:
        """ bottom left position of sprite """
        return (0, height)

    def botmid(self) -> tuple:
        """ bottom middle position of sprite """
        return (width/2, height)

    def botright(self) -> tuple:
        """ bottom right position of sprite """
        return (width, height)




