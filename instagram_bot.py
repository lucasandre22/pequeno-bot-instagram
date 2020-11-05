from selenium import webdriver
from time import sleep
import string
import random

class bot : 
    def __init__(self, username, password) : 
        self.driver = webdriver.Chrome(r"C:\Users\Lucas-PC\chromedriver")
        self.driver.get("https://www.instagram.com")
        self.username = username
        self.password = password
        sleep(2) #sleep para carregar a pagina
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(5)
        
        #/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[1]/div[3]/section[1]/span[1]/button/div/span/svg path para curtir fotos
        #/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[2]/div[3]/section[1]/span[1]/button/div/span/svg path para curtir fotos
        
    def UnfollowAccountFollowers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").click()
        sleep(2)
        link1 = "/html/body/div[4]/div/div/div[2]/ul/div/li["
        link2 = "]/div/div["
        link3 = "]/button"
        rangescroll = 1
        rangescroll2 = 3
        while True :
            aux = (link1) + str(rangescroll) + (link2) + str(rangescroll2) + (link3)
            self.driver.find_element_by_xpath(aux).click()
            rangescroll += 1
            print(rangescroll)
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
            if rangescroll == 13:
                rangescroll2 = 2
            sleep(3)

    def FollowAllUsernameFollowers(self, username_to_search):
        self.username_to_search = username_to_search
        self.SearchUsername()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click() #clica followers
        sleep(5)
        self.link1 = "/html/body/div[4]/div/div/div[2]/ul/div/li["
        self.link2 = "]/div/div["
        self.link3 = "]/button"
        rangescroll = 1
        rangescroll2 = 3
        while True :
            aux = (self.link1) + str(rangescroll) + (self.link2) + str(rangescroll2) + (self.link3)
            self.driver.find_element_by_xpath(aux).click()
            rangescroll += 1
            print(rangescroll)
            if rangescroll == 13:
                rangescroll2 = 2
            sleep(5)

    def RandomCommentsOnUsernameLastPost(self, username_to_search):
        self.username_to_search = username_to_search

        self.SearchUsername()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div[1]").click() #clica last post
        sleep(2)
        self.driver.refresh()
        sleep(3)
        while True :
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
            for j in range(4):
                length1 = random.randint(1,11)
                length2 = random.randint(1,11)
                letters = string.ascii_letters
                result_str = ''.join(random.choice(letters) for i in range(length1))
                result_str += ' '
                result_str += ''.join(random.choice(letters) for i in range(length2))
                try:
                    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(result_str)
                except: 
                    sleep(random.randint(8,20))
                    break
                sleep(1)
                try:
                    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
                except: 
                    sleep(random.randint(8,20))
                    break
                sleep(3)
            self.driver.refresh()
            sleep(5)
    
    def RandomCommentsOnUsernameLastPost2(self):
        self.driver.get("https://www.instagram.com/p/CFSGUrOl4Ll/")
        j = 0
        sleep(5)
        while True :
            length1 = random.randint(1,11)
            length2 = random.randint(1,11)
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length1))
            result_str += ' '
            result_str += ''.join(random.choice(letters) for i in range(length2))
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
            sleep(2)
            try:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(result_str)
            except: 
                sleep(random.randint(2,6))
            sleep(2)
            try:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
            except: 
                j += -1
                sleep(random.randint(2,6))
            sleep(random.randint(13,30))
            self.driver.refresh()
            sleep(5)
            j += 1
            print(j)

    def SearchUsername(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(self.username_to_search) #procura username
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span").click() #clica username
        sleep(3)

    def NavigateAndLikeHashtagPhotos(self, hashtag):
        self.driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
        sleep(2)
        #for i in range(1,3):
            #self.driver.execute(window.scrollTo(0, document.body.scrollHeight))
            #sleep(2)
        self.j = 0
        self.i = 0
        while True:
            self.LikePhoto()
            if self.j == 0:
                self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click() #clica proxima foto primeira vez
                self.j += 1
            else:
                self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click() #clica proxima foto proximas vezes
            sleep(2)
            self.i += 1
            print(self.i)
    
    def LikePhoto(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button").click() #clica botao like
        except:
            print(self.j)
            self.j += 1
            self.i += -1
        sleep(1)
            

        
def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(letters)
    print("Random string is:", result_str)
        

            
my_bot = bot('username','password')
#my_bot.UnfollowAccountFollowers()
#my_bot.FollowAllUsernameFollowers('username')
my_bot.NavigateAndLikeHashtagPhotos('hashtag')
#my_bot.RandomCommentsOnUsernameLastPost()
#my_bot.RandomCommentsOnUsernameLastPost2()