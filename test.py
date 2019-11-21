import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord%2B%E6%B3%95%E5%BE%8B%2B1%2B%E6%B3%95%E5%BE%8B&searchView=text")
print("@")
while 1:
    start = time.clock()
    try:
        #<input type="text" class="ui-widget-content ui-autocomplete-input" autocomplete="off" placeholder="输入“?”定位到当事人、律师、法官、法院、标题、法院观点">
    #    ActionChains(driver).move_to_element(driver.find_elements_by_class_name("login-btn")).perform()
        driver.find_element_by_class_name("login-btn").click()
        time.sleep(1)


        driver.find_element_by_xpath("//input[@id='username']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='username']").clear()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='username']").send_keys("13667272850")
        time.sleep(1)

        driver.find_element_by_xpath("//input[@id='password']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='password']").clear()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='password']").send_keys("mssjwow123")
        time.sleep(1)
        driver.find_element_by_class_name("submit").click()
        time.sleep(5)

        driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").click()
        driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").clear()
        driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").send_keys("山西")
        time.sleep(3)
        driver.find_element_by_class_name("search-box-btn").click()
      #  driver.find_element_by_link_text("结果中搜索").click()
       # driver.find_element_by_xpath("//div[@id='search-mode-dropown']/span").click()
        print ('已定位到元素')
        end=time.process_time()
        break
    except:
        print ("还未定位到元素!")

print ('定位耗费时间：'+str(end-start))
#driver.find_element_by_class_name("login-btn").click()
#a1=driver.find_elements_by_xpath("//span[2]")

#driver.find_element_by_xpath("//div[@id='search-mode-dropown']/span").click()
print('user success!')




# driver.find_element_by_xpath("//*[@class='hide-tip']")
# print("1")
# ActionChains(driver).move_to_element(driver.find_element_by_class_name("hide-tip")).perform()
# driver.find_element_by_class_name("hide-tip").click()
#driver('[ng-click="hideSubSiteTip()"]').click()

# <div class="subSite-Tip ng-scope" ng-if="showSubSiteTip">
#         <div class="tip-area">
#             <img class="tip" src="images/welcome/subSite-tip.png">
#             <img class="hide-tip" src="images/welcome/hide-tip.png" ng-click="hideSubSiteTip()">
#         </div>
#     </div>
#<img class="hide-tip" src="images/welcome/hide-tip.png" ng-click="hideSubSiteTip()">
#elements = driver.findElements(By.xpath("//*[@ng-click="hideSubSiteTip()']"));
#elements.get(1).click();
#elem = driver.find_element_by_class_name("hide-tip")

#elem.click("hideSubSiteTip")
#elem.send_keys(Keys.RETURN)
