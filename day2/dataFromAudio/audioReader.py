import os
import wave
import contextlib

script_dir = os.path.dirname(os.path.abspath(__file__))
wav_path = os.path.join(script_dir, "sample.wav")

with contextlib.closing(wave.open(wav_path, "rb")) as f:
    channels = f.getnchannels()
    sample_width = f.getsampwidth()
    framerate = f.getframerate()
    n_frames = f.getnframes()
    duration = n_frames / float(framerate)

    print("Channels:", channels)
    print("Sample width (bytes):", sample_width)
    print("Frame rate (Hz):", framerate)
    print("Number of frames:", n_frames)
    print("Duration (sec):", round(duration, 2))
