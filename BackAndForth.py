import matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft
from scipy.io import wavfile
from sys import argv
import numpy as np

# Sampling frequency
samples_per_second = 44100

# Number of samples
N = 16384

# Starting Sample
S = 16384

# Frequency resolution
freq_resolution = samples_per_second * 1.0 / N

# Read data
fs, data = wavfile.read(argv[1])
samples = data.T[S:S + N]

# FFT
freq_vectors = rfft(samples, N)
num_buckets = len(freq_vectors)/2 - 1

frequencies = [x*freq_resolution for x in xrange(num_buckets)]

# Manipulate the fft
for i, freq in enumerate(frequencies):
    if abs(freq - 524.871826172) < 1:
        # This does't work if i == 0, but we ignore that case
        freq_vectors[2*i-1] = 0
        freq_vectors[2*i] = 0

# Reverse the FFT
updated_samples = irfft(freq_vectors)

# Verify correctness.
print len(updated_samples)
print len(samples)
for x,y in zip(updated_samples, samples):
    if abs(x - y) > 1e-3:
        print x,y

# Write output
data.T[S:S + N] = updated_samples
wavfile.write("Output.wav", samples_per_second, data.T)
