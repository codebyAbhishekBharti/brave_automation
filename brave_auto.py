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

class Automate_brave:
    def __init__(self,total_profiles,total_adds=6,starting_profile=1):
        global thread_work_completed  # Use the global keyword to modify the global variable
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
            self.starting_profile=starting_profile-1                  #sets the starting profile
        self.browser_opener()
        thread_work_completed=True
    
    def browser_opener(self):
        """this func will open the browser and start the automation"""
        for i in range(self.starting_profile,self.total_profiles):      #loops through the total profiles
            print(f"Profile {i+1}")               #prints on which profile current automation is going on
            os.system("start brave")              #starts edge broswer
            time.sleep(2)                         #wats for 2 seconds so that browser can open successfully
            pyautogui.press('tab')                #presses tab to select profile
            for j in range(3*i):                  #presses tab multiple times to select exect profile
                pyautogui.press('tab')
                # time.sleep(0.1)                 #sets delay in pressing tabs
            pyautogui.press('enter')              #presses enter to open profile
            # do your work here 
            self.automator()                      #runs automator method to start automation works
            time.sleep(0.2)                       #wait a bit so that browser is ready to close
            pyautogui.hotkey('alt', 'f4')         #closing profiles to save RAM from getting full

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

    def first_news_view(self):
        """this func will open first news so that all the ads will show up"""
        pyautogui.press('pagedown')    #scrolls down the page
        time.sleep(4.5)                #sets delay so that news can open properly
        self.window_centre_click()     #clicks on the news 
        time.sleep(1)                  #sets delay for the news to open

    def add_view_handler(self):
        """this func will make sure to view all adds """
        x = self.screen_width // 2              #finds the centre of the page on x axis
        for _ in range(self.total_adds):        #loops through the total adds
            pyautogui.click(x,300)              #clicks anywhere on screen to make sure that page is in view
            time.sleep(0.2)                     #sets delay so that page can load properly
            for i in range(2):                  #loops so that add will be in view
                pyautogui.press('pagedown')
                time.sleep(1)                   #sets delay so that page can load properly
            time.sleep(2)
            pyautogui.press('f5')               #refreshes the page for new add
        pyautogui.hotkey('ctrl','w')            #closes the add view tab
        time.sleep(0.1)                         #waits till current tab closes
        pyautogui.hotkey('ctrl','w')            #closes the news view tab

    def automator(self):
        """this function will handle all the process to automate particular page"""
        time.sleep(0.7)             #sets delay in pressing tabs so that browser can load properly
        self.new_tab()              #opens new tab
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
    
    total_profiles=18
    total_adds=7
    starting_profile=1                #it must be 1<=starting_profile<=total_profiles
    thread_work_completed = False     # Initialize the global variable
    automation_thread = threading.Thread(target=Automate_brave, args=(total_profiles,total_adds,starting_profile,),daemon=True) #daemon is set true so that program can be terminated by pressing 'q'
    automation_thread.start()         #starts the thread
    program_terimator()               #starts the program terminator