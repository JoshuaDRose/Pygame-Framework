import pygame

class Text(pygame.font.Font):
    """ Used as a supplamentary class for default font to minimize code usage """
    def __init__(self, surface):
        self.font.Font.__init__(self)
        self.fonts = pygame.font.get_fonts()
        self.padding = 5
        self.surface = surface

    def draw_text(self, text, size, font_face=pygame.font.get_default_font(), centered_to_screen=False):
        """ Draw text minimizes usage of various differnt font faces """
        font_face = pygame.font.SysFont(font_face,size)
        rendered_text = font_face.render(text, ((255,255,255)), True, None)
        rendered_surface = pygame.Surface(self.padding + rendered_text.width, self.padding + rendered_text.height)
        rendered_surface.blit(rendered_text, (0, 0))
        if centered_to_screen:
            self.surface.blit(rendered_surface, (self.surface.get_width() / 2 - rendered_surface.width / 2, self.surface.get_height() / 2 - rendered_surface.height / 2))
            return
        self.surface.blit(rendered_surface, (0, 0))
        return

    def is_font_face_installed(self, font_face) -> bool:
        """ Returns true if a face is installed on the default system """
        exists = True
        try:
            assert pygame.font.SysFont(font_face, 1)
        except AssertionError:
            exists = False
        return exists
