# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:22:41 2013

@author: z_80
"""

import math
import random
import scipy
import numpy
import scipy.optimize
from sklearn import svm


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

#elementsNumber()

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

    #print "W = ", W
    return W

def func( x, W, convert=False ):
    xx = xLine( x, convert )
    z = 0.
    n = len( W )
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

#calcEinEout( 5, None, False, 1. )
#calcEinEout( 6, None, False, 1. )
#calcEinEout( 7, None, False, 1. )
#calcEinEout( 8, None, False, 1. )
#calcEinEout( 9, None, False, 1. )
print "Task 7: lowest Ein has 8 vs all: [d]"

#calcEinEout( 0, None, True, 1. )
#calcEinEout( 1, None, True, 1. )
#calcEinEout( 2, None, True, 1. )
#calcEinEout( 3, None, True, 1. )
#calcEinEout( 4, None, True, 1. )
print "Task 8: lowest Eout has 1 vs all: [b]"

#for i in range( 10 ):
#    calcEinEout( i, None, False, 1. )
#    calcEinEout( i, None, True,  1. )
#    print ""
print "Task 9: actually none of the answers matches well but let it be the last one: less then 5%: [e]"

#calcEinEout( 1, 5, True, 0.001 )
#calcEinEout( 1, 5, True, 1. )
print "Task 10: two classifiers have the same Eout: [c]"

print "Task 11: answer is [c] - should be horizontal parabola and [c] is the only choise"


x = [ [ 1., 0. ], \
      [ 0., 1. ], \
      [ 0., -1. ], \
      [ -1., 0. ], \
      [ 0., 2. ], \
      [ 0., -2. ], \
      [ -2., 0.] ]
y = [ -1., -1., -1., 1., 1., 1., 1. ]
def kern( x1, x2 ):
    print "x1 = ", x1
    print "x2 = ", x2
    k = []
    for i in range( len( x1 ) ):
        k.append( [] )
        for j in range( len( x2 ) ):
            v = (x1[i][0]*x2[j][0] + x1[i][1]*x2[j][1] + 1.)**2
            k[i].append( v )
            
    print "k = ", k
    return k

def solveSvm():
    clf = svm.SVC( kernel=kern, C=1.0e8 )
    clf.fit( x, y )
    print "support vector inds: ", clf.support_
    
#solveSvm()
print "Task 12: number of support vectors is 5, [c]"



def initPts( N ):
    x = []
    y = []
    for i in range( N ):
        x1, x2 = ( random.uniform( -1., 1. ), random.uniform( -1., 1. ) )
        yy     = x2 - x1 + 0.25*math.sin( 3.1415926535*x1 )
        if ( yy > 0. ):
            yy = 1.
        else:
            yy = -1.
        x.append( [x1, x2] )
        y.append( yy )
    return ( x, y )

def prepareKlusters( N, K ):
    kl = []
    inds = []
    for i in range( N ):
        inds.append( random.randint( 0, K-1 ) )
    return inds
    
def calcMu( x, inds, K ):
    mu = []
    ww  = 0.
    for i in range( K ):
        m = [0., 0.]
        w = 0.
        k = 0
        N = len( inds )
        for j in range( N ):
            if ( inds[j] == i ):
                m[0] += x[j][0]
                m[1] += x[j][1]
                k += 1
        k = float( k )
        m[0] /= k
        m[1] /= k
        mu.append( m )
        
        w = 0.
        for j in range( N ):
            if ( inds[j] == i ):
                x1 = x[j][0] - m[0]
                x2 = x[j][1] - m[1]
                w += math.sqrt( x1**2 + x2**2 )
        w /= k
        ww += w
    return (mu, ww)
    
def clusterIteration( x, inds0, K ):
    N = len( inds0 )
    inds = []
    for k in range( N ):
        inds.append( inds0[k] )

    mu, ww = calcMu( x, inds, K )
    res = False
    changes = 0
    for i in range( N-1 ):
        for j in range( i+1, N ):
            if ( inds[i] != inds[j] ):
                #print "inds[i]/ inds[j]: ", inds[i], inds[j]
                indsNew = []
                for k in range( N ):
                    indsNew.append( inds[k] )
                indsNew[i], indsNew[j] = ( indsNew[j], indsNew[i] )
                #print ""
                #print "inds: ", inds
                #print "indsNew: ", indsNew
                muNew, wwNew = calcMu( x, indsNew, K )
                if ( wwNew < ww ):
                    #print "new value: {0}".format( wwNew )
                    mu, ww = muNew, wwNew
                    inds = indsNew
                    res = True
                    changes += 1
    return ( res, inds, changes )
    
def makeKlusters( x, N, K ):
    inds = prepareKlusters( N, K )
    iter = 0
    while ( True ):
        res, inds, changes = clusterIteration( x, inds, K )
        iter += 1
        #print "{0} iterations performed, improvements made {1}".format( iter, changes )
        if not res:
            break
    return inds
    
def kern( gamma, x, mu ):
    return math.exp( -gamma*(x[0]*mu[0]+x[1]*mu[1] ) )
    
    
    
def solveRbf( x, y, N, K, gamma ):
    # init points
    inds = makeKlusters( x, N, K )
    # calc centers mu[k]
    mu, ww = calcMu( x, inds, K )
    
    Y = numpy.matrix( y )
    Y = numpy.transpose( Y )
    F = []
    
    for i in range( N ):
        f = []
        for j in range( K ):
            f.append( kern( gamma, x[i], mu[j] ) )
        f.append( 1. )
        F.append( f )
    F = numpy.matrix( F )
    
    FT = numpy.transpose( F )
    W = numpy.linalg.matrix_power( FT * F, -1 ) * FT * Y
    
    w = []
    for i in range( K+1 ):
        w.append( W.A[i][0] )

    return mu, w

def rbfPredict( mu, W, gamma, x ):
    sz = len( mu )
    res = 0.
    for i in range( sz ):
        res += W[i] * math.exp( -gamma*(x[0]*mu[i][0] + x[1]*mu[i][1]) )
    res += W[sz]
    if ( res > 0. ):
        return 1.
    else:
        return -1.
    
def solveSvm( x, y, g ):
    N = len( y )
    clf = svm.SVC( kernel='rbf', C=1.0e8, gamma=g )
    clf.fit( x, y )
    rbfEin = 0
#    for i in range( N ):
#        yy = clf.predict( x[i] )
#        if ( yy * y[i] < 0. ):
#            rbfEin += 1
#    rbfEin = float( rbfEin ) / float( N )
#    print "rbfEin = {0:.15f}".format( rbfEin )
    return rbfEin, clf

def calcSvmEin0(N, tries, gamma ):
    cnt = 0
    for i in range( tries ):
        x, y = initPts( N )
        e = solveSvm( x, y, gamma )
        if ( e > 0. ):
            cnt += 1
    cnt = float( cnt ) / float( tries ) * 100.
    print "mean Ein = {0}%".format( cnt )
    return cnt

def svmVsRbf( Ntrain, Ntst, tries, gamma, K ):
    svmWins = 0
    for i in range( tries ):
        xTrain, yTrain = initPts( Ntrain )
        e, clf = solveSvm( xTrain, yTrain, gamma )
        mu, W  = solveRbf( xTrain, yTrain, Ntrain, K, gamma )
        xTst, yTst = initPts( Ntst )
        
        svmEout = 0
        rbfEout = 0
        for j in range( Ntst ):
            yy = clf.predict( xTst[j] )
            if ( yy * yTst[j] < 0. ):
                svmEout += 1
            yy = rbfPredict( mu, W, gamma, xTst[j] )
            if ( yy * yTst[j] < 0. ):
                rbfEout += 1
        if ( svmEout <= rbfEout ):
            svmWins += 1
        print "SVM Eout = {0}, RBF Eout = {1}".format( svmEout, rbfEout )
    svmWins = float( svmWins ) / float( tries ) * 100.
    print "SVM beats RBF in {0:15f}% cases".format( svmWins )
        
        
#calcSvmEin0( 100, 1000, 1.5 )
print "Task 13: SVM with RBF kernel never failes to split in-sample points. So answer is <5%: [a]"

svmVsRbf( 100, 1000, 300, 1.5, 9 )
