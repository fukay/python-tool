#!/usr/bin/python
import sys

count = 0

for line in iter(sys.stdin.buffer.readline, b''):
    s = ''

    for b in line:
        s += b.to_bytes(1,'big').hex()
        count += 1

        if count % 16 != 0:
            s += ' '
        else:
            s += '\n'

    sys.stdout.write(s)

