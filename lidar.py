from rplidar import RPLidar, RPLidarException
import smbus

bus = smbus.SMBus(1)
address = 8

def send_data_to_arduino(data):
    bus.write_byte(address,data)
    print("raspberry pi sent: ", data)

lidar = RPLidar('/dev/ttyUSB0')

lidar.__init__('/dev/ttyUSB0', 115200, 3, None)

lidar.connect()

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

try:
    
    for i, scan in enumerate(lidar.iter_scans()):
        
        one_sent = False
        last_angle = None
        
        for d in scan:
            
            if 350 <= d[1] <= 360 or 0 <= d[1] <= 10:
                
                if (d[2] / 10) <= 100:
                    one_sent = True
                    print(1)
                    send_data_to_arduino(1)
                    break
                
                else:
                    one_sent = False
                    
            if last_angle is not None and abs((last_angle - d[1]) % 360) > 355:
                one_sent = False
            
            last_angle = d[1]
            
        if not one_sent:
            print(0)
            send_data_to_arduino(0)
            one_sent = False
    
        if False:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            break
        
except KeyboardInterrupt as err:
    print('key board interupt')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

except RPLidarException as err:
    print(err)
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    
except AttributeError:
    print('hi attribute error')
