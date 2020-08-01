import cv2
import time
from gaze_tracking import GazeTracking


def register():
	# This function registers a new pattern
	print("Registration Initiated.")
	pattern = "" # Initiating the pattern as empty
	
	# Gaze tracking initiated
	gaze = GazeTracking()
	webcam = cv2.VideoCapture(0)
	
	# File to write the pattern
	f=open("auth_details.txt","a")
	
	# captures the pattern until the user blinks
	while True:
		# We get a new frame from the webcam
		_, frame = webcam.read()

		# We send this frame to GazeTracking to analyze it
		gaze.refresh(frame)

		frame = gaze.annotated_frame()
		text = ""

		if gaze.is_blinking():
			time.sleep(4)
			text = "Blinking"
			break
		elif gaze.is_right():
			time.sleep(.5)
			text = "Looking right"
			pattern += "1"

		elif gaze.is_left():
			time.sleep(.5)
			text = "Looking left"
			pattern += "0"
		elif gaze.is_center():
			#time.sleep(.5)
			text = "Looking center"
	   

		cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

		left_pupil = gaze.pupil_left_coords()
		right_pupil = gaze.pupil_right_coords()
		cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
		cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

		cv2.imshow("Demo", frame)
		#print("record")
		if cv2.waitKey(1) == 27:
			break
	# Writing the pattern to the file
	print(pattern)
	f.write(pattern+"\n")
	#f.write("\n")
	print("Destroying all windows")
	cv2.destroyAllWindows()
	f.close()

	print("Registration ended.")

def login():
	# This function reads a new pattern and verifies it with existing ones in auth_details.txt
	
	print("Login  Initiated.")
	
	pattern = "" # Initiating the pattern as empty
	
	# Gaze tracking initiated
	gaze = GazeTracking()
	webcam = cv2.VideoCapture(0)
	
	# File to read the pattern from
	f=open("auth_details.txt","r")
	
	# captures the pattern until the user blinks
	while True:
		# We get a new frame from the webcam
		_, frame = webcam.read()

		# We send this frame to GazeTracking to analyze it
		gaze.refresh(frame)

		frame = gaze.annotated_frame()
		text = ""

		if gaze.is_blinking():
			time.sleep(4)
			text = "Blinking"
			break
		elif gaze.is_right():
			time.sleep(.5)
			text = "Looking right"
			pattern += "1"

		elif gaze.is_left():
			time.sleep(.5)
			text = "Looking left"
			pattern += "0"
		elif gaze.is_center():
			#time.sleep(.5)
			text = "Looking center"
	   

		cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

		left_pupil = gaze.pupil_left_coords()
		right_pupil = gaze.pupil_right_coords()
		cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
		cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

		cv2.imshow("Demo", frame)
		#print("record")
		if cv2.waitKey(1) == 27:
			break
	
	# Checking it with recorded ones
	# Reads each line from the file
	#print(pattern)
	isLoggedin = False
	for line in f:
		# Checks for a pattern match	
		if line == pattern:
			print("if loop")
			isLoggedin = True
			break
	if isLoggedin:
		print("Authenticated.")
	else:
		print("Not Authenticated.")
	print(pattern)
	print("Destroying all windows")
	cv2.destroyAllWindows()
	f.close()
	print("Login  Ended.")
