#!/usr/bin/env python

import sys
top10=['','','','','','','','','','']
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    for i in range(0,len(words)-1):
        if words[i] in top10:
            for j in range(i+1,len(words)):
                print "%s-%s\t%s" % (words[i],words[j], 1)
