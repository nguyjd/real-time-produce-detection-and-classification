import cv2
import time
import numpy as np

# Threshold for the model.
CONFTHRESHOLD = 0.5
NMSTHRESHOLD = 0.5

# font and color of the text and the box 
COLOR = (0, 255, 0)
FONT = cv2.FONT_HERSHEY_PLAIN


yolov4 = cv2.dnn.readNet('Trained_model.weights', 'yolov4.cfg')
yolov4.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
yolov4.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

yolov4 = cv2.dnn_DetectionModel(yolov4)
yolov4.setInputParams(size=(128, 128), scale=1/255, swapRB=True)

cam = cv2.VideoCapture(0)

labels = ['banana', 'apple', 'eggplant']
produceCount = [0, 0, 0]

while True:

    
    # Time the start of the inference
    start = time.time()
    # img = cv2.imread('TestImages/2banana.jpg')
    # Get a frame from the webcam
    ret, frame = cam.read()

    if ret:

        # Pass the webcam frame through the model.
        labelsIndex, scores, bounds = yolov4.detect(frame, CONFTHRESHOLD, NMSTHRESHOLD)

        for index, bound in enumerate(bounds):
            label = f"{labels[labelsIndex[index]]}: {scores[index]:.2f}"
            cv2.rectangle(frame, bound, COLOR, 1)
            cv2.putText(frame, label, (bound[0], bound[1]-10), FONT, 1, COLOR, 1)

            produceCount[0] = 0
            produceCount[1] = 0
            produceCount[2] = 0

            if labels[labelsIndex[index]] == 'banana':
                produceCount[0] += 1
            elif labels[labelsIndex[index]] == 'apple':
                produceCount[1] += 1
            elif labels[labelsIndex[index]] == 'eggplant':
                produceCount[2] += 1
                    
        print(f"Banana Count: {produceCount[0]}")
        print(f"Apple Count: {produceCount[1]}")
        print(f"Eggplant Count: {produceCount[2]}")

        # Check for a escape press to quit the program
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break

        # Time the end of the inference
        end = time.time()

        # Find the speed of the program.
        fps = 1 / (end-start)
        fps_text = f"FPS: {fps:.2f}"

        cv2.putText(frame, fps_text, (0, 15), FONT, 1, COLOR)

        cv2.imshow('Produce Dectection', frame)



    