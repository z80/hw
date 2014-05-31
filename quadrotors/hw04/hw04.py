
class UserCode:
    def __init__(self):
        # TODO: tune gains
        self.Kp = 1
        self.Kd = 0
        self.xPrev = None
        
            
    def compute_control_command(self, t, dt, x_measured, x_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to compute_control_command
        :param x_measured: measured position (scalar)
        :param x_desired: desired position (scalar)
        :return - control command u
        '''
        # TODO: implement PD controller
        Kx = -5
        Kd = -500
        u = 0.0
        u += Kx*( x_measured - x_desired )
        if ( self.xPrev ):
            v = x_measured - self.xPrev
            u += Kd * v
        self.xPrev = x_measured
                
        return u



