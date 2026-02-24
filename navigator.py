# File use to navigate the qdrone2 using x,y,z and yaw commands
# To simplify usage, the area where new code should be implemented is marked. 

# region: Python level imports
import numpy as np
import cv2
import math
try:
    from quanser.common import Timeout
except:
    from quanser.communications import Timeout
from pal.utilities.stream import BasicStream
from pal.utilities.timing import Timer
from pal.utilities.math import SignalGenerator
from pal.utilities.vision import Camera2D, Camera3D
# endregion 

# region: Experiment constants
simulationTime = 10000 # will run for this amount of seconds
frequency = 200 # Hz
frameRate = 30
CameraCounts = int(round(frequency / frameRate))
# endregion 

counter = 0 # counter to track scopes
receiveCounter = 0 # counter to track receiving data from client
receivedData = np.zeros(16)
cmd_x = 0 # value in meters
cmd_y = 0 # value in meters
cmd_z = 1 # value in meters
cmd_yaw = 0 # value in radians

# region: Initializing all cameras and streams 

realsense = Camera3D(deviceId="0@tcpip://localhost:18986", 
                     mode='RGB&DEPTH',
                     frameWidthRGB=640, 
                     frameHeightRGB=480, 
                     frameRateRGB=frameRate, 
                     frameWidthDepth=640, 
                     frameHeightDepth=480, 
                     frameRateDepth=frameRate)

camRight = Camera2D(cameraId="0@tcpip://localhost:18982", 
                   frameWidth=640, frameHeight=480, 
                   frameRate=frameRate)

camBack = Camera2D(cameraId="1@tcpip://localhost:18983", 
                   frameWidth=640, frameHeight=480, 
                   frameRate=frameRate)

camLeft = Camera2D(cameraId="2@tcpip://localhost:18984", 
                    frameWidth=640, frameHeight=480, 
                    frameRate=frameRate)

camDown = Camera2D(cameraId="3@tcpip://localhost:18985", 
                   frameWidth=640, frameHeight=480, 
                   frameRate=frameRate)


dataStream = BasicStream('tcpip://localhost:18373', 
                       agent='C', sendBufferSize=1460, 
                       receiveBuffer=np.zeros((1,16), dtype=np.float64),
                       recvBufferSize=1460, nonBlocking=False)

timeout=Timeout(seconds=0, nanoseconds=1)
prev_con = False

#endregion

# region: generators for drive commands
# this section can be modified or removed once other logic is added
wave1 = SignalGenerator().sine(amplitude=0.5, angularFrequency=0.05)
wave2 = SignalGenerator().cosine(amplitude=0.5, angularFrequency=0.05)
wave3 = SignalGenerator().sine(amplitude=0.2, angularFrequency=0.1)

cmd_x = next(wave1) 
cmd_y = next(wave2) 
cmd_z = next(wave3) 
# endregion

# Initialize timer
timer = Timer(frequency, simulationTime)

try:
    while timer.check():

        # First check if the server was connected.
        if not dataStream.connected:
            dataStream.checkConnection(timeout=timeout)

        # If a server accepted the connection, let the user know and proceed.
        if dataStream.connected and not prev_con:
            print('Connection to Server was successful.')
            prev_con = dataStream.connected
            continue
        
        # Server is connected, so execute code within this section.
        if dataStream.connected:
            # get current timestamp
            currentTime = timer.get_current_time()

            # Receive data from client
            recvFlag, bytesReceived = dataStream.receive(
                iterations=2, timeout=timeout)
            # print('Total bytes received:', bytesReceived)
            if not recvFlag:
                receiveCounter += 1
                if receiveCounter > 10:
                    print('Client stopped sending data over.')
                    break
            else:
                receiveCounter = 0
                receivedData = dataStream.receiveBuffer[0] # 16 received values. 
                # receivedData looks like:
                # [0] is if the stream is connected
                # [1,2,3] IMU - Gyro (rad/s)
                # [4,5,6] IMU - Accel (m/s/s)
                # [7,8,9] Estimates - Angular Position (rad)
                # [10,11,12] Estimates - Angular Rates (rad/s)
                # [13,14,15] Estimates - Angular Acceleration (m/s/s)
            
            # read cameras when available
            if counter%CameraCounts == 0:
                frames = False
                frameLeft = camLeft.read()
                frameRight = camRight.read()
                frameBack = camBack.read()
                frameDown = camDown.read()

                realsense.read_RGB()
                realsense.read_depth() 

                # NOTE: depth data imageDepth, gives 0-255 values mapped to 0-9.44 meters

                if frameLeft or frameRight or frameBack or frameDown:

                    imageLeft = camLeft.imageData
                    imageRight = camRight.imageData
                    imageBack = camBack.imageData
                    imageDown = camDown.imageData
                    imageRGB = realsense.imageBufferRGB
                    imageDepth = realsense.imageBufferDepthPX 

                    cv2.imshow("Left Drone Image", imageLeft)
                    cv2.imshow("Right Drone Image", imageRight)
                    cv2.imshow("Back Drone Image", imageBack)
                    cv2.imshow("Downwards Drone Image", imageDown)
                    cv2.imshow("Front RGB Drone Image", imageRGB)
                    cv2.imshow("Front Depth Drone Image", imageDepth)

                    cv2.waitKey(1)
                
            counter += 1
            # ---------------------------------------------------------------
            # ---NOTE: Changes to the logic should be made in this section---
            # ---------------------------------------------------------------
            # the rest of the code sets up timing, camera streams and data streams


            cmd_x = wave1.send(currentTime)
            cmd_y = wave2.send(currentTime)
            cmd_z = wave3.send(currentTime) + 1 # NOTE THE +1 TO KEEP THE DRONE IN THE AIR
            cmd_yaw = math.pi/6
            sendCommands = np.array([cmd_x, cmd_y, cmd_z, cmd_yaw])

            

            # ---------------------------------------------------------------
            # ---------------------------------------------------------------
            # ---------------------------------------------------------------

            # send data to drone 
            sentFlag = dataStream.send( sendCommands )
            # print('Did bytes send:', sentFlag)
            # print('Total bytes sent:', len(sendCommands.tobytes()))
            if sentFlag == -1:
                print('Server application not receiving.')
                break

            timer.sleep()

except KeyboardInterrupt:
    print("\nExiting due to keyboard interrupt.")

realsense.terminate()
camLeft.terminate()
camBack.terminate()
camRight.terminate()
camDown.terminate()
dataStream.terminate()

#endregion