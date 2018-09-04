# Frequency Remover

This tool is under development with the purpose of making it easy to remove
certian frequencies from certain fragments of audio directly from the command
line in a scriptable fashion. The intended interface is something like the following, although this CLI is by no means set in stone.


    ./FrequencyRemover <input_audio> <output_audio> <list_of_freq_ranges> [start_time] [end_time]
