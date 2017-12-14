import urllib.request
from selenium import webdriver
import time
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#创建浏览器
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')
browser = webdriver.PhantomJS(desired_capabilities=dcap)
#加载网页
#访问动漫网页
browser.get('http://ac.qq.com/ComicView/index/id/547921/cid/1')
#截图
a = browser.get_screenshot_as_file('D:/可删/test.jpg')
#即用“鼠标触发”20个1280（1页）
for i in range(20):
  js = 'window.scrollTo('+str(i*1280)+','+str((i+1)*1280)+')'
  browser.execute_script(js)
  time.sleep(1)
#将当前URL页面源码写入'D:/可删/dongman.html'文件中
print(browser.current_url)
data = browser.page_source
fh = open('D:/可删/dongman.html','w',encoding='utf-8')
fh.write(data)
fh.close()
browser.quit()

#提取加载的网页上的图片
pat = '<img src="(http://ac.tc.qq.com/store_file_download.buid=.*?name=.*?).jpg"'
allid = re.compile(pat).findall(data)
for i in range(0,len(allid)):
  thisurl = allid[i]
  thisurl2 = thisurl.replace('amp;','')+'.jpg'
  print(thisurl2)
  localpath = 'D:/可删/'+str(i)+'.jpg'
  urllib.request.urlretrieve(thisurl2,filename=localpath)
