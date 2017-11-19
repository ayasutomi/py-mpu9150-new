from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

while True:
    print (sensor.get_accel_data())
    print (sensor.get_gyro_data())
    time.sleep(1)
