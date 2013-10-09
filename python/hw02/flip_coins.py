#!/usr/bin/env python
import random
import math

N_COINS = 1000
N_FLIPS = 10

#This function is a stub for your code for the coin flipping simulation, here it just returns three random values for v_1, v_rand, and v_min
def flip_coins(coins, flips):
    firstHeads = 0
    randHeads  = 0
    randIndex = random.randrange( 0, coins )

    v_min = flips
    for i in range( coins ):
        heads = 0
        for j in range( flips ):
            tst = random.randrange( 0, 2 )
            if ( tst == 0 ):
                heads += 1
        if ( i == 0 ):
            v_one = heads
        if ( i == randIndex ):
            v_rnd = heads
        if ( v_min > heads ):
            v_min = heads
    v_one = float(v_one)/float(flips)
    v_rnd = float(v_rnd)/float(flips)
    v_min = float(v_min)/float(flips)
    return ( v_one, v_rnd, v_min )

def hoefdingsCheck( coinsCnt, flipsCnt, repeatsCnt, eFrom, eTo, eSteps ):
    # Get experimental data for P(|Ein-Eout| > e) estimation.
    experiments = []
    vOne  = 0
    vRand = 0
    vMin  = 0
    state = 0
    for i in range( repeatsCnt ):
        v1, vr, vm = flip_coins( coinsCnt, flipsCnt )
        vOne  += v1
        vRand += vr
        vMin  += vm
        experiments.append( [ v1, vr, vm ] )
        newState = 100 * i / repeatsCnt
        if ( newState != state ):
            state = newState
            print( "{0}% experiment done".format( state ) )
    vOne  = float(vOne)/float(repeatsCnt)
    vRand = float(vRand)/float(repeatsCnt)
    vMin  = float(vMin)/float(repeatsCnt)
        
        
    # Check if Hefdings inequality is satisfied.
    E1Ok    = 1
    ErandOk = 1
    EminOk  = 1
    state = 0
    for k in range( eSteps ):
        e = eFrom + (eTo - eFrom)*float(k)/float(eSteps-1)
        Pmax = 2.0 * math.exp( -2 * e * e * flipsCnt )
        P1    = 0
        Prand = 0
        Pmin   = 0
        for i in range( repeatsCnt ):
            # coin1
            if ( math.fabs(experiments[i][0] - 0.5) > e ):
                P1 += 1
            if ( math.fabs(experiments[i][1] - 0.5) > e ):
                Prand += 1
            if ( math.fabs(experiments[i][2] - 0.5) > e ):
                Pmin += 1
        P1    = float( P1 )/float( repeatsCnt )
        Prand = float( Prand )/float( repeatsCnt )
        Pmin  = float( Pmin )/float( repeatsCnt )
        
        if ( P1 > Pmax ):
            if ( E1Ok > 0 ):
                print "Coin 1 failed, Pmax = {0}, measured {1}".format(Pmax, P1)
            E1Ok = 0
        if ( Prand > Pmax ):
            if ( ErandOk > 0 ):
                print "Random coin failed, Pmax = {0}, measured {1}".format(Pmax, Prand)
            ErandOk = 0
        if ( Pmin > Pmax ):
            if ( EminOk > 0 ):
                print "Coin with minimum heads failed, Pmax = {0}, measured {1}".format(Pmax, Pmin)
            EminOk = 0

        #print "i = {0}".format( k )
        newState = 100 * k / eSteps
        if ( newState != state ):
            state = newState
            print( "{0}% verification done, {1}, {2}, {3}, {4}".format( state, P1, Prand, Pmin, Pmax ) )
            
    print "Report"
    if ( E1Ok > 0 ):
        print "Coin1 passed"
    else:
        print "Coin1 failed"
    if ( ErandOk > 0 ):
        print "Random coin passed"
    else:
        print "Random coin failed"
    if ( EminOk > 0 ):
        print "Coin with minimum heads passed"
    else:
        print "Coin with minimum heads failed"
    print "v for first, rand and min are: {0:.15f}, {1:.15f}, {2:.15f}".format( vOne, vRand, vMin )

##tests = int (parameters[0])
##coins = int (parameters[1])
##flip = int (parameters[2])
##
##for t in range (tests):
##    vone, vrnd, vmin = flip_coins (coins, flip)
##    fout.write (str(t) + ',' + str(vone) + ',' + str(vrnd) + ', '+ str(vmin) + '\n')
    
if ( __name__ == '__main__' ):
    REPEATS   = 100000
    COINS_CNT = 1000
    FLIPS_CNT = 10
    
##    print( "Started" )
##    vOne, vRand, vMin = flip_coins( COINS_CNT, FLIPS_CNT )
##    print( "First try ", vOne, vRand, vMin, COINS_CNT, FLIPS_CNT )
##    v1 = 0
##    vr = 0
##    vm = 0
##    state = 0
##    for i in range( REPEATS ):
##        vOne, vRand, vMin = flip_coins( COINS_CNT, FLIPS_CNT )
##        v1 += vOne
##        vr += vRand
##        vm += vm
##        newState = 100 * i / REPEATS
##        if ( newState != state ):
##            state = newState
##            print( "{0}% done".format( state ) )
##    v1 /= float( REPEATS )
##    vr /= float( REPEATS )
##    vm /= float( REPEATS )
##    print( v1, vr, vm )
    hoefdingsCheck( COINS_CNT, FLIPS_CNT, REPEATS, 0.001, 2, 10000 )
    print( "Finished" )
