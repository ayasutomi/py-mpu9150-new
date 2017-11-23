from mpu9150 import mpu9150
import time
from threading import Thread

def printData():
    sensor.get_all_data()
    print('a:%.3f,%.3f,%.3f g:%.3f,%.3f,%.3f m:%.1f,%.1f,%.1f temp:%.1f '%(
        sensor.accel['x'],sensor.accel['y'],sensor.accel['z'],
        sensor.gyro['x'],sensor.gyro['y'],sensor.gyro['z'],
        sensor.magn['x'],sensor.magn['y'],sensor.magn['z'],
        sensor.temp))
    
if __name__ == "__main__":
    sensor = mpu9150(0x68)
    print(sensor.read_accel_range())
    print(sensor.read_gyro_range())
    while True:
        t = Thread(target=printData, args = ())
        t.start()
        time.sleep(.1)