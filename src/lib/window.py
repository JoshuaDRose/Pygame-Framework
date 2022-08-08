import sys
import pygame

class Window:
    """ define main display """
    def __init__(self, size, flags):
        pygame.display.init()
        self.size = size
        self.flags = flags
        self.display = pygame.display.set_mode(self.size, self.flags, 32)
        pygame.display.set_caption(__file__)
        self.display_width, self.display_height = self.size
         

    def exit_window(self, error=0):
        """ remove pygame.display from namespace """
        pygame.display.quit()
        sys.exit(error)


