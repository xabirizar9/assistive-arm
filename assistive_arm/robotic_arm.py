import numpy as np

from assistive_arm.motor_control import CubemarsMotor

class AssistiveArm:
    def __init__(self):
        self.motors = [
            CubemarsMotor(motor_type="AK70-10", csv_file="motor_data.csv"),
            CubemarsMotor(motor_type="AK60-6", csv_file="motor_data.csv"),
        ]


def calculate_ee_pos(theta_1: CubemarsMotor, theta_2: CubemarsMotor):
    L1 = 0.44
    L2 = 0.41

    P_EE = np.array([
        L1*np.cos(theta_1) + L2*np.cos(theta_1 + theta_2),
        L1*np.sin(theta_1) + L2*np.sin(theta_1 + theta_2),
        theta_1 + theta_2])

    return P_EE

def get_jacobian(theta_1: float, theta_2: float):
    l1 = 0.44
    l2 = 0.41

    jacobian = np.array([
        [-l1*np.sin(theta_1)-l2*np.sin(theta_1+theta_2),
         -l2*np.sin(theta_1+theta_2)],
        [l1*np.cos(theta_1)+l2*np.cos(theta_1+theta_2),
        l2*np.cos(theta_1+theta_2)]])
    
    return jacobian