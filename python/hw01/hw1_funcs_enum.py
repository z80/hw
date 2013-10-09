
import random
N = 8

def score( funcs, index ):
    sc = 0
    for i in range(N):
        matchCnt = 0
        for j in range(3):
            if ( funcs[i][j] == funcs[index][j] ):
                matchCnt += 1
        sc += matchCnt
    return sc

def enumAll():
    funcs = [ [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1,0 ], [1, 1, 1] ]
    sc = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    for i in range( N ):
        sc[i] = score( funcs, i )
        print( "({0} {1} {2}) score: {3}".format( funcs[i][0], funcs[i][1], funcs[i][2], sc[i] ) )

enumAll()
print( "done" )

