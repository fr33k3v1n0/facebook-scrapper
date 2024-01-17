import os
import time
import datetime
import requests
import bs4
import getpass
#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#openpyxl
from openpyxl.workbook import Workbook
#
from termcolor import cprint, colored
from bs4 import BeautifulSoup

#own module
from facebook import constants as const
from facebook.utils import *
from facebook.collector import CollectPosts


class Groupe():
    def __init__(self, name,  member,  last_visited, admins, picture, link ):
        """
        @all information  about a groupe
        """
        self.name = name
        self.member = member
        self.last_visited = last_visited
        self.admins = admins
        self.picture = picture
        self.link = link 



class Message():
    pass


class Post():
    pass

class Friend():
    def __init__(self, name:str, common_friends:int,  profile_link:str, picture_link:str):
        self.name = name
        self.common_friends = common_friends
        self.profile_link = profile_link
        self.picture_link = picture_link
        



class Facebook(webdriver.Firefox):

    def __init__(self, driver_path):
        super(Facebook, self).__init__()
        #self = self# web br
        self.__login = False
        #self.collector = CollectPosts(self.driver)
        self.verbose = True 
        self.cosole_print = False
        #self.__login_url = const.LOGIN_URL
        #self.__base_url = const.bASE_URL 
        #configure the brosheeter driver
        os.environ["PATH"] +=driver_path 
        self.workbook = Workbook()
        self.sheet= self.workbook.active
        self.filename = 'faceboo_scrapper'
        #excel_header(self.sheet, "FACEBOOK SCRAPER || Friend List ||", ["Name", "Common Friend(s)", "Profile Link", "Profile picture"])
    
    def __exit__(self):
        self.workbook.save(self.filename + '.xlsx')

    def login(self):
        """
        @description: login user to his facebook account
        #we lauch the brosheeter, open facebook login page and invite user to go login
        #if user login to the brosheeter, the current url will change to main page
        """
        self.get(const.LOGIN_URL)
        cprint("Go to browser window and login to your facebook account !!", 'green')
        time.sleep(10) #wait user to login
        self.implicitly_wait(10)
        while self.current_url != const.bASE_URL:
            #user is not login
            cprint("Wainting for Login", "blue")
            time.sleep(5)
        
        cprint("GOOD:  you are now login: you can start scraping !! ", 'green')
        self.__login = True
        self.minimize_window()


    def show_actions_list(self):
        """
        @description:
            show differente actions which user can perform
            after login
        """
        print(
            f"""
            SELECT ACTION TO PERFORM:
            1:  {colored("Scrap FB Friends List", 'blue')}
            2:  {colored("Scrap FB Groups List", 'blue')}
            3:  {colored("Scrap Post from FB Group", 'blue')}
            4:  {colored("Scrap FB Group  Members", 'blue')}
            5:  {colored("Scrap FB pages  list", 'blue')}
            6:  {colored("Scrap post from FB Page ", 'blue')}
            00: {colored("Exit the program ", 'red')}
            """
        )
    
    def fb_grp_exist(self, group_name:str):
        """
        @description: try to confirm if a facebook groupe  groupe_name exist and if user is added on it
        """
        pass
    def msg_grp_exist(self, group_name:str):
        """
        @description: try to confirm if a facebook groupe  groupe_name exist and if user is added on it
        """

    def get_messages_from_grp(self, group_name:str, limit=0):
        """
        @groupe_name: the name of groupe
        @limit: limit of message to get
        @description:
            get limit messages from messenger {groupe_name} groupe .
            if limite = 0, get all messages from the groupe
        """
        if self.msg_grp_exist(group_name):
            #code to get all message here
            pass
        else:
            print(f"you havn' {group_name} groupe on your messenger groupes") 

    def get_post_from_grp(self, group_name:str, limit=0):
        """
        @groupe_name: the name of groupe
        @limit: limit of message to get
        @description:
            get limit post  from facebook {groupe_name} groupe .
            if limite = 0, get all post from the groupe
        """
        if self.fb_grp_exist(group_name):
            #code to get all message here
            pass
        else:
            print(f"you havn' {group_name} groupe on your messenger groupes") 

    def get_fb_grp_members(self, group_name, limit=0):
        """
        @groupe_name: the name of groupe
        @limit: limit of member to get default 0. 
            if limit= 0; we get all members from the groupe
        """
        pass
    def get_msg_grp_members(self, group_name, limit=0):
        """
        @groupe_name: the name of groupe
        @limit: limit of member to get default 0. 
            if limit= 0; we get all members from the groupe
        """
        pass
    def htmlSource_to_friend(self, html_code):
        """
            @take the source code of html element selected by self.find_element(By.CSS_SELECTOR, "div[class='xu06os2 xwya9rg']")
                and return Friend objet witch contain all  information about this friend

        """
        soup = BeautifulSoup(html_code, 'lxml')
        name = soup.find(name='span', class_="x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x6prxxf xvq8zen x1s688f xzsf02u").text 
        try:
            common_friends = str_to_int(soup.find('span', class_="x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1nxh6w3 x1sibtaa xo1l8bm xi81zsa").text) 
        except:
            common_friends = 0
        profile_picture = soup.find(name='image')['xlink:href'] 
        profile_link =  soup.find('a')['href']
        #if input("Print info to console? (y/n)").lower() == 'y':
        if self.verbose:
            print(
                f"""
                Friend Name:  {colored(name, 'green')}\n
                common friend: {colored(str(common_friends) + " Friend(s)", 'green')} \n
                profile picture: {colored(profile_picture, 'green')} \n  
                profile link: {colored(profile_link, 'green')}
                """
            )
        return Friend(name, common_friends,profile_link,  profile_picture)

    def save_friend(self, friend:Friend, sheet):
        """ 
        @description:
            save friend object in excel file 
        """
        sheet.append([friend.name, friend.common_friends, friend.profile_link, friend.picture_link])

    def get_friends_list(self, limit=0):
        """
        @limit : the number of friends to get
            if limit = 0: we get all
        @description:
            get the list of user's friend

            """
        excel_header(self.sheet, "FACEBOOK SCRAPER || Friend List ||", ["Friend Name", "Common Friend(s)", "Profile Link", "Profile picture"])
        self.get(const.FRIEND_LIST_URL)
        self.implicitly_wait(10)
        self.get(const.FRIEND_LIST_URL)
        #get total friend
        friend_number_span = self.find_element(By.CSS_SELECTOR, "div[class='xu06os2 xwya9rg']")
        self.friend_number = friend_number_span.text
        self.friend_number = str_to_int(self.friend_number)
        cprint(f"INFO: you have: {self.friend_number} Friend(s)", "blue")
        try:
            limit = int(input("how many friend info  do you wan to scrap? 0 to scrape all: "))
        except:
            pass
        limit = limit and limit or  self.friend_number # limit ? limit : self.friend_number 
        if(limit > 100):
            cprint(f"WARNING:  you wan to scrap {limit} friend info.! that can take some time", 'yellow')
        self.friend_file = input("Enter the file name in whitch you wan to save result: ")
        cprint("wait until we scrap all friend info ......")
        
        #get all friends list
        self.implicitly_wait(20)
        banner = self.find_elements(By.CSS_SELECTOR, "div[class='xb57i2i x1q594ok x5lxg6s x78zum5 xdt5ytf x6ikm8r x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck x1l7klhg x1iyjqo2 xs83m0k x2lwn1j xx8ngbg xwo3gff x1oyok0e x1odjw0f x1e4zzel x1n2onr6 xq1qtft']")
        if len(banner) == 2:
            banner = banner[1]
        else:
            banner = banner[0]
        self.implicitly_wait(100)
        #get focus on friend list banner in order to make some scroll
        actions = ActionChains(self, 100)
        actions.move_to_element(friend_number_span)
        actions.send_keys_to_element(friend_number_span, Keys.LEFT)
        actions.send_keys(Keys.LEFT)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        #know we can scroll until we get all the friend list
        friend_selector =  "div[data-visualcompletion='ignore-dynamic']"
        #now we have all information about friend:
        #we can scrap it and stort to a file
        #element_source = banner.find_elements(By.CSS_SELECTOR, friend_selector)[0].get_attribute("innerHTML")
        for i in range(limit):
            while len(banner.find_elements(By.CSS_SELECTOR, friend_selector)) < i+1: # self.friend_number:
                actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
                #we scroll down to get more groupe
                self.implicitly_wait(5)
            element = banner.find_elements(By.CSS_SELECTOR, friend_selector)[i]
            element_source = element.get_attribute("innerHTML") 
            soup = BeautifulSoup(element_source, 'lxml')
            friend = self.htmlSource_to_friend(element_source)
            self.save_friend(friend, self.sheet)
        self.workbook.save(self.friend_file +'.xlsx')
        
    def htmlSource_to_group(self, html):
        """
        @description:
            take a div which contain information about a group and return an objet group
        """
        soup = BeautifulSoup(html, "lxml")
        group_name = soup.find_all(name='a')[1].text
        group_link = soup.find_all(name='a')[1]['href']
        group_image = soup.find(name='image')['xlink:href']
        last_visited = soup.find(attrs={'class': "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft"}).text
        #let get more information about the groupe
        #let open new tab and get more info
        s = requests.session()
        s.headers.update({"User-Agent": self.execute_script("return navigator.userAgent")})
        for cookie in self.get_cookies():
            c = {cookie['name']: cookie['value']}
            s.cookies.update(c)
        info_page = requests.get(group_link, allow_redirects=True)
        time.sleep(10)
        print(info_page.status_code)
        info_soup = BeautifulSoup(info_page.text, 'lxml')
        #with open("result.html", 'w') as f:
        #    f.write(info_soup.prettify())
        for l in info_soup.find_all('span'): 
            print("that work: " + l.text)
        self.execute_script("window.open(' ');")
        self.switch_to.window(self.window_handles[1])
        #get group info on the new tab
        self.get(group_link + "members/admins")
        self.implicitly_wait(2)
        group_members = str_to_int(self.find_element(By.TAG_NAME, 'strong').text) #the total member of the groupe
        admins_divs = self.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]') 
        admins = [admin.find_elements(By.TAG_NAME, 'span')[2].text for admin in admins_divs]
        if self.verbose:
            print(
                f""" 
                {colored("groupe information:", 'blue') }
                name: {colored(group_name, 'green')}
                link: {colored(group_link, 'green')}
                image link: {colored(group_image, 'green')}
                last visited: {colored(last_visited, 'green')}
                members: {colored(group_members, 'green')}
                admins: {colored(admins, 'green')}
            """
            )
        #reswitch to the main tab and close the new on
        self.close()
        self.switch_to.window(self.window_handles[0])
        return Groupe(group_name, group_members, last_visited, admins, group_image, group_link)
    
    def save_group_info(self, group):
        """
        @description:
            wirte groupe information into excel file

        """
        self.sheet.append([group.name, group.member, group.last_visited, " || ".join(group.admins), group.picture, group.link])
        self.workbook.save(self.filename + '.xlsx')


    def get_groups_list(self, limit=0):
        """
        @limit: the limit of user's groups to get
        @description:
            get uers's added groupe list
        """
        excel_header(self.sheet, "FACEBOOK SCRAPER || GROUP List ||", ["Goup Name", "Members Count", "Last visited", "Administrator(s)", "Image", "Groupe Link"])
        self.sheet.title = "Group List "
        self.get(const.GROUP_LIST_URL)
        self.implicitly_wait(50) #wait the page to load
        group_number_span = self.find_elements(By.CSS_SELECTOR, 'span[class="x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lkfr7t x1lbecb7 x1s688f xzsf02u"]')[1]
        self.group_number = str_to_int(group_number_span.text)
        print(f"You have {self.group_number} group(s)")
        try:
            limit = abs(int(input("how many groupe do you want to scrap? 0 to scrap all: ")))
        except:
            limit = 0 
        limit = limit > self.group_number and self.group_number or limit
        limit = limit and limit or self.group_number # if limit = 0, we scrap all
        #now we can start scrap group information
        self.filename = input("Enter the file name in which data will be stored: ")
        cprint(f"Wait until we scrap {limit} group(s) info...\nthat can take some time", 'green')
        actions = ActionChains(self, 4).click(group_number_span).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)
        actions.perform()
        #resetting the sheet
        self.sheet.column_dimensions["C"].width = 60
        self.sheet.row_dimensions[1].alignment = Alignment(horizontal="left", indent='30')
        #save limit group
        for i in range(limit):
            groups = self.find_elements(By.CSS_SELECTOR, 'div[role="list"]')[1].find_elements(By.CSS_SELECTOR, "div[class='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x150jy0e x1e558r4 xjkvuk6 x1iorvi4 xnpuxes']")
            print(groups[i].find_elements(By.TAG_NAME, 'a')[1].text)
            self.implicitly_wait(15)
            while len(groups) < i+1 :
                    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
                #we scroll down to get more groups
            group = self.htmlSource_to_group(groups[i].get_attribute("innerHTML"))
            self.save_group_info(group)
            
            time.sleep(60)
     
            