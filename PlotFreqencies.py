import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft
from scipy.io import wavfile
from sys import argv

# FFT sample count
N = 8192

# Sampling frequency
samples_per_second = 44100

# Frequency resolution
freq_resolution = samples_per_second / N

fs, data = wavfile.read(argv[1]) # load the data
a = data.T # Assume single-channel track for now.
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b, N) # calculate fourier transform (complex numbers list)
d = len(c)/2 - 1  # you only need half of the fft list (real signal symmetry)
frequencies = [x*freq_resolution for x in xrange(d)]
print '\n'.join(",".join([str(f),str(x)]) for f, x in zip(frequencies, abs(c[:d])))
plt.plot(frequencies, abs(c[:d]),'r')
plt.show()
