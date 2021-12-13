import picamera

	#setup the camera such that it closses
	#when we are done with it
print ("About to take a picture")
with picamera.PiCamera() as camera:
	camera.start_preview()
	camera.resolution = (1280, 720)
	camera.capture("/home/pi/Desktop/GROUP2/GROUP-2/RAAEL.jpg")
	camera.stop_preview()
	print("Picture taken.")
