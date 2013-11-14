
import math
import random

def calc( N = 10000000 ):
    e1 = 0.0
    e2 = 0.0
    e  = 0.0
    for i in range( N ):
        a = random.uniform( 0.0, 1.0 )
        b = random.uniform( 0.0, 1.0 )
        if ( a < b ):
            c = a
        else:
            c = b
        e1 += a
        e2 += b
        e += c
    e1 /= float( N )
    e2 /= float( N )
    e  /= float( N )
    print e1, e2, e


calc()



