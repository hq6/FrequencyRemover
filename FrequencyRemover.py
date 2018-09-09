#!/usr/bin/python

import matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft
from scipy.io import wavfile
from sys import argv
import numpy as np

# Remove frequencies with a starting sample of S, a sampling rate of R, N
# samples per block, and B blocks.
def removeFrequencies(infile, outfile, removedFrequencies = list(), S = 0, B = 1, R = 44100, N = 16384, radius = 8):
    # Frequency resolution
    freq_resolution = R * 1.0 / N

    # Read data
    fs, data = wavfile.read(infile)

    for i in range(B):
        start_sample = S + i * N
        end_sample = start_sample + N
        samples = data.T[start_sample:end_sample]

        # FFT
        freq_vectors = rfft(samples, N)
        num_buckets = len(freq_vectors)/2 - 1

        frequencies = [x*freq_resolution for x in xrange(num_buckets)]

        # Manipulate the fft
        for i, freq in enumerate(frequencies):
          for rf in removedFrequencies:
            if abs(freq - rf) < radius:
              # This does't work if i == 0, but we ignore that case
              freq_vectors[2*i-1] = 0
              freq_vectors[2*i] = 0

        # Reverse the FFT
        updated_samples = irfft(freq_vectors)

        # Update samples
        data.T[start_sample:end_sample] = updated_samples

    # Write output
    wavfile.write(outfile, R, data.T)

removeFrequencies(argv[1], argv[2], [525], 32768, N=163840)
