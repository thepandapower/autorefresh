import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui


buy_x = 1700
buy_y = [300, 515, 725, 625, 830, 1050]
confirm_x = 1100
confirm_y = 700
refresh_x = 300
refresh_y = 1050
confirm_buy_y = 800
bm_height = 135
bm_width = 135
item_x = 815
item1 = {
	'left': item_x,
    'top': 195,
    'width': bm_width,
    'height': bm_height
}

item2 = {
	'left': item_x,
    'top': 405,
    'width': bm_width,
    'height': bm_height
}

item3 = {
	'left': item_x,
    'top': 405,
    'width': bm_width,
    'height': bm_height
}

item4 = {
	'left': item_x,
    'top': 520,
    'width': bm_width,
    'height': bm_height
}

item5 = {
	'left': item_x,
    'top': 735,
    'width': bm_width,
    'height': bm_height
}

item6 = {
	'left': item_x,
    'top': 945,
    'width': bm_width,
    'height': bm_height
}

screen_dim = {
	'left': 0,
	'top': 0,
	'width':1920,
	'height':1200
}


item_dimensions = [item1, item2, item3, item4, item5, item6]

def swipe_up():
	pyautogui.moveTo(1200, 950)
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(1200, 250)
	pyautogui.mouseUp()

def find_match(items):
	for idx, item in enumerate(items):
		result = cv2.matchTemplate(item, bookmark, cv2.TM_CCOEFF_NORMED)
		print(result)
		if result > 0.5:
			return idx

def purchase_item(idx):
	pyautogui.click(buy_x, buy_y[idx])
	pyautogui.click(confirm_x, confirm_buy_y)

def refresh():
	pyautogui.click(refresh_x, refresh_y)
	pyautogui.click(confirm_x, confirm_y)

bookmark = cv2.imread('bookmark.png')
#mystic = cv2.imread('mystic.png')

print(pyautogui.size())
keyboard.wait('s')
print('press s to start and p to pause')
sct = mss.mss()
s1 = numpy.array(sct.grab(screen_dim))
screen = s1[:,:,:3]

res = cv2.matchTemplate(screen, bookmark, cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + bm_width, top_left[1] + bm_height)
print(max_val)
cv2.rectangle(s1, top_left, bottom_right, 255, 2)
cv2.imshow('asdf', s1)
cv2.waitKey(0)
# fps_time = time()
# #while True:
# items = [numpy.array(sct.grab(item_dim))[:,:,:3] for item_dim in item_dimensions]

# found_indices = find_match(items)
# print('found at ' + str(found_indices[0]))