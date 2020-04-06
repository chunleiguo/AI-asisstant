import snowboydecoder
import sys
import signal
import os
from iat_ws_python3 import reco, Ws_Param

interrupted = False

def audioRecorderCallback(fname):
    print("converting audio to text")
    #snowboydecoder.play_audio_file(fname)
    reco(fname)
    #os.remove(fname)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

def detectedCallback():
  #print('recording audio...', end='', flush=True)
  snowboydecoder.play_audio_file('resources/wozai.wav')

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detectedCallback,
	       audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
