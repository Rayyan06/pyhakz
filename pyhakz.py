import pyautogui
import time
import os
import numpy as np

q_table = np.zeros([])

URL = 'https://shellshock.io/'
STARTING_DELAY = 2
LOADING_TIME = 20


PLAY_BUTTON = (515, 500)
PLAY_GAME = (1000, 500)

time.sleep(STARTING_DELAY)
class Controller:

	def __init__(self):
		self.target = (100, 100)
		self.open()

	def open(self):
		# Launch Chrome
		pyautogui.hotkey('win', 'r')
		pyautogui.typewrite('chrome')
		pyautogui.hotkey('enter')
		pyautogui.click (1700, 722)
		pyautogui.typewrite(URL)
		pyautogui.hotkey('enter')
		time.sleep(LOADING_TIME)
		self.click(PLAY_BUTTON)
		time.sleep(LOADING_TIME)
		self.click(PLAY_GAME)

	def getCoordinate(self):
		while True:
			print(pyautogui.position())
	#def reload
	def click(self, xy):
		pyautogui.click(xy[0], xy[1])
	def shoot(self):
		pyautogui.click(self.target[0], self.target[1])

	def reload(self):
		pyautogui.hotkey('r')

	def move(self, direction, duration=1):
		pyautogui.keyDown(direction)
		time.sleep(duration)

	def jump(self):
		self.move('space', duration=1)
		#pyautogui.keyUp(direction)

	def findTarget(self):
		#pyautogui.
		pass

	def dodge(self):
		self.jump()
		self.move('s')

def main():
	controller = Controller()
	controller.move(direction='w', duration=2)
	controller.dodge()

if __name__ =="__main__":
	main()


