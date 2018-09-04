import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft
from scipy.io import wavfile
from sys import argv

# Sampling frequency
samples_per_second = 44100

# Number of samples
N = 16384

# Frequency resolution
freq_resolution = samples_per_second * 1.0 / N

# Read data
fs, data = wavfile.read(argv[1])
samples = data.T[N:2* N]

# subtract the mean of the data
mean_sample = sum(samples) * 1.0 / len(samples)
samples = [x - mean_sample for x in samples]
scaled_samples=[(ele/2**16.) for ele in samples]

freq_vectors = fft(scaled_samples, N)
num_buckets = len(freq_vectors)/2 - 1

frequencies = [x*freq_resolution for x in xrange(num_buckets)]

print '\n'.join(",".join([str(f),str(x)]) for f, x in zip(frequencies, abs(freq_vectors[:num_buckets])))
plt.plot(frequencies, abs(freq_vectors[:num_buckets]),'r')
plt.show()
