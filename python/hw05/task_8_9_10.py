
import math
import random

def twoPtsSeed():
    x11 = random.uniform( -1.0, 1.0 )
    x12 = random.uniform( -1.0, 1.0 )
    x21 = random.uniform( -1.0, 1.0 )
    x22 = random.uniform( -1.0, 1.0 )
    return [x11, x12, x21, x22]

def calcY( x, l ):
    x11 = l[0]
    x12 = l[1]
    x21 = l[2]
    x22 = l[3]
    x2 = x[0] - x11
    y2 = x[1] - x12
    x1 = x21 - x11
    y1 = x22 - x12
    z = x1*y2 - x2*y1
    if ( z > 0.0 ):
        return 1.0
    return -1.0
    
def grad( w, x, y ):
    E0 = -(y*x[0])/( 1.0 + math.exp( y*(w[0]*x[0] + w[1]*x[1] + w[2]) ) )
    E1 = -(y*x[1])/( 1.0 + math.exp( y*(w[0]*x[0] + w[1]*x[1] + w[2]) ) )
    E2 = -(y*1.0)/( 1.0 + math.exp( y*(w[0]*x[0] + w[1]*x[1] + w[2]) ) )
    return (E0, E1, E2)

def logisticStep( w, x, y, n=0.01 ):
    E0, E1, E2 = grad( w, x, y )
    w0 = w[0] - n*E0
    w1 = w[1] - n*E1
    w2 = w[2] - n*E2
    return [ w0, w1, w2 ]
    
def stochasticDescent( Nin=100, Nout = 1000, n = 0.01, maxDiff = 0.01 ):
    
    line = twoPtsSeed()
    w = [ 0.0, 0.0, 0.0 ]
    pts = []
    for i in range( Nin ):
        x = [ random.uniform( -1.0, 1.0 ), random.uniform( -1.0, 1.0 ) ]
        y = calcY( x, line )
        x = [ x[0], x[1], y ]
        pts.append( x )
    # Descent itself.
    iters = 0
    while 1:
        w0 = w
        # generate shuffled array of indices.
        inds = []
        for i in range( Nin ):
            inds.append( i )
        random.shuffle( inds )
        # Provide that shuffled array to learning algorithm.
        for i in range( Nin ):
            ind = inds[ i ]
            xy = pts[ ind ]
            w1 = logisticStep( w0, [xy[0], xy[1]], xy[2], n )
            w0 = w1
        diffX = math.fabs(w1[0]-w[0])
        diffY = math.fabs(w1[1]-w[1])
        diff1 = math.fabs(w1[2]-w[2])
        if ( diffX > diffY ):
            diff = diffX
        else:
            diff = diffY
        if ( diff < diff1 ):
            diff = diff1
        w = w1
        iters += 1
        #print "iter: ", iters, ", diff = ", diff
        if ( diff < maxDiff ):
            break
    
    #Estimating Eout
    Eout = 0.0
    for i in range(Nout):
        x = [ random.uniform( -1.0, 1.0 ), random.uniform( -1.0, 1.0 ) ]
        y = calcY( x, line )
        g = w[2] + w[0]*x[0] + w[1]*x[1]
        if ( g > 0.0 ):
            g = 1.0
        else:
            g = -1.0
        Eout += math.fabs( y - g )
    Eout /= float(Nout)
    #print "Eout = ", Eout
    #print "w = ", w
    #print "line =", line
    return Eout, iters
    
def EoutEstimation( tries = 1000 ):
    done = 0
    Eout = 0.0
    Niters = 0.0
    for i in range( tries ):
        err, iters = stochasticDescent()
        Eout += err
        Niters += float(iters)
        d = 100 * i/(tries-1)
        if ( d != done ):
            print "done ", d, "%"
            done = d
    Eout /= float( tries )
    Niters /= float( tries )
    print "mean Eout = ",   Eout
    print "mean Niters = ", Niters
        
#stochasticDescent()
EoutEstimation()
        
        
        
        
        
        
        
        
