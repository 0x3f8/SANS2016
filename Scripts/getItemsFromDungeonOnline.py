#/usr/local/bin/python

# Python script using pyexpect to collect Item Descriptions from the SANS Holiday Hack Challenge Dungeon
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
f = open('items.txt', 'w')

# Get a couple of common things out of the way
gdt = "GDT>"
objheader = "OB# DESC1 DESC2 DESCO ACT FLAGS1 FLAGS2 FVL TVL	  SIZE CAPAC ROOM ADV CON  READ"

# Compile the match
# Extracting all the fields gets UGLY, I'll figure it out some other time. All fields appear to be fixed width by my python regexfu is weak in this department
#itemre = re.compile(r'^([\s\d]{3})\s?(-?[\s\d]{4,5})\s?(-?[\s\d]{4,5})\s?(-?[\s\d]{4,5})\s?(-?[\s\d]{3,4})\s?(-?[\s\d]{6,7})\s?(-?[\s\d]{6,7})\s?(-?[\s\d]{2,4}?)\s?([\s\d]{2,4}?)\s?([\s\d]{5,6}?)\s?([\s\d]{5,6}?)\s?([\s\d]{5}?)\s?([\s\d]{4}?)\s?([\s\d]{4}?)\s?([\s\d]{4}?)')
# Just get the item description fields

itemre = re.compile(r'^([\s\d]{3})\s?(-?[\s\d]{4,5})\s?(-?[\s\d]{4,5})\s?(-?[\s\d]{4,5})')

# Connect to the Dungeon
p = pexpect.spawnu('/usr/bin/nc ' + host + " " + port)
p.expect('> *.*')

# Enter Debug Mode
p.send('gdt\r')
p.expect(gdt)


# Loop through all items, get the object descriptions, and put the data in a file in tab delimited format
# Object descriptions appear to be fixed width
# E.g.
# OB# DESC1 DESC2 DESCO ACT FLAGS1 FLAGS2 FVL TVL	  SIZE CAPAC ROOM ADV CON  READ
# 19 -4544-12715     0 103 -32736    128   0   0 10000     2   10   0   0     0

for i in xrange(1,218):
# Get the item and store the entry line in 'item'
    p.send('DO\r')
    p.expect('Limits')
    if debug == 1:
        sys.stdout.write("Checking item " + str(i) + "\n")
    p.send(str(i) + '\r')
    p.expect(objheader + "\r\n")
    p.expect(gdt)
    item = p.before
    if debug == 1:
        sys.stdout.write('Item line is ' + item + "\n")

# Extract the obj number, and three description fields from the item var
    obj = itemre.match(item)
#    objnum, objdesc1, objdesc2, objdesc0, objAct, objFlag1, objFlag2, objFvl, objTvl, objSize, objCapac, objRoom, objAdv, objCon, objRead = obj.groups()
    objnum, objdesc1, objdesc2, objdesc0 = obj.groups()


    p.send('DT\r')
    p.expect('Entry:')
    p.send(objdesc1 + "\r")
    p.expect(objdesc1 + "\r\n")
    p.expect(gdt)
    itemDesc1 = p.before.rstrip('\r\n')
    p.send('DT\r')
    p.expect('Entry:')
    p.send(objdesc2 + "\r")
    p.expect(objdesc2 + "\r\n")
    p.expect(gdt)
    itemDesc2 = p.before.rstrip('\r\n')
    p.send('DT\r')
    p.expect('Entry:')
    p.send(objdesc0 + "\r")
    p.expect(objdesc0 + "\r\n")
    p.expect(gdt)
    itemDesc0 = p.before.rstrip('\r\n')
    f.write(objnum.lstrip(' ') + "\t" + itemDesc1 + "\t" + itemDesc2 + "\t" + itemDesc0 + "\n")
    if debug == 1:
        sys.stdout.write("Descriptions are " + objnum.lstrip('\s') + "\t" + itemDesc1 + "\t" + itemDesc2 + "\t" + itemDesc0)

f.close()
