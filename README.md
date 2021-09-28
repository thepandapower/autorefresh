<h1>How to Use </h1>

0. Before running, please read through the rest of the readme, complete the required setup, and make sure you have it configured to your computer if you believe necessary. 
1. Open `autorefresh.py` in any text editor and change `skystone_limit` and `gold_limit` to the desired maximum skystones and gold you are willing to spend and save the file.
2. In a new terminal window please run `autorefresh.py` with python.
3. Open and maximize your Bluestacks window. Open the secret shop in E7 if it isn't open already. 
4. Press the `s` key on your keyboard to start the auto-refresh program. Wait until the program stops after it has finished spending all of your desired skystones and gold.
5. Make sure to keep Bluestacks window maximized and on your screen for the duration of this process.
6. Press and hold `q` on your keyboard when you want it to stop or it isn't doing what you want it to.
<h1>Notes </h1>

 - I threw together this tool in an hour or two so it might not be reliable.
 - I appologize to people who are not as experienced with programming because the instructions aren't very thorough but I have a midterm tomorrow :(
 - It is intended to just be used on full screen bluestacks.
 - If it is ever stops doing what you want it to do, hold q or go back to the terminal window and spam Ctrl+C
<br></br>

<h1>Required Setup</h1>

1. Have python installed
2. Please install all the required libraries in requirements.txt by running "pip install requirements.txt" in temrinal

<br></br>
<h1>Customizing to your computer</h1>
There is some fine-tuning required to properly use this program. 
You can try the base configuration, but if it doesn't work, please do the following

 - run `mouseLocation.py` which prints your screen resolution and then reads the position of your mouse
 - update the `width` and `height` of `screen_dim` inside of `autorefresh.py` with your screen resolution
 - update the `refresh_x` and `refresh_y` with the (x, y) location of the middle of the refresh shop button
 - update the `confirm_x` and `confirm_y` with the (x, y) location of the middle of the confirm button (the one you press after hitting refresh)
 - update `confirm_buy_y` with the y location of the middle of the confirm button you press after "Buy" button
 - update `item_x_off` and `item_y_off` with the x and y distance from the top left corner of the bookmark icon in shop from the middle of the "Buy" button
 - Depending on how different your screen resolution really is from mine, you might also have to re-screenshot an example of the BM or mystic icon in shop (when emulator is fullscreened) and replace the ones currently in this folder
 - Depending on the lag of your emulator, you might also want to add some additional `sleep()` statements throughout the program, do as you see fit