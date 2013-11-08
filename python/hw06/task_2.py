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
                line = [int(i) for i in line]
                inData.append(line)    
    with open( outFile ) as f:
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                line = [int(i) for i in line]
                outData.append(line)    

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

def linReg( x, k=0, wd=0 ):
    X = []
    Y = []
    sz = len(x)
    for i in range( sz ):
        xx = xLine( x[i] )
        X.append( xx )
        y.append( [ x[i][2] ] )
    Y = numpy.matrix( Y )
    X = numpy.matrix( X )
    
    XT = X.transpose()
    # Calc XTX
    XTX = XT * X

    # Lambda.
    if ( wd > 0 ):
        L = numpy.identity( 8 ) * math.pow( 10.0, k )
        XTX = XTX + L
    
    #Calc XTY
    XTY = XT * Y
    
    # Invert xTx
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    
    # Multiply W = invXTX * XTY
    W = invXTX * XTY
    
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
    
    

def inAndOutErrors( wd=0, k = -3 ):
    inX, outX = readData()
    W = linReg( inX, wd, k )
    
    cnt = len( inX )
    Ein = 0.0
    for i in range( cnt ):
        z = func( inX[i], W )
        if ( z * inX[2] < 0.0 ):
            Ein += 1.0
    Ein /= float( cnt )
    
    cnt = len( outX )
    Eout = 0.0
    for i in range( cnt ):
        z = func( outX[i], W )
        if ( z * outX[2] < 0.0 ):
            Eout += 1.0
    Eout /= float( cnt )
    
    print Ein, Eout, k
    return Ein, Eout

inAndOutErrors()
inAndOutErrors( 1, -3 )
inAndOutErrors( 1, 3 )
inAndOutErrors( 1, 2 )
inAndOutErrors( 1, 1 )
inAndOutErrors( 1, 0 )
inAndOutErrors( 1, -1 )
inAndOutErrors( 1, -2 )





    
