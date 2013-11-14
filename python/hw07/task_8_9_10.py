
import random
import scipy
import numpy
import scipy.optimize

from sklearn import svm


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
    if ( percep( x, y, w ) * g < 0.0 ):
        w[0] += g
        w[1] += x*g
        w[2] += y*g
        return 1
    else:
        return 0

def teachPla( xx, xy, g, w ):
    iters = 0
    while ( 1 ):
        # Count not matching
        notMatch = {}
        ind = 0
        N = len( xx )
        for i in range( N ):
            v = percep( xx[i], xy[i], w )
            if ( v != g[i] ):
                notMatch[ind] = i
                ind += 1
        if ( ind < 1 ):
            #print( "Iterations totally {0}".format(iters) )
            return w

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
    return w
        
    
    
    
def svmSolve( xx, xy, y ):
    sz = len( y )
    X = []
    Y = []
    for i in range( sz ):
        X.append( [ xx[i], xy[i] ] )
        Y.append( y[i] )
        
    #clf = svm.LinearSVC()
    clf = svm.SVC( kernel='linear', gamma=2 )
    clf = clf.fit( X, Y )
    return clf

    
    
def singleRun( N=10, tests=1000 ):
    xx = {}
    xy = {}
    g  = {}
    w  = {}
    w[0] = 0.0
    w[1] = 0.0
    w[2] = 0.0
    r1x = random.uniform( -1., 1. )
    r1y = random.uniform( -1., 1. )
    r2x = random.uniform( -1., 1. )
    r2y = random.uniform( -1., 1. )
    # Setting arrays of initial points.
    s = 0.
    for i in range(N):
        xx[i] = random.uniform( -1., 1. )
        xy[i] = random.uniform( -1., 1. )
        g[i]  = func( xx[i], xy[i], r1x, r1y, r2x, r2y )
        s += g[i]
    if math.fabs( s ) > float(N-1):
        return ( False, None, None )
            
    w = teachPla( xx, xy, g, w )
    s = svmSolve( xx, xy, g )
    #print "support_vectors = ", s.n_support_ 
    #print "support_vectors = ", len( s.support_ )
    
    # Counting error probability
    pE = 0.
    sE = 0.
    for i in range( tests ):
        x1 = random.uniform( -1., 1. )
        x2 = random.uniform( -1., 1. )
        y  = func( x1, x2, r1x, r1y, r2x, r2y )
        v = w[0] + w[1]*x1 + w[2] * x2
        if ( v * y < 0.0 ):
            pE += 1
        v = s.predict( [x1, x2] )
        if ( v * y < 0.0 ):
            sE += 1
    pE = float( pE ) / float( tests ) * 100.0
    sE = float( sE ) / float( tests ) * 100.0
    #print "E(perc) = ", pE
    #print "E(svm)  = ", sE
    diff = pE - sE
    #print "svm is {0}% better".format( diff )
    #print s.support_vectors_
        
    return ( True, diff, len( s.support_ ) )

def countIters( N = 100, tests = 1000, tries = 1000):

    done = 0
    diff = 0.
    sup  = 0
    for i in range( tries ):
        res = False
        while ( not res):
            aaa, d, n = singleRun( N, tests )
            res = aaa
        diff += d
        sup  += n
        d = 100 * i / tries
        if ( d != done ):
            done = d
            print "done {0}%".format( d )
    diff /= float( tries )
    sup   = float( sup ) / float( tries )
    print "Diff = {0}%, n = {1}".format( diff, sup )
        


countIters()
#singleRun()
print( "done" )

