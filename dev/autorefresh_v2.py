import keyboard
import mss
import cv2
import numpy as np
from time import time, sleep
import pyautogui


## PREFERENCES ##

threshold = 0.975
skystone_limit = 1900
gold_limit = 7*10**6
refresh_count = 0
bm_count = 0
mystic_count = 0


## FUNCTIONALITY ##

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

test_mystic = cv2.imread('test_mystic.png')
ideal_mystic = cv2.resize(test_mystic, (int(bm_dim), int(bm_dim)), interpolation = cv2.INTER_AREA)

sct = mss.mss()
bookmark = ideal_bm
mystic = ideal_mystic

def click(x, y):
	pyautogui.moveTo(x, y)
	sleep(.75)
	pyautogui.click()
	sleep(0.1)
	pyautogui.click()
	sleep(.5)

def find_item():
	global bm_count, mystic_count
	found = False
	src_image = np.array(sct.grab(screen_dim))
	screen = src_image[:,:,:3]
	bookmark_res = cv2.matchTemplate(screen, bookmark, cv2.TM_CCORR_NORMED)
	mystic_res = cv2.matchTemplate(screen, mystic, cv2.TM_CCORR_NORMED)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(bookmark_res)
	if(max_val > threshold):
		found = True
		bm_count += 1
		purchase_item(max_loc)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(mystic_res)
	if(max_val > threshold):
		found = True
		mystic_count += 1
		purchase_item(max_loc)
	return found

def swipe_up():
	pyautogui.moveTo(1200, 950)
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(1200, 250)
	pyautogui.mouseUp()

def purchase_item(loc):
	click(loc[0] + item_x_off, loc[1] + item_y_off)
	print('purchased')
	#sleep(1)
	click(confirm_x, confirm_buy_y)
	#sleep(.5)

def refresh():
	global refresh_count
	click(refresh_x, refresh_y)
	click(confirm_x, confirm_y)
	refresh_count += 1

print('press s to start and hold q to quit')
keyboard.wait('s')
while (refresh_count + 1)*3 <= skystone_limit and (bm_count + mystic_count + 1) * 300000 <= gold_limit:
	# keyboard.wait('s')
	foundItem = find_item()
	#sleep(.5)
	swipe_up()
	sleep(1)
	foundItem = find_item()
	#sleep(.5)
	refresh()
	sleep(1)
	if keyboard.is_pressed('q'):
		break

print('bought ' + str(bm_count) + ' bookmarks and ' + str(mystic_count) + ' mystics in ' + str(refresh_count*3) + ' skystones')

