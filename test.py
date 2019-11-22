from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
from pyquery import PyQuery as pq
from selenium.webdriver.common.action_chains import ActionChains
import pymongo
import time
from utils.configwusong import *
from xdaili import Xdaili
class Products(object):
    def __init__(self):
        """
        初始化
        """
        # 数据库配置
        self.client = pymongo.MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]
        # 代理配置
        self.auth = Xdaili().auth()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--start-maximized')
        self.chrome_options.add_argument('--headless')
        self.plugin_file = './utils/proxy_auth_plugin.zip'
        self.chrome_options.add_extension(self.plugin_file)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #    self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
    def spider(self):
     self.driver.get(URL)
     print("@")
     while 1:
            try:
                self.driver.find_element_by_class_name("login-btn").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@id='username']").click()
                self.driver.find_element_by_xpath("//input[@id='username']").clear()
                self.driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
                time.sleep(3)
                self.driver.find_element_by_xpath("//input[@id='password']").click()
                self.driver.find_element_by_xpath("//input[@id='password']").clear()
                self.driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
                self.driver.find_element_by_class_name("submit").click()
                time.sleep(5)
                self.driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").click()
                self.driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").clear()
                self.driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").send_keys("山西")
                self.driver.find_element_by_class_name("search-box-btn").click()
                time.sleep(3)
                #
                # j =1
                # while j<5:
                #     element = self.driver.find_element_by_xpath("//button[@class='view-more ng-scope']")
                #     element.click()
                #     time.sleep(3)
                #     j=j+1
                lit = self.driver.find_elements_by_class_name("judgement ng-scope")
                lis = self.driver.find_elements_by_xpath('//div[@class = "judgements"]/div[@class="judgement ng-scope"]')
                for i in range(len(lis)):
              #  for i in range(2):
                    print("开始点击")
                    i=i+1
                    div_str = '//div[@class="judgements"]/div[{}]/div[2]/h3/a'.format(i)
                    self.driver.find_element_by_xpath(div_str).click()
                    print("点击完成")
                    all_h = self.driver.window_handles
                    self.driver.switch_to.window(all_h[1])
                    h2 = self.driver.current_window_handle
                    print('已定位到元素')
                    time.sleep(1)
                    try:
                        self.get_products()
                    except:
                        print("product失败")
                    self.driver.close()
                    self.driver.switch_to.window(all_h[0])

                self.driver.close()
                print('关闭')
                #end = time.process_time()
                break
            except:
                print("还未定位到元素!")

    def get_products(self):
        try:
            # 获取网页源码
            wenshu=self.driver.find_element_by_xpath('//section[@class="paragraphs ng-isolate-scope"]').text
            print("wenshu:",wenshu)
            product = {
                     'wenshu': wenshu
                 }
           # print(product)
            self.save_to_mongo(product)
        except Exception:
            print("捕捉失败")
    def save_to_mongo(self, result):
        """
        存储至数据库
        :param result: 抓取的数据
        :return: None
        """
        print("到mongo了")
        try:
            if self.db[MONGO_COLLECTION].insert(result):
                print('存储到MONGODB成功', result)
        except Exception:
            print('存储到MONGODB失败', result)
    def main(self):
        self.spider()
if __name__ == '__main__':
    start=time.clock()
    taobao_product = Products()
    taobao_product.main()
    end=time.process_time()
    print('耗时：' + str(end - start))

    # def spider2(self):
    #     driver = webdriver.Chrome()
    #     driver.get(
    #         "https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord%2B%E6%B3%95%E5%BE%8B%2B1%2B%E6%B3%95%E5%BE%8B&searchView=text")
    #     print("@")
    #     while 1:
    #         start = time.clock()
    #         try:
    #             #  driver.find_elements_by_class_name("judgements")
    #             # result = driver.xpath('//(@class='judgements')')
    #             driver.find_element_by_xpath("//div[@class='judgements']/div[1]/div[2]/h3/a").click()
    #             time.sleep(9)
    #             print('已定位到元素')
    #             end = time.process_time()
    #             break
    #         except:
    #             print("还未定位到元素!")
    #     print('定位耗费时间：' + str(end - start))
