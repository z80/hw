
import random

# Points
N = 100

def func( x, y, r1x, r1y, r2x, r2y ):
    ax = x - r1x
    ay = y - r1y
    bx = r1x - r2x
    by = r1y - r2y
    z = ax * by - ay * bx
    if ( z > 0 ):
        z = 1.0
    else:
        z = -1.0
    return z

def percep( x, y, w ):
    v =  w[0] + x * w[1] + y * w[2]
    if ( v > 0 ):
        return 1.0
    else:
        return -1.0

def percepAdj( x, y, g, w ):
    if ( percep( x, y, w ) != g ):
        w[0] += g
        w[1] += x*g
        w[2] += y*g
        return 1
    else:
        return 0

def teach( xx, xy, g, w ):
    iters = 0
    while ( 1 ):
        # Count not matching
        notMatch = {}
        ind = 0
        for i in range( N ):
            v = percep( xx[i], xy[i], w )
            if ( v != g[i] ):
                notMatch[ind] = i
                ind += 1
        if ( ind < 1 ):
            print( "Iterations totally {0}".format(iters) )
            return iters

        cnt = ind
        #print( "iteration # {0}, not matches # {1}".format( iters, cnt ) )
        # Teach
        if ( cnt > 1 ):
            ind = random.randrange( 0, cnt-1 )
        else:
            ind = 0
        ind = notMatch[ind]
        percepAdj( xx[ind], xy[ind], g[ind], w )
        
        iters += 1

def countIters():
    # Tries number
    tries = 1000
    iters = 0

    for k in range( tries ):
        # Initial conditions.
        xx = {}
        xy = {}
        g  = {}
        w  = {}
        w[0] = 0.0
        w[1] = 0.0
        w[2] = 0.0
        r1x = 2.0 * (random.random() - 0.5)
        r1y = 2.0 * (random.random() - 0.5)
        r2x = 2.0 * (random.random() - 0.5)
        r2y = 2.0 * (random.random() - 0.5)
        # Setting arrays of initial points.
        for i in range(N):
            xx[i] = 2.0 * (random.random() - 0.5)
            xy[i] = 2.0 * (random.random() - 0.5)
            g[i]  = func( xx[i], xy[i], r1x, r1y, r2x, r2y )
            
        iters += teach( xx, xy, g, w )
    iters = float(iters)
    iters /= float(tries)
    print( "tries = {0}".format( iters ) )

    # Check perceptron precission.
    tries = 100000
    n = 0
    for i in range( tries ):
        x = 2.0 * (random.random() - 0.5)
        y = 2.0 * (random.random() - 0.5)
        g = func( x, y, r1x, r1y, r2x, r2y )
        f = percep( x, y, w )
        if ( f != g ):
            n += 1
    n = float( n )
    tries = float( tries )
    p = n / tries
    print( "P(f!=g) is {0}".format( p ) )


countIters()
print( "done" )

