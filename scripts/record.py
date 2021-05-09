import pyaudio
import numpy as np

def record(duration=3, fs=8000):
    nsamples = duration*fs
    p = pyaudio.PyAudio()
    print("recording")
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True,
                    frames_per_buffer=nsamples)
    buffer = stream.read(nsamples)
    array = np.frombuffer(buffer, dtype='int16')
    stream.stop_stream()
    print("stopped")
    stream.close()
    p.terminate()
    return array

def say(array, fs=8000):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=len(array.shape), rate=fs, output=True)
    stream.write(array.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()