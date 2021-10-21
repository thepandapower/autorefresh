import keyboard
import mss
import cv2
import numpy as np
from time import time, sleep
import pyautogui

locationFile = open('myLocations.txt', 'r')

def getLocationPair():
	inLine = locationFile.readline()
	inLine = inLine[:-1]
	locs = inLine.split(',')
	loc1 = int(locs[0].strip())
	loc2 = int(locs[1].strip())
	return loc1, loc2

refresh_x, refresh_y = getLocationPair()
confirm_x, confirm_y = getLocationPair()
TL_x, TL_y = getLocationPair()
BR_x, BR_y = getLocationPair()
bm_dim = int(locationFile.readline()[:-1])
bm_height = bm_dim
bm_width = bm_dim
dummy_buy_x, dummy_buy_y = getLocationPair()
item_x_off, item_y_off = getLocationPair()
confirm_buy_x, confirm_buy_y = getLocationPair()

locationFile.close()

screenRes = pyautogui.size()

screen_dim = {
	'left': 0,
	'top': 0,
	'width':screenRes.width,
	'height':screenRes.height
}


test_bm = cv2.imread('test_bm.png')
ideal_bm = cv2.resize(test_bm, (int(bm_dim), int(bm_dim)), interpolation = cv2.INTER_AREA)

sct = mss.mss()
bookmark = ideal_bm
threshold = 0.975

keyboard.wait('s')
found = False
src_image = np.array(sct.grab(screen_dim))
screen = src_image[:,:,:3]
bookmark_res = cv2.matchTemplate(screen, bookmark, cv2.TM_CCORR_NORMED)
# mystic_res = cv2.matchTemplate(screen, mystic, cv2.TM_CCORR_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(bookmark_res)

print(max_val)
if(max_val > threshold):
	found = True
	# bm_count += 1
	print('BOOKMARK FOUND AT: ' + str(max_loc))
	pyautogui.moveTo(max_loc[0] + item_x_off, max_loc[1] + item_y_off)