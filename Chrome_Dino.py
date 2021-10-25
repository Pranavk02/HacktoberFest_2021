import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):    
    
    for i in range(140, 160): # Light And Dark Mode
        for j in range(250, 270):
            if data[i, j] == 33:
                check = True
            else:
                check = False
      
    for i in range(300, 500): # Birds (X1,X2) (Width) Left To Right
        for j in range(410, 560):  # Birds (Y1,Y2) (Height) Top To Bottom
            try:
                if check:    
                    var = data[i, j] > 100
                else:
                    var = data[i, j] < 100
            except:
                var = data[i, j] < 100
            if var:
                hit("down")
                time.sleep(0.35)
                pyautogui.keyUp('down') 
                return
    for i in range(300, 500): # Cactus (X1,X2) (Width) Left To Right
        for j in range(560, 650):  # Cactus (Y1,Y2) (Height) Top To Bottom
            try:
                if check:    
                    var = data[i, j] > 100
                else:
                    var = data[i, j] < 100
            except:
                var = data[i, j] < 100    
            if var:
                hit("up")
                pyautogui.keyUp('up')
                return            
                
if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # for i in range(300, 500): # BIrds (X1,X2) (Width) Left To Right
        #     for j in range(410, 563):  # BIrds (Y1,Y2) (Height) Top To Bottom
        #         data[i, j] = 0
        
        # for i in range(300, 500): # Cactus (X1,X2) (Width) Left To Right
        #     for j in range(563, 650):  # Cactus (Y1,Y2) (Height) Top To Bottom
        #         data[i, j] = 171

        # image.show()
        # break

        
