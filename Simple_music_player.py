print("If you get any error during run this program Run \npip install pygame\n in terminal and again run it")
from pygame import mixer

mixer.init()
mixer.music.load("samplecontents/house_lo.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("")
    if query == "p":
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == "e":
        mixer.music.stop()
        break