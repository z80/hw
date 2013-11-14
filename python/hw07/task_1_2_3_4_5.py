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

def xLine( x, sz ):
    X = []
    X.append( 1.0 )
    X.append( x[0] )
    X.append( x[1] )
    X.append( x[0]*x[0] )
    X.append( x[1]*x[1] )
    X.append( x[0]*x[1] )
    X.append( math.fabs(x[0]-x[1]) )
    X.append( math.fabs(x[0]+x[1]) )
    res = X[0:sz+1]
    return res

def linReg( x, sz, cnt=25 ):
    X = []
    Y = []
    #print x
    if ( cnt > 10 ):
        fromInd = 0
        toInd   = 25
    else:
        fromInd = 25
        toInd   = 35
    for i in range( fromInd, toInd ):
        #print x[i][0]
        #print x[i][1]
        #print x[i][2]
        xx = xLine( x[i], sz )
        X.append( xx )
        Y.append( [ x[i][2] ] )
    Y = numpy.matrix( Y )
    X = numpy.matrix( X )
    
    XT = X.transpose()
    # Calc XTX
    XTX = XT * X
    
    #Calc XTY
    XTY = XT * Y
    
    # Invert xTx
    invXTX = numpy.linalg.matrix_power( XTX, -1 )
    
    # Multiply W = invXTX * XTY
    W = invXTX * XTY

    return W

def func( x, W ):
    sz = len( W )
    xx = xLine( x, sz )
    z = 0.0
    for i in range( sz ):
        z += xx[i]*W[i]
    return z
    
    

def classificationErr( sz, cnt=25 ):
    inX, outX = readData()
    #print inX, len( inX )
    W = linReg( inX, sz, cnt )
    #print W
    
    cntTop = len( inX )
    if ( cnt > 10 ):
        fromInd = 0
        toInd   = 25
    else:
        fromInd = 25
        toInd   = 35
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

    print "sz = {0:.15f}".format( sz ), ", Eval = {0:.15f}".format( Eval ), ", Eout = {0:.15f}".format( Eout )
    
    return Eval, Eout

classificationErr( 3, 25 )
classificationErr( 4, 25 )
classificationErr( 5, 25 )
classificationErr( 6, 25 )
classificationErr( 7, 25 )

classificationErr( 3, 10 )
classificationErr( 4, 10 )
classificationErr( 5, 10 )
classificationErr( 6, 10 )
classificationErr( 7, 10 )




    
