import cv2
from PIL import ImageGrab
import numpy as np
from matplotlib import pyplot as pyplot
import imutils

MIN_THRESH = 1
EggColors = {
'hat':([111, 0, 0], [255, 255, 255]),
'brown':([0, 74, 14], [32, 199, 220])
}

class EggFinder:
	#image = cv2.imread(image)
	def __init__(self):
		#self.hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		self.EggsMasks =[]

	def findEggs(self, image):
		self.hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		# Reset our egg array
		self.EggMasks = []
		for EggF in EggColors.values():
			self.EggMasks.append(self.findEgg(self.hsvImage, EggF[0], EggF[1]))
		return self.EggMasks

	def findEgg(self, image, lower, upper):
		""" Returns tuple, x position of center, y position of center """
		lower = np.array(lower)
		upper = np.array(upper)
		shapeMask = cv2.inRange(image, lower, upper)

		# find the contours in the mask
		cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		# loop over the contours
		# compute the center of the contour
		for c in cnts:
			if cv2.contourArea(c) > MIN_THRESH:
				M = cv2.moments(c)
				cX = int(M["m10"] / M["m00"])
				cY = int(M["m01"] / M["m00"])
				self.drawMasks(c, cX, cY)
				return (cX, cY,)
			else:
				pass

	def drawMasks(self, c, cX, cY):
		# draw the contour and center of the shape on the image
		cv2.drawContours(self.hsvImage, [c], -1, (0, 255, 0), 2)
		cv2.circle(self.hsvImage, (cX, cY), 7, (255, 255, 255), -1)
		cv2.putText(self.hsvImage, "enemy target", (cX - 20, cY - 20),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
		cv2.waitKey(10)
