import math
import numpy as np
from plot import plot, plot_trajectory, plot_covariance_2d

class UserCode:
    def __init__(self):
        # 3x3 state covariance matrix
        self.sigma = 0.01 * np.identity(3) 

        pos_noise_std = 0.01
        yaw_noise_std = 0.01
        self.Q = np.array([
            [pos_noise_std*pos_noise_std,0,0],
            [0,pos_noise_std*pos_noise_std,0],
            [0,0,yaw_noise_std*yaw_noise_std]
        ])

        #measurement noise
        z_pos_noise_std = 0.01
        z_yaw_noise_std = 0.01
        self.R = np.array([
            [z_pos_noise_std*z_pos_noise_std,0,0],
            [0,z_pos_noise_std*z_pos_noise_std,0],
            [0,0,z_yaw_noise_std*z_yaw_noise_std]
        ])
        # state vector [x, y, yaw] in world coordinates
        self.x = np.zeros((3,1))
        self.markers = self.get_markers()
        self.sp = self.markers[0]
        self.markerInd = 0
        
    def get_markers(self):
        '''
        place up to 30 markers in the world
        '''
        markers = [
             [0, 0], # marker at world position x = 0, y = 0
             [1.5, 0.5],  # marker at world position x = 2, y = 0
             [4.5, 0.5],
             [1.5, 3.5],
             [4.5, 3.5],
             [7.0, 5.5], 
             [4.0, 5.5],
             [4.0, 8.5],
             [7.0, 8.5],
             [10.0,9.5],
             [9.5,11.0],
             [10.0,12.5],
             [8.0,11.0],
             [6.0,11.0]
        ]
        
        #TODO: Add your markers where needed


        
        return markers
        
    def state_callback(self, t, dt, linear_velocity, yaw_velocity):
        '''
        called when a new odometry measurement arrives approx. 200Hz
    
        :param t - simulation time
        :param dt - time difference this last invocation
        :param linear_velocity - x and y velocity in local quadrotor coordinate frame (independet of roll and pitch)
        :param yaw_velocity - velocity around quadrotor z axis (independet of roll and pitch)

        :return tuple containing linear x and y velocity control commands in local quadrotor coordinate frame (independet of roll and pitch), and yaw velocity
        '''
        
        #return np.ones((2,1)) * 0.1, 0

        eps = 0.2
        
        if ( self.abs( self.x[0] - self.sp[0] ) < eps ) and ( self.abs( self.x[1] - self.sp[1] ) < eps ):
            self.markerInd = (self.markerInd + 1) % len( self.markers )
            self.sp = self.markers[ self.markerInd ]
        
        self.x = self.predictState(dt, self.x, linear_velocity, yaw_velocity)

        dx = self.sp[0] - self.x[0]
        dy = self.sp[1] - self.x[1]
        A = self.rotation( self.x[2] ).T
        r = np.array( [ dx, dy ] ).T
        r = np.dot( A, r )
        dx = r[0]
        dy = r[1]
        da = math.atan2( dy, dx ) - self.x[2]

        # xy control gains
        Kp_xy = 1 # xy proportional
        Kd_xy = 0.5 # xy differential
        
        # height control gains
        Kp_z  = 0.1 # z proportional
        Kd_z  = 0.5 # z differential
        
        self.Kp = np.array([[Kp_xy, Kp_xy, Kp_z]]).T
        self.Kd = np.array([[Kd_xy, Kd_xy, Kd_z]]).T

        ux = Kp_xy * dx
        uy = Kp_xy * dy
        ua = Kp_z  * da

        #print( self.markerInd, self.sp[0], self.sp[1], self.x[0], self.x[1], da )
        

        return np.array( [ ux, uy ] ), ua

    def measurement_callback(self, marker_position_world, marker_yaw_world, marker_position_relative, marker_yaw_relative):
        '''
        called when a new marker measurement arrives max 30Hz, marker measurements are only available if the quadrotor is
        sufficiently close to a marker
            
        :param marker_position_world - x and y position of the marker in world coordinates 2x1 vector
        :param marker_yaw_world - orientation of the marker in world coordinates
        :param marker_position_relative - x and y position of the marker relative to the quadrotor 2x1 vector
        :param marker_yaw_relative - orientation of the marker relative to the quadrotor
        '''
        #pass

        z = np.array([[marker_position_relative[0], marker_position_relative[1], marker_yaw_relative]]).T
        z_predicted = self.predictMeasurement(self.x, marker_position_world, marker_yaw_world)
                
        H = self.calculatePredictMeasurementJacobian(self.x, marker_position_world, marker_yaw_world)
        K = self.calculateKalmanGain(self.sigma, H, self.R)
        
        self.x = self.correctState(K, self.x, z, z_predicted)
        self.sigma = self.correctCovariance(self.sigma, K, H)
        
        self.visualizeState()


    def abs( self, x ):
        if ( x > 0.0 ):
            return x
        else:
            return -x
    
    def rotation(self, yaw):
        '''
        create 2D rotation matrix from given angle
        '''
        s_yaw = math.sin(yaw)
        c_yaw = math.cos(yaw)
                
        return np.array([
            [c_yaw, -s_yaw], 
            [s_yaw,  c_yaw]
        ])
    
    def normalizeYaw(self, y):
        '''
        normalizes the given angle to the interval [-pi, +pi]
        '''
        while(y > math.pi):
            y -= 2 * math.pi
        while(y < -math.pi):
            y += 2 * math.pi
        return y
    
    def visualizeState(self):
        # visualize position state
        plot_trajectory("kalman", self.x[0:2])
        plot_covariance_2d("kalman", self.sigma[0:2,0:2])
    
    def predictState(self, dt, x, u_linear_velocity, u_yaw_velocity):
        '''
        predicts the next state using the current state and 
        the control inputs local linear velocity and yaw velocity
        '''
        x_p = np.zeros((3, 1))
        x_p[0:2] = x[0:2] + dt * np.dot(self.rotation(x[2]), u_linear_velocity)
        x_p[2]   = x[2]   + dt * u_yaw_velocity
        x_p[2]   = self.normalizeYaw(x_p[2])
        
        return x_p
    
    def calculatePredictStateJacobian(self, dt, x, u_linear_velocity, u_yaw_velocity):
        '''
        calculates the 3x3 Jacobian matrix for the predictState(...) function
        '''
        s_yaw = math.sin(x[2])
        c_yaw = math.cos(x[2])
        
        dRotation_dYaw = np.array([
            [-s_yaw, -c_yaw],
            [ c_yaw, -s_yaw]
        ])
        F = np.identity(3)
        F[0:2, 2] = dt * np.dot(dRotation_dYaw, u_linear_velocity)
        
        return F
    
    def predictCovariance(self, sigma, F, Q):
        '''
        predicts the next state covariance given the current covariance, 
        the Jacobian of the predictState(...) function F and the process noise Q
        '''
        return np.dot(F, np.dot(sigma, F.T)) + Q
    
    def calculateKalmanGain(self, sigma_p, H, R):
        '''
        calculates the Kalman gain
        '''
        return np.dot(np.dot(sigma_p, H.T), np.linalg.inv(np.dot(H, np.dot(sigma_p, H.T)) + R))
    
    def correctState(self, K, x_predicted, z, z_predicted):
        '''
        corrects the current state prediction using Kalman gain, the measurement and the predicted measurement
        
        :param K - Kalman gain
        :param x_predicted - predicted state 3x1 vector
        :param z - measurement 3x1 vector
        :param z_predicted - predicted measurement 3x1 vector
        :return corrected state as 3x1 vector
        '''
        
        # TODO: implement correction of predicted state x_predicted
        mu = x_predicted + np.dot( K, z - z_predicted )
            
        #return x_predicted
        return mu
    
    def correctCovariance(self, sigma_p, K, H):
        '''
        corrects the sate covariance matrix using Kalman gain and the Jacobian matrix of the predictMeasurement(...) function
        '''
        return np.dot(np.identity(3) - np.dot(K, H), sigma_p)
    
    def predictMeasurement(self, x, marker_position_world, marker_yaw_world):
        '''
        predicts a marker measurement given the current state and the marker position and orientation in world coordinates 
        '''
        z_predicted = Pose2D(self.rotation(x[2]), x[0:2]).inv() * Pose2D(self.rotation(marker_yaw_world), marker_position_world);
        
        return np.array([[z_predicted.translation[0], z_predicted.translation[1], z_predicted.yaw()]]).T
    
    def calculatePredictMeasurementJacobian(self, x, marker_position_world, marker_yaw_world):
        '''
        calculates the 3x3 Jacobian matrix of the predictMeasurement(...) function using the current state and 
        the marker position and orientation in world coordinates
        
        :param x - current state 3x1 vector
        :param marker_position_world - x and y position of the marker in world coordinates 2x1 vector
        :param marker_yaw_world - orientation of the marker in world coordinates
        :return - 3x3 Jacobian matrix of the predictMeasurement(...) function
        '''
        
        # TODO: implement computation of H
        x_m = marker_position_world
        c = math.cos(x[2])
        s = math.sin(x[2])
        H11 = -c
        H12 = -s
        H13 = c*( x_m[1]-x[1] ) - s*(x_m[0] - x[0])
        H21 = s
        H22 = -c
        H23 = -s*( x_m[1]-x[1] ) - c*( x_m[0] - x[0] )
        H31 = 0.0
        H32 = 0.0
        H33 = -1.0
        H = np.array([
            [ H11, H12, H13 ], 
            [ H21, H22, H23 ],
            [ H31, H32, H33 ]
        ])
        
        #return np.zeros((3,3))
        return H



class Pose2D:
    def __init__(self, rotation, translation):
        self.rotation = rotation
        self.translation = translation
        
    def inv(self):
        '''
        inversion of this Pose2D object
        
        :return - inverse of self
        '''
        inv_rotation = self.rotation.transpose()
        inv_translation = -np.dot(inv_rotation, self.translation)
        
        return Pose2D(inv_rotation, inv_translation)
    
    def yaw(self):
        from math import atan2
        return atan2(self.rotation[1,0], self.rotation[0,0])
        
    def __mul__(self, other):
        '''
        multiplication of two Pose2D objects, e.g.:
            a = Pose2D(...) # = self
            b = Pose2D(...) # = other
            c = a * b       # = return value
        
        :param other - Pose2D right hand side
        :return - product of self and other
        '''
        return Pose2D(np.dot(self.rotation, other.rotation), np.dot(self.rotation, other.translation) + self.translation)


