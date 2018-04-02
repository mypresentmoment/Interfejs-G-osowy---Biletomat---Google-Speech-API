import pyaudio
import wave
from array import array

def rec(length):
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=16000
    CHUNK=1000
    RECORD_SECONDS=length
    FILE_NAME=r"C:\Users\Janek\PycharmProjects\test\resources\answer.wav"

    audio=pyaudio.PyAudio() #instantiate the pyaudio

    #recording prerequisites
    stream=audio.open(format=FORMAT,channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

    #starting recording
    frames=[]

    for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data=stream.read(CHUNK)
        data_chunk=array('h',data)
        vol=max(data_chunk)
        if(vol>=0):
            print("something said")
            frames.append(data)
        else:
            print("nothing")
        print("\n")


    #end of recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    #writing to file
    wavfile=wave.open(FILE_NAME,'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(audio.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))#append frames recorded to file
    wavfile.close()
    return FILE_NAME