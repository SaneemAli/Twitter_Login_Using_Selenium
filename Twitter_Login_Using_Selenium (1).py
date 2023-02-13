#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[52]:


# Script to Login to Twitter using (E-mail or username) and password
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

class Twitterbot:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name  
        

        chrome_options = Options()
        self.bot = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(6)
        email = bot.find_element(By.XPATH,"//input[@name='text']")
        email.send_keys(self.username)
        next_button = bot.find_element(By.XPATH, "//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")
        next_button.click()
        time.sleep(3)
        
        username = bot.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")
        username.send_keys(self.name)
        next_button = bot.find_element(By.XPATH, "//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")
        next_button.click()
        time.sleep(3)
        
        
        password = bot.find_element(By.XPATH, '//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        password.send_keys(self.password)
        login_button = bot.find_element(By.XPATH, '//div[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
        login_button.click()
        time.sleep(2)

# Loop to ask the user if they want to tweet or not
        while True:
            user_input = input("Do you want to tweet? (y/n): ")
            if user_input == "y":
                tweet_input = bot.find_element(By.XPATH,'//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')

        # Enter your tweet
                tweet_text = input("Enter your tweet: ")
                tweet_input.send_keys(tweet_text)
                time.sleep(3)

        # Submit the tweet
                tweet_button = bot.find_element(By.XPATH, '//div[@class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]').click()




        # Wait for the tweet to post
                time.sleep(2)

                print("Tweet posted!")
            else:
                break


        

f = Twitterbot("saneemali1@gmail.com", 'Hald1r@ms','Saneem_Ali')        
f.login()


# In[ ]:


\


# In[ ]:




