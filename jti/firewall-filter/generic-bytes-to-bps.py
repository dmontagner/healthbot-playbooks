from __future__ import division
from __future__ import print_function
import sys
import copy

prev_value = {}
prev_time = {}
prev_bps = {}

'''
This function returns used% out of total available
'''
def bytes_to_bps(index_name, bytes_counter, **kwargs):
    global prev_value
    global prev_time
    global prev_bps

    # get present time
    cur_time = kwargs.get('point_time', 0)
    bytes_counter = int(bytes_counter)

    # convert bytes into bits
    # bps = (bytes * 8)
    bits_counter = bytes_counter * 8
    cur_value = bits_counter

    # calculate the time difference
    time_difference = ( cur_time - prev_time.get(index_name, 0) )

    # Calculate data seen in bps
    try:
        bps = ( cur_value - prev_value.get(index_name, 0) ) / time_difference
    except Exception:
        print("error: exception caught!", file=sys.stderr)
        bps = prev_value.get(index_name, 0)

    # update global variables
    prev_value[index_name] = cur_value
    prev_time[index_name] = cur_time

    return bps
