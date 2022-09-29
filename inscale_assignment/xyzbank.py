
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner

class XYZBANK(unittest.TestCase):

    def setUp(cls):
        PATH = (r"C:\Users\hpadmin\Desktop\inscale_assignment\inscale_assignment\chromedriver\chromedriver.exe")
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        time.sleep(5)
        print(cls.driver.title)
    
    def test_xyzBankTest(self):

        MANAGERLOGIN = self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-lg'and @ng-click='manager()']")
        MANAGERLOGIN.send_keys(Keys.RETURN)
        MANAGERLOGIN.click()

        time.sleep(5)

        BUTTONADDCUSTOMER = self.driver.find_element(By.XPATH,"//button[@ng-click='addCust()']")
        BUTTONADDCUSTOMER.send_keys(Keys.ENTER)
        time.sleep(5)


        list_1 = [['Chrisopher'	,'Connely',	'L789C349'], ['Frank','Christopher','A897N450'], ['Christopher','Minka'	,'M098Q585'],
        ['Connely'	,'Jackson',	'L789C349'], ['Jackson'	,'Frank','L789C349'], ['Minka','Jackson','A897N450'],
        ['Jackson',	'Connely','L789C349'], ['Lawrence','Zimmerman','L789C349'], ['Mariotte','Tova','L789C349']]


        for query in list_1:
            self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']").send_keys(query[0])
            time.sleep(1)
            self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']").send_keys(query[1])
            time.sleep(1)
            self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']").send_keys(query[2])
            self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
            time.sleep(1)
            self.driver.switch_to.alert.accept()
            time.sleep(1)


        CUSTOMERBUTTON = self.driver.find_element(By.XPATH,"//button[@ng-class='btnClass3' and @ng-click='showCust()']")
        CUSTOMERBUTTON.click()
        time.sleep(5)


        #print all customer name on console to verify

        rows = len(self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr"))
        columns = len(self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td"))-1

        print("Number of Rows:", rows)
        print("Number of Columns:", columns)

        for row in range(2, rows+1):
            for col in range(1,columns+1):
                value = self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr["+str(row)+"]/td["+str(col)+"]")
                print(value[0].text)
            print()


        #Delete 2 Customer

        SEARCHNAME1 = self.driver.find_element(By.XPATH,"//input[@type='text' and @ng-model='searchCustomer']")
        SEARCHNAME1.click
        time.sleep(1)
        SEARCHNAME1.send_keys("Jackson")
        time.sleep(2)

        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td[5]/button").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//input[@type='text' and @ng-model='searchCustomer']").clear()
        time.sleep(1)

        SEARCHNAME2 = self.driver.find_element(By.XPATH,"//input[@type='text' and @ng-model='searchCustomer']")
        SEARCHNAME2.click
        time.sleep(1)
        SEARCHNAME2.send_keys("Christopher")
        time.sleep(2)

        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[5]/button").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH,"//input[@type='text' and @ng-model='searchCustomer']").clear()
        time.sleep(1)  


    
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test complete')
        



if __name__ == '__main__':  
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\hpadmin\Desktop\inscale_assignment\inscale_assignment\report'))









