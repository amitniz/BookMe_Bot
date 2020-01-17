import os,timer,platform
from selenium import webdriver

#TODO: update the landing page..

class communication():

    #Constructor
    def __init__(self):
        # Sets the location of the chromedriver file

        if platform.system() == 'Linux':
            self.driver = webdriver.Chrome(os.path.dirname(__file__) + '/chromedriver_linux')
        elif platform.system() == "Windows":
            pass
        else:
            self.driver = webdriver.Chrome(os.path.dirname(__file__) + '/chromedriver_mac')
    # Goes to the reservation's url and submits
    def book(self):
        btn = self.driver.find_element_by_class_name('btn btn-success save create btnCreate')
        btn.click()

    # Login to Bookme
    def login_Old(self,email,password,addr): #Obst
        self.driver.get(addr) # Opens the given web page
        email_id = self.driver.find_element_by_id('email') # Searches for the email id
        password_id = self.driver.find_element_by_id('password') # Searches for the password id
        email_id.send_keys(email) # Fills the given email at the email location
        password_id.send_keys(password) # Fills the given password at the password location
        btn = self.driver.find_element_by_xpath("class='btn btn-success save create btnCreate']") # Searches for the submit button
        btn.click()# Clicks the submit button


    def login(self,email,password,addr):
        self.driver.get(addr)
        email_id =self.driver.find_element_by_id('i0116')
        email_id.send_keys(email)
        btn= self.driver.find_element_by_id('idSIButton9') # Email Button
        btn.click()
        passport_id = self.driver.find_element_by_id('i0118')
        passport_id.send_keys(password)
        timer.delay()
        btn_2 = self.driver.find_element_by_id('idSIButton9')
        btn_2.click()
        btn_3 = self.driver.find_element_by_id('idSIButton9')
        btn_3.click()
        reservation_btn = self.driver.find_element_by_xpath("//*[@class='btn btn-success save create btnCreate']")
        timer.delay()
        reservation_btn.click()

        #Not Finished

    def quit(self):
        self.driver.__exit__() #Closes the webdriver
