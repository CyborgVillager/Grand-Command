# imports includes GC_Source, will have detailed information
from gc_source import *


#Making the window
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Grand Command v2")



# Background Music
pygame.mixer.music.load('Sounds/Background_SoundTrack.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)



# Main Info for GC
from gc_main import *

    


MusicPaused = MainMenu.HomeScreen(pygame, gameDisplay,[font_40,font_50,font_150], clock, MusicPaused)
