#!/bin/bash

# Generate a tone with the frequency and length passed in, and write the output
# to standard out. Frequency is in hertz and time is in seconds.
generateTone() {
    frequency=$1
    length=$2
    sox -n -p synth $length sine $frequency
}

# Play a tone with the frequency and length passed in.
# Eventually, this take a CSV of tones, combine them and play them.
playTone() {
    frequency=$1
    length=$2
    play -n synth $length sin $frequency
}

sox -n SingleTone.wav synth 3 sin 523.25
sox -m <(generateTone 523.25 2) <(generateTone 800 2) -b 16 DualTone.wav
