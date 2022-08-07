import pygame
import pygame.mixer

class Audio:
    """ sfx channeling, routing & mixing """
    def __init__(self, channels, default_vol=5):
        """ Audio class constructor """
        self.channels = channels

    def play_sound(self, audio, channel):
        """ 
        audio: pygame.mixer.Sound 
        channel: pygame.mixer.Channel
        """
        channel.play(audio)

    def fade_sound(self, audio, channel, duration, start=pygame.time.get_ticks()):
        """ Fade out audio for x duration """
        while pygame.time.get_ticks() < start:
            if channel.volume > 0:
                channel.volume -= .1
                pygame.mixer.Channel(channel).volume(round(channel.volume))

            else:
                break
