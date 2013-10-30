
#import numpy.float128
import math

def E( u, v ):
    print "at => ", u, v
    res = math.pow( ( u*math.exp(v) - 2.0*v*math.exp(-u) ), 2 )
    return res

def grad( u, v ):
    dEdu = 2.0*( u*math.exp(v) - 2.0*v*math.exp(-u) )*( math.exp(v) + 2.0*v*math.exp(-u) )
    dEdv = 2.0*( u*math.exp(v) - 2.0*v*math.exp(-u) )*( u*math.exp(v) - 2.0*math.exp(-u) )
    return (dEdu, dEdv)
    
def step( u, v, n=0.1 ):
    a, b = grad( u, v )
    a *= n
    b *= n
    return ( u-a, v-b )
    
def stepU( u, v, n=0.1 ):
    a, b = grad( u, v )
    a *= n
    return ( u-a, v )

def stepV( u, v, n=0.1 ):
    a, b = grad( u, v )
    b *= n
    return ( u, v-b )

def descent( u0, v0, n = 0.1, e=1.0e-14 ):
    iters = 0
    u = u0
    v = v0
    while 1:
        u, v = step( u, v, n )
        err = E( u, v )
        iters += 1
        print err, iters
        if ( err < e ):
            break
        
def gradDescent( u0, v0, n=0.1, iters=15 ):
    u = u0
    v = v0
    for i in range( iters ):
        u, v = stepU( u, v, n )
        u, v = stepV( u, v, n )
        err = E( u, v )
        print "E = ", err
        
    
descent( 1.0, 1.0 )
gradDescent( 1.0, 1.0 )
