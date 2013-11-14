
import math


def meanConst( ro ):
    b = 0.0
    err = 0.0
    # Exclude the first point
    b   += 0.5
    err += 0.5
    # Exclude the middle point
    b   += 0.0
    err += 1.0
    # Exclude the last point
    b   += 0.5
    err += 0.5
    # Final estimation
    b   /= 3.0
    err /= 3.0

    # Actually err is 2/3
    return err

def meanLinear( ro ):
    a = 0.0
    b = 0.0
    err = 0.0
    # Exclude the first point
    err += 2.0/(1.0-ro)
    # Exclude the second point
    err += 1.0
    # Exclude the last point
    err += 2.0/(1.0+ro)

    err /= 3.0
    return err
