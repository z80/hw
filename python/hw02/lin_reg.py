
import random

N = 100

def func( x, y, line ):
    r1x = line[0]
    r1y = line[1]
    r2x = line[2]
    r2y = line[3]

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


def calcW( line, ptsCnt ):
    X = []
    Y = []
    for i in range( ptsCnt ):
        xx = random.uniform( -1, 1 )
        xy = random.uniform( -1, 1 )
        y  = func( xx, xy, line )
        X.append( [1, xx, xy] )
        Y.append( y )
    # Calc XTX
    XTX = []
    for i in range( 3 ):
        XTX.append( [ 0, 0, 0 ] )
        for j in range( 3 ):
            for k in range( ptsCnt ):
                XTX[i][j] += X[k][i] * X[k][j]
    #Calc XTY
    XTY = []
    for i in range( 3 ):
        XTY.append( 0 )
        for k in range( ptsCnt ):
            XTY[i] += X[k][i] * Y[k]
    # invert xTx
    invXTX = []


    # Multiply W = invXTX * XTY
    W = [ 0, 0, 0]
    for i in range( 3 ):
        for j in range( 3 ):
           W[i] += invXTX[i][j] * XTY[j]

    return W

def checkW( line, W, ptsCheckCnt ):
    Ein = 0
    for i in range( ptsCheckCnt ):
        xx = random.uniform( -1, 1 )
        xy = random.uniform( -1, 1 )
        y  = func( xx, xy, line )
        h  = W[0] + W[1]*xx + W[2]*yy
        if ( h > 0 ):
            h = 1
        else:
            h = -1
        if ( y * h < 0 ):
            Ein += 1
    Ein = float(Ein)/float(ptsCnt)
    return Ein


def experiment( ptsCnt, ptsCheckCnt ):
    line = []
    line.append( random.uniform( -1, 1 ) )
    line.append( random.uniform( -1, 1 ) )
    line.append( random.uniform( -1, 1 ) )
    line.append( random.uniform( -1, 1 ) )
    W = calcW( line, ptsCnt )
    Ein = checkW( line, W, ptsCheckCnt )





