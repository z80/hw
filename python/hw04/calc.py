
import random
import numpy
import numpy.linalg
import math

def randomLine():
    x1 = random.uniform( -1, 1 )
    x2 = x1
    while x2 == x1:
        x2 = random.uniform( -1, 1 )
    y1 = math.sin( 3.1415926535 * x1 )
    y2 = math.sin( 2.1415926535 * x2 )

    X = [ [ x1 ], [ x2 ] ]
    X = numpy.matrix( X )
    Y = [ [ y1 ], [ y2 ] ]
    Y = numpy.matrix( Y )
    #print X
    #print Y

    XT = X.transpose()
    XTX = XT * X
    XTY = XT * Y
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    A = invXTX * XTY
    return A[0][0]

def variance( cnt = 10000 ):
    g = 0.95492965855137
    v = 0.0
    for i in range( cnt ):
        a = randomLine()
        v += 1/2.0 * math.pow( (g - a), 2 ) * 2.0 / 3.0
    v /= float( cnt )
    return v

def funcA( b, x ):
    return b

def funcB( b, x ):
    return b*x

def funcC( b, x ):
    return b[0]*x + b[1]

def funcD( b, x ):
    return b*x*x

def funcE( b, x ):
    return b[0]*x*x + b

def randomPts():
    x1 = random.uniform( -1, 1 )
    x2 = x1
    while x2 == x1:
        x2 = random.uniform( -1, 1 )
    y1 = math.sin( 3.1415926535 * x1 )
    y2 = math.sin( 2.1415926535 * x2 )
    return ( x1, y1, x2, y2 )

def bestFit( x1, y1, x2, y2 ):
    #funcA
    X = [ [1.0], [1.0] ]
    Y = [ [y1], [y2] ]
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    XT = X.transpose()
    XTX = XT * X
    XTY = XT * Y
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    aA = invXTX * XTY

    #funcB
    X = [ [x1], [x2] ]
    Y = [ [y1], [y2] ]
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    XT = X.transpose()
    XTX = XT * X
    XTY = XT * Y
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    aB = invXTX * XTY

    #funcC
    X = [ [1.0, x1], [1.0, x2] ]
    Y = [ [y1], [y2] ]
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    XT = X.transpose()
    XTX = XT * X
    XTY = XT * Y
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    aC = invXTX * XTY

    #duncD
    X = [ [x1*x1], [x2*x2] ]
    Y = [ [y1],    [y2] ]
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    XT = X.transpose()
    XTX = XT * X
    XTY = XT * Y
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    aD = invXTX * XTY
    
    #funcE
    X = [ [1.0, x1*x1], [1.0, x2*x2] ]
    Y = [ [y1],         [y2] ]
    X = numpy.matrix( X )
    Y = numpy.matrix( Y )
    XT = X.transpose()
    XTX = XT * X
    XTY = XT * Y
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    aE = invXTX * XTY

    return (aA, aB, aC, aD, aE)

def findBestFit( cnt=100, intCnt=100 ):
    a = { "a":0.0, "b":0.0, "c":[0.0, 0.0], "d":0.0, "e":[0.0, 0.0] }
    for i in range( cnt ):
        x1, y1, x2, y2 = randomPts()
        w = bestFit( x1, y1, x2, y2 )
        a["a"] += w[0]
        a["b"] += w[1]
        a["c"][0] += w[2][0]
        a["c"][1] += w[2][1]
        a["d"] += w[3]
        a["e"][0] += w[4][0]
        a["e"][1] += w[4][1]
    # This is best fit
    a["a"] /= float(cnt)
    a["b"] /= float(cnt)
    a["c"][0] /= float(cnt)
    a["c"][1] /= float(cnt)
    a["d"] /= float(cnt)
    a["e"][0] /= float(cnt)
    a["e"][1] /= float(cnt)
    print a

    #Calculate out of sample error
    e = [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
    for i in range( cnt ):
        x1, y1, x2, y2 = randomPts()
        w = bestFit( x1, y1, x2, y2 )
        dx = 2.0/intCnt
        for k in range( intCnt ):
            x = -1.0 + 2.0 * k / float(intCnt-1)
            # A
            e[0] += math.fabs( a["a"] - w[0] )
            # B
            e[1] += math.fabs( (a["b"] - w[1]) * x )
            # C
            e[2] += math.fabs( a["c"][0] - w[2][0] + (a["c"][1] - w[2][1])*x )
            # D
            e[3] += math.fabs( (a["d"] - w[3])*x*x )
            # E
            e[4] += math.fabs( a["e"][0] - w[4][0] + (a["e"][1] - w[4][1])*x*x )
    cnt = float(cnt)
    e[0] *= dx/cnt
    e[1] *= dx/cnt
    e[2] *= dx/cnt
    e[3] *= dx/cnt
    e[4] *= dx/cnt
    print e

print variance()
# Variance is 0.2272144, option A for question 6.
findBestFit()
# Minimal out of sample error is for y = a*x. Option B for question 7.
    


