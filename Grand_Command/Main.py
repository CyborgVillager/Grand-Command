from gc_source_mod import *

# Making the window
from gc_window import *

# Global Info
from gc_global_info import *

#Making the window
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Grand Command v2")

# Fonts
from gcfonts import *

# Loading the images
from gc_loadimg import *



# Background Music
pygame.mixer.music.load('Sounds/Background_SoundTrack.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)


# Shorten
from gc_shorten import *


#Checks for all the achviements




    
#Draws all the tiles
from gc_tileinfo import *



# Main Info for GC
from gc_main import *

    


MusicPaused = MainMenu.HomeScreen(pygame, gameDisplay,[font_40,font_50,font_150], clock, MusicPaused)
