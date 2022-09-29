
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

        #Click button to add customer
        BUTTONADDCUSTOMER = self.driver.find_element(By.XPATH,"//button[@ng-click='addCust()']")
        BUTTONADDCUSTOMER.send_keys(Keys.ENTER)
        time.sleep(5)

        #Customer 1
        FIRSTNAMEADDCUSTOMER1 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER1.send_keys('Christopher')
        time.sleep(1)

        LASTNAMEADDCUSTOMER1 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER1.send_keys('Connely')
        time.sleep(1)

        POSTCODEADDCUSTOMER1 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER1.send_keys('L789C349')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 2

        time.sleep(1)

        #FIRSTNAMEADDCUSTOMER2 = driver.find_element(By.CSS_SELECTOR,"input.First Name")
        FIRSTNAMEADDCUSTOMER2 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER2.click()
        FIRSTNAMEADDCUSTOMER2.send_keys('Frank')
        time.sleep(1)


        LASTNAMEADDCUSTOMER2 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER2.click()
        LASTNAMEADDCUSTOMER2.send_keys('Christopher')
        time.sleep(1)

        POSTCODEADDCUSTOMER2 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER2.click()
        POSTCODEADDCUSTOMER2.send_keys('A897N450')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 3

        FIRSTNAMEADDCUSTOMER3 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER3.click()
        FIRSTNAMEADDCUSTOMER3.send_keys('Christopher')
        time.sleep(1)


        LASTNAMEADDCUSTOMER3 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER3.click()
        LASTNAMEADDCUSTOMER3.send_keys('Minka')
        time.sleep(1)

        POSTCODEADDCUSTOMER3 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER3.click()
        POSTCODEADDCUSTOMER3.send_keys('M098Q585')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 4

        FIRSTNAMEADDCUSTOMER4 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER4.click()
        FIRSTNAMEADDCUSTOMER4.send_keys('Connely')
        time.sleep(1)


        LASTNAMEADDCUSTOMER4 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER4.click()
        LASTNAMEADDCUSTOMER4.send_keys('Jackson')
        time.sleep(1)

        POSTCODEADDCUSTOMER4 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER4.click()
        POSTCODEADDCUSTOMER4.send_keys('L789C349')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 5

        FIRSTNAMEADDCUSTOMER5 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER5.click()
        FIRSTNAMEADDCUSTOMER5.send_keys('Jackson')
        time.sleep(1)


        LASTNAMEADDCUSTOMER5 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER5.click()
        LASTNAMEADDCUSTOMER5.send_keys('Frank')
        time.sleep(1)

        POSTCODEADDCUSTOMER5 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER5.click()
        POSTCODEADDCUSTOMER5.send_keys('L789C349')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 6

        FIRSTNAMEADDCUSTOMER6 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER6.click()
        FIRSTNAMEADDCUSTOMER6.send_keys('Minka')
        time.sleep(1)


        LASTNAMEADDCUSTOMER6 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER6.click()
        LASTNAMEADDCUSTOMER6.send_keys('Jackson')
        time.sleep(1)

        POSTCODEADDCUSTOMER6 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER6.click()
        POSTCODEADDCUSTOMER6.send_keys('A897N450')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 7

        FIRSTNAMEADDCUSTOMER7 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER7.click()
        FIRSTNAMEADDCUSTOMER7.send_keys('Jackson')
        time.sleep(1)


        LASTNAMEADDCUSTOMER7 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER7.click()
        LASTNAMEADDCUSTOMER7.send_keys('Connely')
        time.sleep(1)

        POSTCODEADDCUSTOMER7 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER7.click()
        POSTCODEADDCUSTOMER7.send_keys('L789C349')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 8

        FIRSTNAMEADDCUSTOMER8 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER8.click()
        FIRSTNAMEADDCUSTOMER8.send_keys('Lawrence')
        time.sleep(1)


        LASTNAMEADDCUSTOMER8 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER8.click()
        LASTNAMEADDCUSTOMER8.send_keys('Zimmerman')
        time.sleep(1)

        POSTCODEADDCUSTOMER8 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER8.click()
        POSTCODEADDCUSTOMER8.send_keys('L789C349')
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn btn-default']").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

        #Customer 9

        FIRSTNAMEADDCUSTOMER9 = self.driver.find_element(By.XPATH,"//input[@ng-model='fName' and @placeholder='First Name']")
        FIRSTNAMEADDCUSTOMER9.click()
        FIRSTNAMEADDCUSTOMER9.send_keys('Mariotte')
        time.sleep(1)


        LASTNAMEADDCUSTOMER9 = self.driver.find_element(By.XPATH,"//input[@ng-model='lName' and @placeholder='Last Name']")
        LASTNAMEADDCUSTOMER9.click()
        LASTNAMEADDCUSTOMER9.send_keys('Tova')
        time.sleep(1)

        POSTCODEADDCUSTOMER9 = self.driver.find_element(By.XPATH,"//input[@ng-model='postCd' and @placeholder='Post Code']")
        POSTCODEADDCUSTOMER9.click()
        POSTCODEADDCUSTOMER9.send_keys('L789C349')
        time.sleep(1)

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









#kalau nak tutup window
#driver.quit()
