
import random
import scipy
import numpy
import scipy.optimize

from sklearn import svm

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
                    y.append( 1.0 )
                    x.append( [ line[1], line[2] ] )
                else:
                    if ( neg == None ):
                        y.append( -1.0 )
                        x.append( [ line[1], line[2] ] )
                    elif ( neg == line[0] ):
                        y.append( -1.0 )
                        x.append( [ line[1], line[2] ] )
    #print "data size is: {0}".format( len( y ) )
    return (x, y)
    
def readInFile( pos, neg=None ):
    x, y = readDataFile( './features.train', pos, neg )
    return ( x, y )

def readOutFile( pos, neg=None ):
    x, y = readDataFile( './features.test', pos, neg )
    return ( x, y )

def trainVsAll( pos ):
    x, y = readInFile( pos )
    clf = svm.SVC( kernel='poly', degree=2, C=0.01 )
    clf = clf.fit( x, y )
    svmSz = len( clf.support_vectors_ )
    Ein = 0
    sz = len( y )
    for i in range( sz ):
        yy = clf.predict( x[i] )
        if ( yy * y[i] < 0.0 ):
            Ein += 1
    Ein = float( Ein )
    Ein /= float( sz )
    print "Ein[{0}] = {1:.15f}, support vectors number is {2}".format( pos, Ein, svmSz )
    
def train( pos, neg, cc=0.01, dd=2, kk='poly' ):
    x, y = readInFile( pos, neg )
    clf = svm.SVC( kernel=kk, degree=dd, C=cc, coef0=0.0, gamma=0.0 )
    clf = clf.fit( x, y )
    svmSz = len( clf.support_vectors_ )

    Ein = 0
    sz = len( y )
    for i in range( sz ):
        yy = clf.predict( x[i] )
        if ( yy * y[i] < 0.0 ):
            Ein += 1
    Ein = float( Ein )
    Ein /= float( sz )
    
    x, y = readOutFile( pos, neg )
    Eout = 0
    sz = len( y )
    for i in range( sz ):
        yy = clf.predict( x[i] )
        if ( yy * y[i] < 0.0 ):
            Eout += 1
    Eout = float( Eout )
    Eout /= float( sz )
    print "Ein[{0}vs{1}] = {2:.15f}, Eout = {3:.15f} support vectors number is {4}".format( pos, neg, Ein, Eout, svmSz )
    
#print "Value versus all other values:"
#for i in range( 10 ):
#    trainVsAll( i )
print "Value against another value:"
train( 1, 5, 2, 0.001 )
train( 1, 5, 5, 0.001 )
train( 1, 5, 2, 0.01 )
train( 1, 5, 5, 0.01 )
train( 1, 5, 2, 0.1 )
train( 1, 5, 5, 0.1 )
train( 1, 5, 2, 1. )
train( 1, 5, 5, 1. )
    
print "Done..."
print "Biggest Ein is for 0"
print "Smallest Ein is for 1"
print "Support vector number difference is 1854"

print "Eout goes down when C goes up"