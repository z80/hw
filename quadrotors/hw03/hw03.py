import numpy as np

class Pose3D:
    def __init__(self, rotation, translation):
        self.rotation = rotation
        self.translation = translation
        
    def inv(self):
        '''
        Inversion of this Pose3D object
        
        :return inverse of self
        '''
        # TODO: implement inversion
        #inv_rotation = self.rotation
        #inv_translation = self.translation
        r = self.rotation
        t = self.translation
        ir = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
        it = [ 0, 0, 0 ]
        for i in range( 3 ):
            for j in range( 3 ):
                ir[i][j] = r[j][i]
        #print "ir = ", ir
        for i in range( 3 ):
            v = 0.0
            for j in range( 3 ):
                v -= t[j] * ir[i][j]
            it[i] = v
        inv_rotation    = np.array( ir )
        inv_translation = np.array( it )

        return Pose3D(inv_rotation, inv_translation)
    
    def __mul__(self, other):
        '''
        Multiplication of two Pose3D objects, e.g.:
            a = Pose3D(...) # = self
            b = Pose3D(...) # = other
            c = a * b       # = return value
        
        :param other: Pose3D right hand side
        :return product of self and other
        '''
        # TODO: implement multiplication
        r1 = self.rotation
        t1 = self.translation
        r2 = other.rotation
        t2 = other.translation
        a = [ [ r1[0][0], r1[0][1], r1[0][2], t1[0] ],
              [ r1[1][0], r1[1][1], r1[1][2], t1[1] ],
              [ r1[2][0], r1[2][1], r1[2][2], t1[2] ],
              [ 0.0,      0.0,      0.0,      1.0 ] ]
        b = [ [ r2[0][0], r2[0][1], r2[0][2], t2[0] ],
              [ r2[1][0], r2[1][1], r2[1][2], t2[1] ],
              [ r2[2][0], r2[2][1], r2[2][2], t2[2] ],
              [ 0.0,      0.0,      0.0,      1.0 ] ]
        c = [ [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0] ]
        for i in range( 4 ):
            for j in range( 4 ):
                v = 0.0
                for k in range( 4 ):
                    v += a[i][k] * b[k][j]
                c[i][j] = v
        r = np.array( [ [c[0][0], c[0][1], c[0][2]],
                        [c[1][0], c[1][1], c[1][2]],
                        [c[2][0], c[2][1], c[2][2]] ] )
        t = np.array( [ c[0][3], c[1][3], c[2][3] ] )
        
        return Pose3D( r, t )
    
    def __str__(self):
        return "rotation:\n" + str(self.rotation) + "\ntranslation:\n" + str(self.translation.transpose())

def compute_quadrotor_pose(global_marker_pose, observed_marker_pose):
    '''
    :param global_marker_pose: Pose3D 
    :param observed_marker_pose: Pose3D
    
    :return global quadrotor pose computed from global_marker_pose and observed_marker_pose
    '''
    # print global_marker_pose.rotation[0][0]
    # TODO: implement global quadrotor pose computation
    #global_quadrotor_pose = None
    #print "*********************************"
    #print global_marker_pose
    #print "-------------------------"
    #print global_marker_pose.inv()
    #print "-------------------------"
    #print observed_marker_pose
    #print "-------------------------"
    #print global_marker_pose.inv() * observed_marker_pose
    #print "#################################"
    global_quadrotor_pose = global_marker_pose * observed_marker_pose.inv()

    return global_quadrotor_pose

