import keyboard
import mss
import cv2
import numpy as np
from time import time, sleep
import pyautogui


item_x_off = 850
item_y_off = 100
confirm_x = 1100
confirm_y = 700
refresh_x = 300
refresh_y = 1050
confirm_buy_y = 800
bm_height = 135
bm_width = 135

screen_dim = {
	'left': 0,
	'top': 0,
	'width':1920,
	'height':1200
}

sct = mss.mss()
bookmark = cv2.imread('bookmark.png')
mystic = cv2.imread('mystic.png')

threshold = 0.975
skystone_limit = 636
gold_limit = 3*10**6
refresh_count = 0
bm_count = 0
mystic_count = 0

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

