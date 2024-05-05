import os

def playAlarm():
    soundPath = "classic-alarm.wav"
    os.system("aplay " + soundPath)

playAlarm()