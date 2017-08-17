from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')
browser = webdriver.PhantomJS(desired_capalilities=dcap)
browser.get('http://ac.qq.com/ComicView/index/id/518333/cid/1')
a = browser.get_screenshot_as_file('D:/学习资料/tencent_dongman/test.jpg')
for i in range(10):
  js = 'window.scrollTo('+str(i*1280)+','+str((i+1)*1280)+')'
  browser.execute_script(js)
  time.sleep(1)
print(browser.current_url)
data = browser.page_source
fh = open('D:/学习资料/tencent_dongman/dongman.html','w',encoding='utf-8')
fh.write(data)
fh.close()
browser.quit()
