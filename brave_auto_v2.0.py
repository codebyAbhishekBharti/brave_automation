"""
The automation program will help me to automate brave to earn bat
1. Open brave
2. Open first profile
3. click new tab
3. scroll down
4. click on the first news
5. Go to new tab
6. scroll down till add
7. refresh page
8. do refresh and scroll 6 times
9. switch to new account and do all again
"""

import pyautogui
import time
import os
import cv2
import threading
import keyboard
from PIL import Image
import numpy as np

class Automate_brave:
    def __init__(self,total_profiles,total_adds=6,starting_profile=1):
        global thread_work_completed  # Use the global keyword to modify the global variable
        #remove failsafe of pyautogui
        pyautogui.FAILSAFE = False
        if(total_profiles<1):
            print("Invalid total profiles, total profiles must be greater than 0")
            thread_work_completed=True
            return None
        else:
            self.total_profiles=total_profiles                        #Sets total profiles for automation
        self.screen_width, self.screen_height = pyautogui.size()  #gets the screen size
        self.total_adds=total_adds                                #set to 7, 6 is exact

        if(starting_profile<1 or starting_profile>total_profiles):#checks if starting profile is valid or not
            print("Invalid starting profile, starting profile must be 1<=starting_profile<=total_profiles")
            thread_work_completed=True
            return None
        else :
            self.starting_profile=starting_profile                  #sets the starting profile
        self.browser_opener()
        thread_work_completed=True
        
    def browser_opener(self):
        """this func will handle the browser opener"""
        os.system("start brave")              #starts edge broswer
        time.sleep(2)                         #wats for 2 seconds so that browser can open successfully
        pyautogui.press('tab')                #presses tab to select profile
        pyautogui.press('enter')              #presses enter to open profile
        if(self.starting_profile==1):
            print(f"Profile 1")              
            self.automator()                      #runs automator method to start automation works
            time.sleep(0.2)                       #wait a bit so that browser is ready to close
            self.starting_profile+=1

        for i in range(self.starting_profile,self.total_profiles+1):      #loops through the total profiles
            if(i in [12,13,14,15,17,19]):           #skips the profiles which are not working
                continue
            print(f"Profile {i}")
            time.sleep(1)                         #wait a bit so that browser is ready to close 
            pyautogui.hotkey('ctrl','shift','m')  #opens profile view
            time.sleep(0.2)                       #wait a bit so that browser is ready to close
            for j in range(i-2):
                pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(0.2)                       #wait a bit so that browser is ready to close
            self.automator()                      #runs automator method to start automation works
            pyautogui.hotkey('alt', 'f4')         #closing profiles to save RAM from getting full
        # pyautogui.hotkey('alt', 'f4')             #closing main profile

    def new_tab(self):
        """This func will open new tab properly """
        time.sleep(0.5)                 #sets delay in pressing tabs so that browser can load properly
        pyautogui.hotkey('ctrl','t')    #opens new tab
        time.sleep(1)                   #sets delay so that new tab can open properly
        pyautogui.click(128,205)        #Random click to get out of address bar

    def get_pixel_color_from_screen(self,x, y):
        """This func will return the pixel color at the given coordinates in RGB format"""
        screenshot = pyautogui.screenshot() #takes screenshot
        image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())  #Convert the screenshot to a Pillow Image
        pixel_color = image.getpixel((x, y))  # (R, G, B) tuple for coordinates (x, y)
        return pixel_color
        
    def check_news_present(self):
        """This func will check if news is present or not
            by check the darkness of the news section
        """
        screenshot = pyautogui.screenshot()
        img = np.array(screenshot) # Convert the image to a NumPy array
        x1, y1, x2, y2 = (705, 212, 1215, 420) # Extract region of interest based on provided coordinates
        threshold = 90 # Set threshold for determining "darkness"
        roi = img[y1:y2, x1:x2]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) # Convert the region to grayscale
        average_brightness = np.mean(gray_roi) # Compute the average brightness within the region
        is_dark_region = average_brightness < threshold # Determine if the region is dark based on the threshold
        return not is_dark_region

    def first_news_view(self):
        """this func will open first news so that all the ads will show up"""
        # https://www.digitaltrends.com/movies/underrated-amazon-prime-video-movies-winter-2024/
        #type it using pyautogui
        self.new_tab()
        news_link="https://www.digitaltrends.com/movies/underrated-amazon-prime-video-movies-winter-2024/"
        time.sleep(1)
        pyautogui.click(574,65)
        pyautogui.typewrite(news_link)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl','w')            #closes the news view tab
        # time.sleep(0.2)
    
    def take_screenshot(self):
        """This func will take screenshot and return it"""
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        return screenshot

    def check_image_presence(self,template_path):
        """This func will check if the template image is present in the screenshot"""
        template = cv2.imread(template_path)
        screenshot = self.take_screenshot()
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Adjust this threshold based on your needs
        locations = np.where(result >= threshold)
        return len(locations[0]) > 0
    
    def news_activator(self):
        """this func will activate the news is add is not showing up"""
        self.new_tab()
        news_link="https://www.digitaltrends.com/movies/underrated-amazon-prime-video-movies-winter-2024/"
        time.sleep(1)
        pyautogui.click(574,65)
        pyautogui.typewrite(news_link)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl','w')            #closes the news view tab  

    def wait_for_news_load(self):
        """This func will wait for the news to load properly"""
        # self.news_activator()
        for i in range(3):
            self.new_tab()
            for _ in range(7):
                if(self.check_image_presence("news.png")):
                    time.sleep(1)
                    pyautogui.click(945,840)
                    time.sleep(1.2)
                    return 1
                time.sleep(1)
            pyautogui.hotkey('ctrl','w')
        return -1
    
    def add_view_handler(self):
        """this func will make sure to view all adds """
        x = self.screen_width // 2              #finds the centre of the page on x axis
        not_add_present=0                        #sets the counter for adds not present  
        for i in range(self.total_adds):        #loops through the total adds
            time.sleep(1)
            pyautogui.scroll(-1000)         #scrolls down to add
            time.sleep(1)                   #sets delay so that page can load properly
            if(not self.check_image_presence("Ad_logo_new.png")):       #checks if add is present or not
                not_add_present+=1                  #increases the counter if add is not present
            if(not_add_present>=1):                 #checks if add is not present for 2 times
                break                               #breaks the loop
            pyautogui.press('f5')               #refreshes the page for new add
        pyautogui.hotkey('ctrl','w')            #closes the add view tab
        time.sleep(0.1)                         #waits till current tab closes

    def window_maximise(self):
        """this func will maximise the window"""
        pyautogui.hotkey('alt','space')            #maximises the window
        pyautogui.press('x')                       #maximises the window
        time.sleep(0.1)

    def automator(self):
        """this function will handle all the process to automate particular page"""
        time.sleep(0.7)             #sets delay in pressing tabs so that browser can load properly
        self.wait_for_news_load()      #opens first news
        self.add_view_handler()     #handles all the adds to view properly

def program_terimator():
    """Terminates the whole program if 'q' is pressed or Ctrl+C is used."""
    try:
        while True:
            if keyboard.is_pressed('q') or thread_work_completed:            #checks it 'q' is pressed
                print("Jai shree ram")
                exit()                              #terminates the whole program
            time.sleep(0.1)                         #sets delay so that cpu can rest a bit
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Terminating the program.")
        exit()                                      #terminates the whole program
if __name__ == '__main__':
    total_profiles=24
    total_adds=7
    starting_profile=1                #it must be 1<=starting_profile<=total_profiles
    thread_work_completed = False     # Initialize the global variable
    automation_thread = threading.Thread(target=Automate_brave, args=(total_profiles,total_adds,starting_profile,),daemon=True) #daemon is set true so that program can be terminated by pressing 'q'
    automation_thread.start()         #starts the thread
    program_terimator()               #starts the program terminator