# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input #adequate image into the format required by our mode
from tensorflow.keras.preprocessing.image import img_to_array #converting images into numpy arrays
from tensorflow.keras.models import load_model #loading our trained model
from imutils.video import VideoStream #input a frame of video
import numpy as np #numpy for array operations
import imutils #for basic image processing, easier with openCV
import time
import cv2
import os

def detect_and_predict_mask(frame, faceNet, maskNet):
	#get frame dimensions and construct blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
		(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()
	print(detections.shape)

	#initialise list of faces, thier locations, and predictions from face mask detector network
	faces = []
	locs = []
	preds = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence or probability associated with the detection
		confidence = detections[0, 0, i, 2]

		# filter out weak detections(confidence is greater than the minimum confidence)
		if confidence > 0.5:
			# compute the (x, y)-coordinates of the bounding box for the object
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI, convert it from BGR to RGB channel ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# add the face and bounding boxes to their respective lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# we make a prediction only if atleast one face was detected
	if len(faces) > 0:
		# for faster inference we'll make batch predictions on *all* faces at the same time rather than one-by-one prediction
		# in the above `for` loop
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	# return a 2-tuple of the face locations and their corresponding predictions
	return (locs, preds)

# load the serialized face detector model from folder
prototxtPath = r"face_detector\deploy.prototxt"
weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
maskNet = load_model("mask_detector.model")

# initialize the video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

#load our trained model
maskNet = load_model("mask_detector.model")
#now we have loaded model for mask detection as well as face detection

# initialize the video stream i.e start camera
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

#loop through frames i.e images from video stream
#frrames per second is more and heance we feel its a video 
while True:
    # get frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# detect faces in the frame and determine if they are wearing a face mask or not
	(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet) #method call

	# loop over the detected face locations and their corresponding locations
	for (box, pred) in zip(locs, preds):
		# unpack the bounding box and predictions
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		# determine the class label and color we'll use to draw the bounding box and text
		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255) #colour cod efor box around face

		# include the probability in the label
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
        #if  Mask percentage is above 90% while mask is on, considerable accuracy

		# draw rectangular box around face and show label
		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
    
#cleanup 
cv2.destroyAllWindows()
vs.stop()