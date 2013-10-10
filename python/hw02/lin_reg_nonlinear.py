
import random
import numpy
import numpy.linalg

N = 100

def func( x1, x2 ):
    f = x1*x1 + x2*x2 - 0.6
    if ( f > 0 ):
        return 1
    return -1


def calcWSimple( ptsCnt ):
    X = []
    Y = []
    for i in range( ptsCnt ):
        x1 = random.uniform( -1, 1 )
        x2 = random.uniform( -1, 1 )
        #print "Point ", xx, xy
        y  = func( x1, x2 )
        X.append( [1, x1, x2] )
        Y.append( [y] )
    # 10% noise
    for i in range( ptsCnt * 10 / 100 ):
        randIndex = random.randrange( 0, ptsCnt )
        Y[randIndex][0] = -Y[randIndex][0]
        
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    XT = X.transpose()
    # Calc XTX
    XTX = XT * X
    
    #Calc XTY
    XTY = XT * Y

    # Invert xTx
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    
    # Multiply W = invXTX * XTY
    W = invXTX * XTY

    #print W
    #print "a, ",  W[0][0]
    #print W[1][0]
    #print W[2][0]
    #print X[2]

    return ( W, X, Y )

def checkEinSimple( W, X, Y ):
    Ein  = 0
    inSamplePts = len( Y )
    for i in range( inSamplePts ):
        y = X[i] * W
        if ( y * Y[i][0] < 0.0 ):
            Ein += 1
    Ein = float(Ein)/float(inSamplePts)
        
    return Ein

def calcWAdv( X, Y ):
    #print "X = ", X
    #print "Y = ", Y
    
    N = len(Y)

    #print "N = ", N
    XX = []
    ex1 = numpy.matrix( [ [0], [1], [0] ] )
    ex2 = numpy.matrix( [ [0], [0], [1] ] )
    for i in range(N):
        x1 = X[i]*ex1
        x2 = X[i]*ex2
        XX.append( [1, x1, x2, x1*x2, x1*x1, x2*x2] )
    XX = numpy.matrix( XX )
    #print "XX = ", XX
    XXT = XX.transpose()
    XXTXX = XXT * XX
    invXXTXX = numpy.linalg.matrix_power( XXTXX, -1 )

    XXTY = XXT * Y

    W = invXXTXX * XXTY
    #print "Adv W = ", W
    return W, XX, Y

def checkEoutAdv( W, outSamplePts ):
    Eout = 0
    for i in range( outSamplePts ):
        x1 = random.uniform( -1, 1 )
        x2 = random.uniform( -1, 1 )
        y  = func( x1, x2 )
        Perr = random.uniform( 0.0, 1.0 )
        if ( Perr < 0.1 ):
            y = -y
        X = numpy.matrix( [ 1, x1, x2, x1*x2, x1*x1, x2*x2 ] )
        #print "X = ", X
        #print "W = ", W
        Y = X * W
        if ( Y * y < 0.0 ):
            Eout += 1
    Eout = float(Eout)/float(outSamplePts)
    #print "Eout = {0:.15f}".format( Eout )
    return Eout

def checkMatch( W, A, ptsCnt ):
    Err = 0
    for i in range( ptsCnt ):
        x1 = random.uniform( -1, 1 )
        x2 = random.uniform( -1, 1 )
        x = [ 1, x1, x2, x1*x2, x1*x1, x2*x2 ]
        x = numpy.matrix( x )
        yw = x * W
        ya = x * A
        if ( yw * ya < 0.0 ):
            Err += 1
    Err = float( Err ) / float( ptsCnt )
    print  "Err = ", Err
    return Err


def experiment( ptsCnt, triesCnt = 1000, outSamplePts = 1000 ):
    Ein = 0
    Eout = 0

    st = 0
    Wmean = numpy.matrix( [ [0], [0], [0], [0], [0], [0] ] )
    for i in range( triesCnt ):
        W, X, Y = calcWSimple( ptsCnt )
        Ein += checkEinSimple( W, X, Y )

        W, XX, YY = calcWAdv( X, Y )
        Eout += checkEoutAdv( W, outSamplePts )
        Wmean += W
        newSt = i * 100 / triesCnt
        if ( newSt != st ):
            st = newSt
            print "{0}% done".format( st )
    Ein = float(Ein)/float(triesCnt)
    Eout = float(Eout)/float(outSamplePts)
    Wmean = Wmean / float(outSamplePts)
    print "Simple   Ein  = {0:.15f}".format( Ein )
    print "Advanced Eout = {0:.15f}".format( Eout )
    print "W mean = ", Wmean
    checkMatch( Wmean, numpy.matrix( [ [-1],[-0.05],[0.08],[0.13],[1.5],[1.5] ] ), outSamplePts )
    checkMatch( Wmean, numpy.matrix( [ [-1],[-0.05],[0.08],[0.13],[1.5],[15] ] ), outSamplePts )
    checkMatch( Wmean, numpy.matrix( [ [-1],[-0.05],[0.08],[0.13],[15],[1.5] ] ), outSamplePts )
    checkMatch( Wmean, numpy.matrix( [ [-1],[-0.05],[0.08],[0.13],[0.05],[0.05] ] ), outSamplePts )
    checkMatch( Wmean, numpy.matrix( [ [-1],[-0.05],[0.08],[1.5],[0.15],[0.15] ] ), outSamplePts )



if ( __name__ == '__main__' ):
    PTS_CNT = 1000
    TRIES_CNT = 1000
    OUT_SAMPLE_PTS = 1000
    experiment( PTS_CNT, TRIES_CNT, OUT_SAMPLE_PTS )




