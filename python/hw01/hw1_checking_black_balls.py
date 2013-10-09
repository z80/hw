
import random

# Points
N = 100000

def iters():
    balls = [ ['b', 'b'], ['b', 'w'] ]
    bbBalls  = 0
    bxBalls = 0
    for i in range( N ):
        bagIndex = random.randrange( 0, 2 )
        ball1Index  = random.randrange( 0, 2 )
        if ( ball1Index == 0 ):
            ball2Index = 1
        else:
            ball2Index = 0
        if ( balls[bagIndex][ball1Index] == 'b' ):
            # First ball is black
            bxBalls += 1
            if ( balls[bagIndex][ball2Index] == 'b' ):
                # Second is also blask.
                bbBalls += 1
    # probability is N<both black> / N<first black>
    p = float(bbBalls) / float(bxBalls)
    print bbBalls
    print bxBalls
    print( "Probability estimation {0}".format( p ) )


iters()
print( "done" )

