
import random
import scipy
import numpy
import scipy.optimize

from sklearn import svm

clf = svm.SVC()

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
        
        
def svmFunc( a, A, X, Y ):
    s = 0.0
    sz = len( a )
    aa = []
    for i in range( sz ):
        s -= a[i]
        aa.append( [ a[i] ] )
    aa = numpy.matrix( aa )
    s += ( aa.transpose() * A * aa ).flat[0] / 2.0
    res = s.flat[0]
    #print "a = ", a
    #print "A = ", A
    #print "X = ", X
    #print "Y = ", Y
    print "Func = ", res
    return res
    
def svmCons( a, A, X, Y ):
    sz = len( a )
    aa = []
    for i in range( sz ):
        aa.append( [ a[i] ] )
    aa = numpy.matrix( aa )
    s = Y.transpose() * aa
    res = s.flat[0]
    print "Contraint = ", res
    return res
    
def svmJac( a, A, X, Y ):
    sz = len( a )
    j = []
    aa = []
    for i in range( sz ):
        j.append( -1.0 )
        aa.append( [ a[i] ] )
    aa = numpy.matrix( aa )
    s = ( aa.transpose() * A )
    for i in range( sz ):
        j[i] += s.flat[i]
    print "Jac = ", j
    return j
    
    
    
def svm( xx, xy, y ):
    sz = len( y )
    X = []
    Y = []
    for i in range( sz ):
        X.append( [ xx[i], xy[i] ] )
        Y.append( [ y[i] ] )
    A = []
    for i in range( sz ):
        line = []
        for j in range( sz ):
            line.append( y[i]*y[j] * ( X[i][0] * X[j][0] + X[i][1] * X[j][1] ) )
        A.append( line )
    A = numpy.matrix( A )
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    
    args = ( A, X, Y )
    cons = { 'type': 'eq', 'fun': svmCons, 'args': args }
    bnds = []
    initial = []
    for i in range( sz ):
        bnds.append( (0, None) )
        initial.append( random.uniform( 0.0, 0.0 ) )
    print "A = "
    print A
    print "X = "
    print X
    print "Y = "
    print Y
    print "Contraints = "
    print cons
    print "Bounds = "
    print bnds
    res = scipy.optimize.minimize( svmFunc, initial, jac=svmJac, args=args, \
                                  method='SLSQP', constraints=cons, \
                                  bounds=bnds, options={ 'maxiter': 3, 'disp':True } )
    print "SVM message is: ", res.message
    print "SVM result is:  ", res.x
    
    
def singleRun( N=5 ):
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
            
    teachPla( xx, xy, g, w )

    a = svm( xx, xy, g )

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


#countIters()
singleRun()
print( "done" )

