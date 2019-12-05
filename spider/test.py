from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#import pymongo
import time
from spider.utils.configwusong import *
#from xdaili import Xdaili
class Products(object):
    def __init__(self):
        """
        初始化
        """
        # 数据库配置
#        self.client = pymongo.MongoClient(MONGO_URL)
#        self.db = self.client[MONGO_DB]
#        self.collection = self.db[MONGO_COLLECTION]
        # 代理配置
#        self.auth = Xdaili().auth()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--start-maximized')
        self.chrome_options.add_argument('--headless')
        self.plugin_file = './utils/proxy_auth_plugin.zip'
        self.chrome_options.add_extension(self.plugin_file)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #    self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def spider(self,key):
     self.driver.get(URL)
     print("@")
     while 1:
            try:
                time.sleep(3)
                self.driver.find_element_by_class_name("login-btn").click()
                time.sleep(3)
                self.driver.find_element_by_xpath("//input[@id='username']").click()
                self.driver.find_element_by_xpath("//input[@id='username']").clear()
                self.driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
                self.driver.find_element_by_xpath("//input[@id='password']").click()
                self.driver.find_element_by_xpath("//input[@id='password']").clear()
                self.driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
                self.driver.find_element_by_class_name("submit").click()
                time.sleep(5)
                self.driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").click()
                self.driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").clear()
                self.driver.find_element_by_xpath("//input[@placeholder='输入“?”定位到当事人、律师、法官、法院、标题、法院观点']").send_keys(key)
                self.driver.find_element_by_class_name("search-box-btn").click()
                time.sleep(3)

                j =1
                for j in range(4):
                    element = self.driver.find_element_by_xpath("//button[@class='view-more ng-scope']")
                    element.click()
                    time.sleep(3)

                lit = self.driver.find_elements_by_class_name("judgement ng-scope")
                lis = self.driver.find_elements_by_xpath('//div[@class = "judgements"]/div[@class="judgement ng-scope"]')

                for i in range(len(lis)):
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
        try:
            if self.db[MONGO_COLLECTION].insert(result):
                print('存储到MONGODB成功', result)
        except Exception:
            print('存储到MONGODB失败', result)

    def main(self,keyword):
         self.spider(keyword)



# if __name__ == '__main__':
#     start=time.process_time()
#    # print('请输入关键词：')
#     str = input("请输入关键词：")
#     law_product = Products()
#     law_product.main(str)
#     end=time.process_time()
#     print('耗时：' + str(end - start))

