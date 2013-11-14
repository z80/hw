
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
        
    
    
    
def svmSolve( xx, xy, y, doPlot=False ):
    sz = len( y )
    X = []
    Y = []
    for i in range( sz ):
        X.append( [ xx[i], xy[i] ] )
        Y.append( y[i] )
        
    #clf = svm.LinearSVC()
    clf = svm.SVC( kernel='linear', C=1.0E6 )
    clf = clf.fit( X, Y )
    
    
    if ( doPlot ):
        
        xxx = xx
        xxy = xy
        w = clf.coef_[0]
        a = -w[0] / w[1]
        xx = np.linspace( -1.2, 1.2 )
        yy = a * xx - (clf.intercept_[0]) / w[1]
        
        # plot the parallels to the separating hyperplane that pass through the
        # support vectors
        b = clf.support_vectors_[0]
        yy_down = a * xx + (b[1] - a * b[0])
        b = clf.support_vectors_[-1]
        yy_up = a * xx + (b[1] - a * b[0])
        
        # plot the line, the points, and the nearest vectors to the plane
        pl.plot(xx, yy, 'k-')
        pl.plot(xx, yy_down, 'k--')
        pl.plot(xx, yy_up, 'k--')
        
        pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
        print xxx
        print xxy
        pl.scatter( xxx, xxy, s=10, facecolors='none' ) #c=Y, cmap=pl.cm.Paired )
        
        
        pl.axis('tight')
        pl.show()        
    
    
    return clf

    
    
def singleRun( N=10, tests=1000, doPlot=False ):
    xx = []
    xy = []
    g  = []
    w  = [ 0.0, 0.0, 0.0 ]
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
        xx.append( random.uniform( -1., 1. ) )
        xy.append( random.uniform( -1., 1. ) )
        g.append( func( xx[i], xy[i], r1x, r1y, r2x, r2y ) )
        s += g[i]
    if math.fabs( s ) > float(N-1):
        return ( False, None, None )
            
    w = teachPla( xx, xy, g, w )
    s = svmSolve( xx, xy, g, doPlot )
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

def countIters( N = 100, tests = 3000, tries = 1000 ):

    done = 0
    svmBetter = 0
    sup  = 0
    for i in range( tries ):
        res = False
        if i == 0:
            doPlot = True
        else:
            doPlot = False
        while ( not res):
            aaa, d, n = singleRun( N, tests, doPlot )
            res = aaa
        if ( d > 0.0 ):
            svmBetter += 1
        sup  += n
        d = 100 * i / tries
        if ( d != done ):
            done = d
            print "done {0}%".format( d )
    svmBetter /= float( tries )
    svmBetter *= 100.0
    sup   = float( sup ) / float( tries )
    print "svmBetter = {0}%, n = {1}".format( svmBetter, sup )
        


countIters()
#singleRun()
print( "done" )

