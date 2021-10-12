# -*- coding: utf-8 -*- 
#needed imports
import time
import sys
import cv2
import numpy as np
import pygetwindow as pw
import pyautogui
import pydirectinput as pi
import pytesseract
from PIL import Image



imagePath = 'C:/Users/aryam/Desktop/Development/tfttokengrinder/curscreen.png'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
def forfeit():
	pi.press("enter")
	time.sleep(.5)
	pi.press("/")
	time.sleep(.5)
	pi.press("f")
	time.sleep(.5)
	pi.press("f")
	time.sleep(.5)
	pi.press("enter")
	time.sleep(.5)
	pi.moveTo(831, 483)
	time.sleep(.5)
	pi.click()
	time.sleep(.5)
	pi.mouseDown()
	time.sleep(.5)
	pi.mouseUp()
	time.sleep(5)
def playAgain():
	time.sleep(5)
	pi.moveTo(829, 909)
	time.sleep(.5)
	pi.click()
	time.sleep(5)
	pi.click()
def acceptGame():
	time.sleep(.5)
	pi.moveTo(964, 756)
	time.sleep(.5)
	pi.click()
def selectGame():
	pi.moveTo(831, 483)
	time.sleep(.5)
	pi.click()
	time.sleep(.5)
	pi.mouseDown()
	time.sleep(.5)
	pi.mouseUp()
	time.sleep(5)
def checkForAccept():
	img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
	img = img[750:780, 900:1020]
	(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	img = cv2.bitwise_not(img)
	cv2.imwrite("acceptRegion.png", img)
	acceptAreaWords = pytesseract.image_to_string(Image.open("acceptRegion.png"))
	try:
		acceptAreaWords = acceptAreaWords.split()[0]
		print(acceptAreaWords)
	except:
		print("no accept area words")
		None
	if("ACCEPT" in acceptAreaWords):
		acceptGame()
def getRoundStartWait():
	img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
	img = img[0:38, 810:870]
	(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	img = cv2.bitwise_not(img)
	cv2.imwrite("temp.png", img)
	round = pytesseract.image_to_string(Image.open("temp.png"))
	try:
		round = round.split()[0]
	except:
		None
	print("round: ", round)
	if(round.rstrip() == "1-3"):
		time.sleep(700)
		selectGame()
		forfeit()
		playAgain()
def getGameState():
	titles = pw.getAllTitles()
	if('League of Legends (TM) Client' in titles):
		#window = pw.getWindowsWithTitle('League of Legends (TM) Client')[0]
		#x1, x2, y1, y2 = window.left, window.right, window.top, window.bottom
		pyautogui.screenshot(imagePath)
		im = Image.open(imagePath)
		#im = im.crop((x1, y1, x2, y2))
		im.save(imagePath)

		getRoundStartWait()
	elif('League of Legends' in titles):
		#window = pw.getWindowsWithTitle('League of Legends')[0]
		#x1, x2, y1, y2 = window.left, window.right, window.top, window.bottom
		pyautogui.screenshot(imagePath)
		#im = Image.open(imagePath)
		#im = im.crop((x1, y1, x2, y2))
		#im.save(imagePath)

		checkForAccept()

	else:
		print("League of Legends is NOT open")
time.sleep(3)
while(True):
	getGameState()
	time.sleep(1)