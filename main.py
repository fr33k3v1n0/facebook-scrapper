"""
@project_name: facebook scraper 
@author: IROPA ZAKARIE
@email: zakarieiropa@gmail.com
@job: freelancer, python dev, web scraper, ctf player
@passion: cyber security
"""

"""
@description:
    this is a simple facebook scraper.
    with this programme, we can login to facebook and get :
        -- Friends list
        -- Groups (facebook | messenger) list 
        -- All message from on groupe
        -- All message chatted with one friend
        -- Notification list
        -- And so on
"""
import os
from os import system 
from termcolor import cprint
from facebook.facebook import Facebook

if __name__ == "__main__":
    system("clear || cls")
    os.environ['PATH'] += "/user/bin" #location of webdriver
    print(
        '''
 _______                 _                 _                                                 
(_______)               | |               | |                                                
 _____ _____  ____ _____| |__   ___   ___ | |  _     ___  ____  ____ _____ ____  _____  ____ 
|  ___|____ |/ ___) ___ |  _ \ / _ \ / _ \| |_/ )   /___)/ ___)/ ___|____ |  _ \| ___ |/ ___)
| |   / ___ ( (___| ____| |_) ) |_| | |_| |  _ (   |___ ( (___| |   / ___ | |_| | ____| |    
|_|   \_____|\____)_____)____/ \___/ \___/|_| \_)  (___/ \____)_|   \_____|  __/|_____)_|    
                                                                          |_|                
 _                          _                 _                                              
| |                        | |               (_)                                             
| |__  _   _    _____ _____| |  _ _____  ____ _ _____                                        
|  _ \| | | |  (___  |____ | |_/ |____ |/ ___) | ___ |                                       
| |_) ) |_| |   / __// ___ |  _ (/ ___ | |   | | ____|                                       
|____/ \__  |  (_____)_____|_| \_)_____|_|   |_|_____)                                       
      (____/                                             
        '''
    )

fb = Facebook("/usr/bin")
fb.login()
#fb.show_actions_list()
fb.show_actions_list()
action = input(": ")
if action.strip() == '1':
    fb.get_friends_list()
elif action.strip() == '2':
    fb.get_groups_list()
else:
    cprint("You Select bad action, Bye!!", 'red')
