from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot: #Sets up bot commands
    def __init__(self, username, password): #Gets username and password and opens up Firefox
        self.username= username
        self.password= password
        self.bot= webdriver.Firefox(executable_path= r"\Users\kingj\AppData\Local\Programs\Python\Python37-32\geckodriver")
        
    def login(self): #Logs into Twitter
        bot= self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email= bot.find_elements_by_name('session[username_or_email]')[1]
        password= bot.find_elements_by_name('session[password]')[1]
        email.clear() #Clears email if one is already present
        password.clear() #Clears password if one is already present
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        
    def like_tweet(self,hashtag): #Likes the tweets when found
        bot=self.bot
        bot.get('https://twitter.com/search?q='+ hashtag+ '&src=typd') #Opens the Twitter search
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets=bot.find_elements_by_class_name('tweet')
            links=[elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' +link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click() #Likes the Tweet
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)
        
ed=TwitterBot('Email', 'Pass')
ed.login()
ed.like_tweet('Example')