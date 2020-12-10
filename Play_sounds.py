import winsound

def playsound(frequency, duration):
    """
    Frequency : Hertz
    Duration : Millisecodes
    """
    winsound.Beep(frequency, duration)

def melody():
    """
    Add frequency with time duration
    """
    playsound(1500, 400)
    playsound(1000, 200)
    playsound(1350, 100)
    playsound(1350, 100)
    playsound(1200, 200)
if __name__ == "__main__":
    melody()