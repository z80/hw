
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
        #print "Point ", xx, xy
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
                
    #print "XTX: "
    #for i in range( 3 ):
    #    print XTX[i][0], XTX[i][1], XTX[i][2]
        
    #Calc XTY
    XTY = []
    for i in range( 3 ):
        XTY.append( 0 )
        for k in range( ptsCnt ):
            XTY[i] += X[k][i] * Y[k]
            
    #print "XTY: "
    #for i in range( 3 ):
    #    print XTY[i]
            
    # Invert xTx
    invXTX = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    d = XTX[0][0]*(XTX[1][1]*XTX[2][2]-XTX[1][2]*XTX[2][1])+XTX[0][1]*(XTX[1][2]*XTX[2][0]-XTX[1][0]*XTX[2][2])+XTX[0][2]*(XTX[1][0]*XTX[2][1]-XTX[1][1]*XTX[2][0])

    invXTX[0][0] = (XTX[1][1]*XTX[2][2]-XTX[1][2]*XTX[2][1])/d
    invXTX[0][1] = (XTX[0][2]*XTX[2][1]-XTX[0][1]*XTX[2][2])/d
    invXTX[0][2] = (XTX[0][1]*XTX[1][2]-XTX[0][2]*XTX[1][1])/d

    invXTX[1][0] = (XTX[1][2]*XTX[2][0]-XTX[1][0]*XTX[2][2])/d
    invXTX[1][1] = (XTX[0][0]*XTX[2][2]-XTX[0][2]*XTX[2][0])/d
    invXTX[1][2] = (XTX[0][2]*XTX[1][0]-XTX[0][0]*XTX[1][2])/d

    invXTX[2][0] = (XTX[1][0]*XTX[2][1]-XTX[1][1]*XTX[2][0])/d
    invXTX[2][1] = (XTX[0][1]*XTX[2][0]-XTX[0][0]*XTX[2][1])/d
    invXTX[2][2] = (XTX[0][0]*XTX[1][1]-XTX[0][1]*XTX[1][0])/d

    #print "invXTX: "
    #for i in range( 3 ):
    #    print invXTX[i][0], invXTX[i][1], invXTX[i][2]

    #print "Check inv matrix: "
    #A = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    #for i in range( 3 ):
    #    for j in range( 3 ):
    #        for k in range( 3 ):
    #            A[i][j] += XTX[i][k] * invXTX[k][j]
    #for i in range( 3 ):
    #    print A[i][0], A[i][1], A[i][2]
    


    # Multiply W = invXTX * XTY
    W = [ 0, 0, 0]
    for i in range( 3 ):
        for j in range( 3 ):
           W[i] += invXTX[i][j] * XTY[j]

    #print "W: "
    #for i in range( 3 ):
    #    print W[i]

    return ( W, X, Y )

def checkW( line, W, X, Y, ptsCheckCnt ):
    Ein  = 0
    inSamplePts = len( Y )
    for i in range( inSamplePts ):
        y = W[0] + W[1]*X[i][1] + W[2]*X[i][2]
        if ( y * Y[i] < 0.0 ):
            Ein += 1
    Ein = float(Ein)/float(inSamplePts)
        
    Eout = 0
    for i in range( ptsCheckCnt ):
        xx = random.uniform( -1, 1 )
        xy = random.uniform( -1, 1 )
        y  = func( xx, xy, line )
        h  = W[0] + W[1]*xx + W[2]*xy
        if ( h > 0 ):
            h = 1
        else:
            h = -1
        if ( y * h < 0 ):
            Eout += 1
    Eout = float(Eout)/float(ptsCheckCnt)
    return Ein, Eout

def plaImplementation( W, X, Y, triesCnt = 1000, maxIters = 1000000 ):
    N = len( Y )
    iters = 0
    for i in range(maxIters):
        randBase = random.randrange( 0, N )
        matchCnt = 0
        for j in range( N ):
            ind = (randBase + j) % N
            y = W[0] + W[1]*X[ind][1] + W[2]*X[ind][2]
            if ( y * Y[ind] < 0 ):
                W[0] += Y[ind]
                W[1] += X[ind][1] * Y[ind]
                W[2] += X[ind][2] * Y[ind]
                break
            else:
                matchCnt += 1
        iters += 1
        if ( matchCnt >= N ):
            #print "Converged in ", i+1, " iterations"
            break
    #print "PLA iterations number = ", iters
    return iters


def experiment( ptsCnt, ptsCheckCnt, triesCnt = 1000, performPla=0 ):
    Ein = 0
    Eout = 0
    plaIters = 0
    for i in range( triesCnt ):
        line = []
        line.append( random.uniform( -1, 1 ) )
        line.append( random.uniform( -1, 1 ) )
        line.append( random.uniform( -1, 1 ) )
        line.append( random.uniform( -1, 1 ) )
        W, X, Y = calcW( line, ptsCnt )
        #print W
        ein, eout = checkW( line, W, X, Y, ptsCheckCnt )
        if ( performPla > 0 ):
            plaIters += plaImplementation( W, X, Y )
        Ein += ein
        Eout += eout
    Ein = float(Ein)/float(triesCnt)
    Eout = float(Eout)/float(triesCnt)
    plaIters = float(plaIters)/float(triesCnt)
    print "Ein={0:.15f}, Eout={1:.15f}".format( Ein, Eout )
    print "PLA iterations number = {0:.15f}".format( plaIters )


if ( __name__ == '__main__' ):
    PTS_CNT = 100
    PTS_CHECK_CNT = 1000
    TRIES_CNT = 1000
    experiment( PTS_CNT, PTS_CHECK_CNT, TRIES_CNT )

    #PLA iterations cnt
    PTS_CNT = 10
    PTS_CHECK_CNT = 100
    experiment( PTS_CNT, PTS_CHECK_CNT, TRIES_CNT, 1 )


