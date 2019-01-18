#!/usr/bin/python

import binascii
import sys
import string

row_num = 0

for line in iter(sys.stdin.readline, ""):
    row_num += 1
    hex_str = line.replace(' ', '').replace('\r', '').replace('\n', '')

    if len(hex_str) % 2 != 0 :
        sys.stderr.write('input is not hex string. row=' + str(row_num) + ', line=' + line)
        exit(-1)

    if set(hex_str).issubset(string.hexdigits):
        sys.stdout.buffer.write(binascii.unhexlify(hex_str))
    else:
        sys.stderr.write('input is not hex string. row=' + str(row_num) + ', line=' + line)
        exit(-2)

exit(0)

