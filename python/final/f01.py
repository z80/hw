# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:22:41 2013

@author: z_80
"""

import random
import scipy
import numpy
import scipy.optimize


def elementsNumber( N = 10 ):
    z = []
    for i in range( N+1 ):
        for j in range( N+1 ):
            if ( i+j > 0 ) and ( i+j <= N ):
                k = [i, j]
                try:
                    ind = z.index( k )
                except ValueError:
                    print k
                    z.append( k )
    print "dim = ", len( z )

elementsNumber()

print "Task 1: None of the above [e]"

print "Task 2: if H is a set of constant \
real values mean could be another real value \
but not one form the set so it is [b]"

print "Task 4: stochastic noise doesn not \
depend on learning model it is a feature of the \
data, [d]"

print "Task 5: If for lin reg solution constraint is \
satisfied then it is the solution if constrained task \
so it is [a]"

print "Task 6: soft-order constraints for polynomials \
can be converted into augmented error - lecture 12, [b]"

def readDataFile( fname, pos, neg=None ):
    x = []
    y = []
    with open( fname ) as f:
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                line = [float(i) for i in line]
                # Making first value integer.
                line[0] = int( line[0] )
                if ( line[0] == pos ):
                    y.append( [1.0] )
                    x.append( [ line[1], line[2] ] )
                else:
                    if ( neg == None ):
                        y.append( [-1.0] )
                        x.append( [ line[1], line[2] ] )
                    elif ( neg == line[0] ):
                        y.append( [-1.0] )
                        x.append( [ line[1], line[2] ] )
    #print "data size is: {0}".format( len( y ) )
    #print y
    return (x, y)
    
def readInFile( pos, neg=None ):
    x, y = readDataFile( './features.train', pos, neg )
    return ( x, y )

def readOutFile( pos, neg=None ):
    x, y = readDataFile( './features.test', pos, neg )
    return ( x, y )

def loadData( pos, neg=None ):
    xTrain, yTrain = readInFile( pos, neg )
    xTest,  yTest  = readOutFile( pos, neg )
    return xTrain, yTrain, xTest, yTest

def xLine( x, convert=False ):
    if not convert:
        return [ 1., x[0], x[1] ]
    
    X = []
    X.append( 1.0 )
    X.append( x[0] )
    X.append( x[1] )
    X.append( x[0]*x[1] )
    X.append( x[0]*x[0] )
    X.append( x[1]*x[1] )
    return X

def linReg( x, y, convert=False, L=0. ):
    #print "data size = ", len( y )
    Y = numpy.matrix( y )
    X = []
    n = len( x )
    for i in range( n ):
        X.append( xLine( x[i], convert ) )
    X = numpy.matrix( X )
    
    XT = X.transpose()
    # Calc XTX
    XTX = XT * X

    # Lambda.
    if ( L > 0. ):
        if convert:
            n = 6
        else:
            n = 3
        L = numpy.identity( n ) * L
        #print "XTX = ", XTX
        #print "lambda = ", L
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

def func( x, W, convert=False ):
    xx = xLine( x, convert )
    z = 0.
    n = len( xx )
    for i in range( n ):
        z += xx[i]*W[i]
    return z

def calcEinEout( pos, neg=None, convert=False, L = 0. ):
    xTr, yTr, xTst, yTst = loadData( pos, neg )
    Ein = 0
    w = linReg( xTr, yTr, convert, L )
    N = len( yTr )
    for i in range( N ):
        x = xTr[i]
        yy = func( x, w, convert )
        if ( yy * yTr[i] < 0. ):
            Ein += 1
    Ein = float( Ein )
    Ein /= float( N )
    
    Eout = 0
    N = len( yTst )
    for i in range( N ):
        x = xTst[i]
        yy = func( x, w, convert )
        if ( yy * yTst[i] < 0. ):
            Eout += 1
    Eout = float( Eout )
    Eout /= float( N )
    
    if ( neg == None ):
        neg = "all"
    print "{0} vs {1}: Ein = {2:.15f}, Eout = {3:.15f}".format( pos, neg, Ein, Eout )

calcEinEout( 5, None, False, 1. )
calcEinEout( 6, None, False, 1. )
calcEinEout( 7, None, False, 1. )
calcEinEout( 8, None, False, 1. )
calcEinEout( 9, None, False, 1. )















