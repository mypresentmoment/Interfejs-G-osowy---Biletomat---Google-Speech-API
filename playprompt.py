import wave
import pyaudio
import sys
import winsound

def play_prompt(name):
    winsound.PlaySound(name,winsound.SND_FILENAME)
    print("Odtwarzanie promptu >>>")
