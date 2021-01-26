#!/usr/bin/env python3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def heart(f):
    s = ""
    for row in range(6):
        for col in range(7):
            if(row==0 and col%3!=0)or(row==1 and col%3==0) or (row-col==2) or (row+col==8):
                s+=f+" "
            else:
                s+="  "
        s+="\n"
    return s


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name or group name:")
msg = input("Enter message:")
count = int(input("Enter count:"))

input("Enter anything after scan QR code")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Success")