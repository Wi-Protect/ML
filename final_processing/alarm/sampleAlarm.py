import os

def playAlarm():
    soundPath = "final_processing\alarm\classic-alarm.wav"
    os.system("aplay " + soundPath)

playAlarm()