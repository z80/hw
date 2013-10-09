#!/usr/bin/env python

import sys
import math
import random
import os
import flip_coins

if len(sys.argv) < 2:
    print "3\nNumber of Tests\t100000\nNumber of Coins\t1000\nFlip\t10"
    sys.exit(0)

#This function is a stub for your code for the coin flipping simulation, here it just returns three random values for v_1, v_rand, and v_min
def flip_coins (coins, flip):
    vone = random.gauss (0.75, 0.05)
    vrnd = random.gauss (0.55, 0.05)
    vmin = random.gauss (0.35, 0.05)
    return (vone, vrnd, vmin)

parameters = [float(x) for x in sys.argv[1:-2]]
row_id = int(sys.argv[-2])
out_file = sys.argv[-1]
tmp_file = out_file + ".tmp"

tests = int (parameters[0])
coins = int (parameters[1])
flip = int (parameters[2])

fout = open (tmp_file, 'w')
fout.write ("Test::number,V_one::number,V_rnd::number,V_min::number\n")
for t in range (tests):
    vone, vrnd, vmin = flip_coins (coins, flip)
    fout.write (str(t) + ',' + str(vone) + ',' + str(vrnd) + ', '+ str(vmin) + '\n')
fout.close ()

os.rename (tmp_file, out_file)
    
    
