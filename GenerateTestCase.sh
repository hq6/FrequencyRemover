#!/bin/bash

# Generate a tone with the frequency and length passed in, and write the output
# to standard out. Frequency is in hertz and time is in seconds.
generateTone() {
    frequency=$1
    length=$2
    sox -n -p synth $length sine $frequency rate 44100
}

# Play a tone with the frequency and length passed in.
# Eventually, this take a CSV of tones, combine them and play them.
playTone() {
    frequency=$1
    length=$2
    play -n synth $length sin $frequency rate 44100
}

sox -n -b 16 SingleTone.wav synth 10 sin 525 rate 44100
sox -m <(generateTone 523.25 10) <(generateTone 800 10) -b 16 DualTone.wav
