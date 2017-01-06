#/usr/local/bin/python

# Python script using pyexpect to collect Room Descriptions from the SANS Holiday Hack Challenge Dungeon
# Standard expect is a little inflexible for this

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import logging
import pexpect
import sys
import re

# Configure the host and port
host = "dungeon.northpolewonderland.com"
port = "11111"

# Begin the madness

debug = 0
f = open('rooms.txt', 'w')

# Get a couple of common things out of the way
gdt = "GDT>"
objheader = "RM#  DESC1  DESC2  EXITS ACTION  VALUE  FLAGS"

# Compile the match

roomre = re.compile(r'^([\s\d+]{3})\s*(-?[\s\d]{,})\s*(-?[\s\d]{3,5})')

# Connect to the Dungeon
p = pexpect.spawnu('/usr/bin/nc ' + host + " " + port)
p.expect('> *.*')

# Enter Debug Mode
p.send('gdt\r')
p.expect(gdt)


# Loop through all rooms, get the descriptions, and put the data in a file in tab delimited format
# Object descriptions appear to be fixed width
# E.g.
# RM#  DESC1  DESC2  EXITS ACTION  VALUE  FLAGS
#  1  -9678  -9693      1      0      5   8192

for i in xrange(1,193):
    # Get the room and store the entry line in 'item'
    p.send('DR\r')
    p.expect('Limits')
    if debug == 1:
        sys.stdout.write("Checking Room " + str(i) + "\n")
    p.send(str(i) + '\r')
    p.expect(objheader + "\r\n")
    p.expect(gdt)
    room = p.before
    if debug == 1:
        sys.stdout.write('Room line is ' + room + "\n")

    # Extract the obj number, and description fields from the item var
    obj = roomre.match(room)
    roomnum, objdesc1, objdesc2 = obj.groups()


    p.send('DT\r')
    p.expect('Entry:')
    p.send(objdesc1 + "\r")
    p.expect(objdesc1 + "\r\n")
    p.expect(gdt)
    roomDesc1 = p.before.rstrip('\r\n')
    p.send('DT\r')
    p.expect('Entry:')
    p.send(objdesc2 + "\r")
    p.expect(objdesc2 + "\r\n")
    p.expect(gdt)
    roomDesc2 = p.before.rstrip('\r\n')
    f.write(roomnum.lstrip(' ') + "\t" + roomDesc1 + "\t" + roomDesc2 + "\n")
    if debug == 1:
        sys.stdout.write("Descriptions are " + roomnum.lstrip('\s') + "\t" + roomDesc1 + "\t" + roomDesc2 + "\r")

f.close()
