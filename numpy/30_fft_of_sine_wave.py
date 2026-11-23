# FFT - the loudest frequency of a sine wave is 5 Hz here.
import numpy as np
def top_freq(signal, rate=100):
    mag = np.abs(np.fft.rfft(signal))
    freqs = np.fft.rfftfreq(len(signal), 1 / rate)
    return float(freqs[np.argmax(mag[1:]) + 1])

if __name__ == "__main__":
    t = np.linspace(0, 1, 100, endpoint=False)
    s = np.sin(2 * np.pi * 5 * t)
    assert abs(top_freq(s) - 5.0) < 1.0
    print("ok")
