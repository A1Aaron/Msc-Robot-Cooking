from pymycobot import MyCobot
from pymycobot.genre import Angle
import numpy as np
mc = MyCobot("/dev/ttyAMA0",1000000)
# mc.release_all_servos()
# mc.set_gripper_state(0,50) 
# mc.send_angles([-60.99, -23.2, -5.09, -50.27, -80.15, -6.67],20)
a = np.array([mc.get_coords()[:3]])
print(mc.get_angles())
