import numpy as np

class State:
    def __init__(self):
        self.position = np.zeros((3,1))
        self.velocity = np.zeros((3,1))

class UserCode:
    def __init__(self):
        # TODO: tune gains
    
        # xy control gains
        Kp_xy = -1 # xy proportional
        Kd_xy = -0.5 # xy differential
        
        # height control gains
        Kp_z  = -1 # z proportional
        Kd_z  = -0.5 # z differential
        
        self.Kp = np.array([[Kp_xy, Kp_xy, Kp_z]]).T
        self.Kd = np.array([[Kd_xy, Kd_xy, Kd_z]]).T

        self.xPrev = None
        self.yPrev = None
        self.zPrev = None
    
    def compute_control_command(self, t, dt, state, state_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param state: State - current quadrotor position and velocity computed from noisy measurements
        :param state_desired: State - desired quadrotor position and velocity
        :return - xyz velocity control signal represented as 3x1 numpy array
        '''
        ux = 0.0
        uy = 0.0
        uz = 0.0
        ux += self.Kp[0] * ( state.position[0] - state_desired.position[0] )
        uy += self.Kp[1] * ( state.position[1] - state_desired.position[1] )
        uz += self.Kp[2] * ( state.position[2] - state_desired.position[2] )
        #if ( self.xPrev != None ):
        #v = state.position[0] - self.xPrev
        ux += self.Kd[0] * (state.velocity[0] - state_desired.velocity[0] )
        uy += self.Kd[1] * (state.velocity[1] - state_desired.velocity[1] )
        uy += self.Kd[2] * (state.velocity[2] - state_desired.velocity[2] )

        
        # plot current state and desired setpoint
        self.plot(state.position, state_desired.position)
        
        # TODO: implement PID controller computing u from state and state_desired
        u = np.zeros((3,1))
        #u = np.array( [ux, uy, uz] ).T
        u[0] = ux
        u[1] = uy
        u[2] = uz
        #print state.position - state_desired.position
        
        return u
        
    def plot(self, position, position_desired):
        from plot import plot
        plot("x", position[0])
        plot("x_des", position_desired[0])
        plot("y", position[1])
        plot("y_des", position_desired[1])
        plot("z", position[2])
        plot("z_des", position_desired[2])
        
