import time
import pyautogui
import keyboard
import mouse

start_button = "p"

def record(num_tiles, coords):
    tiles = []
    while len(tiles) < num_tiles:
        coord_num = 0
        for x, y in coords:
            pixel = pyautogui.pixel(x, y)
            
            # if pixel is white (lit up)
            if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                
                # if this is a different tile than before
                # (same tile doesn't get clicked twice consecutively)
                if len(tiles) == 0 or tiles[-1] != coord_num:
                    tiles.append(coord_num)
            coord_num += 1
    return tiles

def repeat(sequence, coords):
    # click on every tile in sequence in order
    for index in sequence:
        mouse.move(coords[index][0], coords[index][1], absolute = True)
        mouse.click()
        time.sleep(0.1)


# start the program
keyboard.wait(start_button)
time.sleep(0.2)

# find 3x3 grid
grid_loc = pyautogui.locateOnScreen('grid.png', confidence = 0.7)
xs = [int(grid_loc.left + grid_loc.width // 6 + i * grid_loc.width // 3) for i in range(3)]
ys = [int(grid_loc.top + grid_loc.height // 6 + i * grid_loc.height // 3) for i in range(3)]

# contain 9 coordinates at indexes 0-8
coords = []
for y in ys:
    for x in xs:
        coords.append((x, y))
        
        
# run the program
num_tiles = 1
while True:
    # kill program
    if keyboard.is_pressed(start_button):
        break
    
    # get the sequence that the game gives us
    sequence = record(num_tiles, coords)
    time.sleep(1)
    
    # play sequence back
    repeat(sequence, coords)
    num_tiles += 1
        