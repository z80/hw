import math
import numpy

def readData():
    inFile = "in.dta"
    outFile = "out.dta"
    inData = []
    outData = []
    with open( inFile ) as f:
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                line = [float(i) for i in line]
                inData.append(line)    
    with open( outFile ) as f:
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                line = [float(i) for i in line]
                outData.append(line)
    return (inData, outData)

def xLine( x ):
    X = []
    X.append( 1.0 )
    X.append( x[0] )
    X.append( x[1] )
    X.append( x[0]*x[0] )
    X.append( x[1]*x[1] )
    X.append( x[0]*x[1] )
    X.append( math.fabs(x[0]-x[1]) )
    X.append( math.fabs(x[0]+x[1]) )
    return X

def linReg( x, cnt=25, wd=0, k=0 ):
    X = []
    Y = []
    #print x
    sz = len(x)
    for i in range( cnt ):
        #print x[i][0]
        #print x[i][1]
        #print x[i][2]
        xx = xLine( x[i] )
        X.append( xx )
        Y.append( [ x[i][2] ] )
    Y = numpy.matrix( Y )
    X = numpy.matrix( X )
    
    XT = X.transpose()
    # Calc XTX
    XTX = XT * X

    # Lambda.
    if ( wd > 0 ):
        lmbd = math.pow( 10.0, k )
        L = numpy.identity( 8 ) * lmbd
        print "lambda = ", lmbd
        XTX = XTX + L
    
    #Calc XTY
    XTY = XT * Y
    
    # Invert xTx
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    
    # Multiply W = invXTX * XTY
    W = invXTX * XTY

    #print "W = "
    #print W
    return W

def func( x, W ):
    xx = xLine( x )
    z = xx[0]*W[0] + \
        xx[1]*W[1] + \
        xx[2]*W[2] + \
        xx[3]*W[3] + \
        xx[4]*W[4] + \
        xx[5]*W[5] + \
        xx[6]*W[6] + \
        xx[7]*W[7]
    return z
    
    

def classificationErr( cnt=25, wd=0, k = -3 ):
    inX, outX = readData()
    #print inX, len( inX )
    W = linReg( inX, cnt, wd, k )
    
    cntTop = len( inX )
    Eval = 0.0
    for i in range( cnt, cntTop ):
        z = func( inX[i], W )
        #print "z = "
        #print z
        if ( z * inX[i][2] < 0.0 ):
            Eval += 1.0
    Eval /= float( cnt )


    cnt = len( outX )
    Eout = 0.0
    for i in range( cnt ):
        z = func( outX[i], W )
        if ( z * outX[i][2] < 0.0 ):
            Eout += 1.0
    Eout /= float( cnt )

    print "k = {0:.15f}".format( k ), ", Eval = {0:.15f}".format( Eval ), ", Eout = {0:.15f}".format( Eout )
    
    return Eval, Eout

classificationErr( 25, 1, 3 )
classificationErr( 25, 1, 4 )
classificationErr( 25, 1, 5 )
classificationErr( 25, 1, 6 )
classificationErr( 25, 1, 7 )

classificationErr( 10, 1, 3 )
classificationErr( 10, 1, 4 )
classificationErr( 10, 1, 5 )
classificationErr( 10, 1, 6 )
classificationErr( 10, 1, 7 )




    
