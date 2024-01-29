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
import threading
import keyboard
from PIL import Image

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
        
        self.loading_left_pixel = (928, 455)                      # Coordinates of the left pixel of the loading bar
        self.loading_right_pixel = (971, 455)                    # Coordinates of the right pixel of the loading bar
        self.loading_top_pixel = (950, 434)                       # Coordinates of the top pixel of the loading bar
        self.loading_bottom_pixel = (950, 476)                    # Coordinates of the bottom pixel of the loading bar

        self.add_lower_left_pixel = (1329, 434)                    # Coordinates of the left pixel of the add icon
        self.add_lower_right_pixel = (1334, 434)                   # Coordinates of the right pixel of the add icon
        self.add_lower_bottom_pixel = (1332, 438)                  # Coordinates of the bottom pixel of the add icon
        self.add_lower_centre_pixel = (1332, 436)                  # Coordinates of the centre pixel of the add icon
        self.add_middle_left_pixel = (1329, 474)                    # Coordinates of the left pixel of the add icon
        self.add_middle_right_pixel = (1334, 474)                   # Coordinates of the right pixel of the add icon
        self.add_middle_bottom_pixel = (1332, 478)                  # Coordinates of the bottom pixel of the add icon
        self.add_middle_centre_pixel = (1332, 476)                  # Coordinates of the centre pixel of the add icon
        self.add_upper_left_pixel = (1329, 184)                    # Coordinates of the left pixel of the add icon
        self.add_upper_right_pixel = (1334, 184)                   # Coordinates of the right pixel of the add icon
        self.add_upper_bottom_pixel = (1332, 189)                  # Coordinates of the bottom pixel of the add icon
        self.add_upper_centre_pixel = (1332, 185)                  # Coordinates of the centre pixel of the add icon

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
        pyautogui.hotkey('alt', 'f4')             #closing main profile

    def window_centre_click(self):
        """this func will find the centre of the page and click at the centre"""
        x = self.screen_width // 2       #finds the centre of the page
        y = self.screen_height // 2      #finds the centre of the page
        pyautogui.click(x, y)            # Click on the center

    def new_tab(self):
        """This func will open new tab properly """
        time.sleep(0.5)                 #sets delay in pressing tabs so that browser can load properly
        pyautogui.hotkey('ctrl','t')    #opens new tab
        time.sleep(1)                   #sets delay so that new tab can open properly
        self.window_centre_click()      #clicks on the centre of the page so that page view can be worked on not the address bar
    
    def get_pixel_color_from_screen(self,x, y):
        """This func will return the pixel color at the given coordinates in RGB format"""
        screenshot = pyautogui.screenshot() #takes screenshot
        image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())  #Convert the screenshot to a Pillow Image
        pixel_color = image.getpixel((x, y))  # (R, G, B) tuple for coordinates (x, y)
        return pixel_color

    def check_news_present(self):
        """This func will check if news is present or not"""
        total_match=0
        RGB_Values = (132,136,156)   #RGB values of the loading icon
        if(self.get_pixel_color_from_screen(*self.loading_left_pixel)==RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.loading_right_pixel)==RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.loading_top_pixel)==RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.loading_bottom_pixel)==RGB_Values):
            total_match+=1
        if(total_match>=2):
            return False 
        else:
            return True

    def first_news_view(self):
        """this func will open first news so that all the ads will show up"""
        for i in range(4):              #loops so that news will show up
            self.new_tab()              #opens new tab
            pyautogui.press('pagedown')    #scrolls down the page
            time.sleep(1)             #sets delay so that page can load properly
            flag=False
            for x in range(5):
                time.sleep(1)           #sets delay so that page can load properly
                if(self.check_news_present):
                    flag=True
                    break
            if(flag):
                self.window_centre_click() #clicks on the news
                time.sleep(1)              #sets delay for the news to open
                break
            else:
                print("News is not present")
            pyautogui.hotkey('ctrl','w')            #closes the news view tab
    
    def check_add_present(self):
        """This func will check if add is present or not"""
        total_match=0
        Red_RGB_Values = (255,71,36)
        Orange_RGB_Values = (158, 31, 99)
        Purple_RGB_Values = (102, 45, 145)
        White_RGB_Values = (255, 255, 255)
        if(self.get_pixel_color_from_screen(*self.add_lower_left_pixel)==Red_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_lower_right_pixel)==Orange_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_lower_bottom_pixel)==Purple_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_lower_centre_pixel)==White_RGB_Values):
            total_match+=1
        if(total_match>=4):
            return True
        total_match=0
        if(self.get_pixel_color_from_screen(*self.add_middle_left_pixel)==Red_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_middle_right_pixel)==Orange_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_middle_bottom_pixel)==Purple_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_middle_centre_pixel)==White_RGB_Values):
            total_match+=1
        if(total_match>=4):
            return True
        total_match=0
        if(self.get_pixel_color_from_screen(*self.add_upper_left_pixel)==Red_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_upper_right_pixel)==Orange_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_upper_bottom_pixel)==Purple_RGB_Values):
            total_match+=1
        if(self.get_pixel_color_from_screen(*self.add_upper_centre_pixel)==White_RGB_Values):
            total_match+=1
        if(total_match>=4):
            return True
        
        return False

    def add_view_handler(self):
        """this func will make sure to view all adds """
        x = self.screen_width // 2              #finds the centre of the page on x axis
        not_add_present=0                        #sets the counter for adds not present
        for _ in range(self.total_adds):        #loops through the total adds
            pyautogui.click(x,300)              #clicks anywhere on screen to make sure that page is in view
            time.sleep(0.2)                     #sets delay so that page can load properly
            for i in range(2):                  #loops so that add will be in view
                pyautogui.press('pagedown')
                time.sleep(1)                   #sets delay so that page can load properly
            time.sleep(1)
            #below two lines has some problem
            if(not self.check_add_present()):       #checks if add is present or not
                not_add_present+=1                  #increases the counter if add is not present
            if(not_add_present>=2):                 #checks if add is not present for 2 times
                break                               #breaks the loop
            pyautogui.press('f5')               #refreshes the page for new add
        pyautogui.hotkey('ctrl','w')            #closes the add view tab
        time.sleep(0.1)                         #waits till current tab closes
        pyautogui.hotkey('ctrl','w')            #closes the news view tab

    def automator(self):
        """this function will handle all the process to automate particular page"""
        time.sleep(0.7)             #sets delay in pressing tabs so that browser can load properly
        self.first_news_view()      #opens first news
        self.new_tab()              #opens new tab
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
