from test import Products
import time
start = time.process_time()
# print('请输入关键词：')
str = input("请输入关键词：")
law_product = Products()
law_product.main(str)
end = time.process_time()
print('耗时：' + str(end - start))