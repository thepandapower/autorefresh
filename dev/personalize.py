import keyboard
import pyautogui


def saveLocation(f):
	keyboard.wait('x')
	loc = pyautogui.position()
	f.write(str(loc.x) + ', ' + str(loc.y) + '\n')
	return loc

#make file for locations
locationFile = open('myLocations.txt', 'w')

print('Please open Bluestacks, e7, and enter the secret shop\n')


#find refresh button
print('Please move your mouse to the center of the Refresh button and press `x`\n')
refresh_loc = saveLocation(locationFile)


#find refresh confirm button
print('Please click the Refresh button and move your mouse to the center of the Confirm button and press `x`, then press Cancel\n')
refConfirm_loc = saveLocation(locationFile)


#find item TL corner
print('Refresh the shop until you find either friendship bm, bookmark, or mystics')
print('Do NOT scroll anymore in the shop')
print('WARNING: DO THIS NEXT INSTRUCTION CAREFULLY')
print('Please move your mouse to the top left corner of the square item icon INCLUDING THE GREY BORDER')
print('then press `x`\n')
item_TL_loc = saveLocation(locationFile)


#find item BR corner?? (or TR corner)
print('WARNING: DO THIS NEXT INSTRUCTION CAREFULLY')
print('Please move your mouse to the bottom right corner of the square item icon INCLUDING THE GREY BORDER')
print('then press `x`\n')
item_BR_loc = saveLocation(locationFile)

#calculate BM ideal size based on these points
personal_dim_1 = item_BR_loc.x - item_TL_loc.x
personal_dim_2 = item_BR_loc.y - item_TL_loc.y
avg_dim = int((((personal_dim_1 + personal_dim_2)/2) // 5) * 5)
locationFile.write(str(avg_dim) + '\n')

#find purchase button
print('Please move your mouse to the center of the Buy button corresponding to square item icon and press `x`\n')
buy_loc = saveLocation(locationFile)

#calculate X and Y offset from the item's TL corner to the purchase button
buy_offset_x = buy_loc.x - item_TL_loc.x
buy_offset_y = buy_loc.y - item_TL_loc.y
locationFile.write(str(buy_offset_x) + ', ' + str(buy_offset_y) + '\n')


#find purchase confirm button
print('Press the Buy button and move your mouse over to the center of the confirm Buy button and press `x`\n')
buyConfirm_loc = saveLocation(locationFile)


#Create a file to store personalized locations
locationFile.close()