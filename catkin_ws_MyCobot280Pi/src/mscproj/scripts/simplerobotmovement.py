from pymycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

mc = MyCobot(PI_PORT,PI_BAUD)

print(mc.is_power_on())
