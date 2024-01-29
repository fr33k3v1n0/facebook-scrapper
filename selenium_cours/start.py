import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #emulate keybord
from selenium.webdriver.common.by import By 
#from selenium.webdriver.options import Options


#os.environ["PATH"]  += "chrom_exe_path" :confir the browser
os.environ["PATH"] += "/usr/bin/" 
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/login.php")
driver.implicitly_wait(30)
while driver.current_url != "https://www.facebook.com/":
    """login_form  = driver.find_element(By.ID, 'login_form')
    email_input = login_form.find_element(By.ID, "email")
    password_input = login_form.find_element(By.ID, "pass")
    email = input("Email or phone number: ")
    password = getpass.getpass("password: ")
    driver.implicitly_wait(300)
    email_input.send_keys(email)
    password_input.send_keys(password)
    response = login_form.submit()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)  # import time
    print(driver.current_url)
    with open('index.html', 'w') as f:
        f.write(driver.page_source)
    print("username or password incorrect !")
    """
    print("you need to login into facebook. go to your browser and do it")
    time.sleep(15)

print("you are login")
print(
    """
    select an action to perform
    1: ---
    2 : ---
    3: ---
    """

)

with open('index.html', 'w') as f:
    f.write(driver.page_source)

driver.close()