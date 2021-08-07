from pygame import mixer 

mixer.init()
mixer.music.load('highopes(MP3_160K).mp3')
mixer.music.play()

import time

time.sleep(580)
#necessita do arquivo da música na mesma pasta do arquivo.py