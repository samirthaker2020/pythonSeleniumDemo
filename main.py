from selenium import webdriver
path1 = "C:\\Users\\JOKERPC1\\PycharmProjects\\pythonSeleniumDemo\\Driver\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=path1)
driver.get("http://www.samirthaker.info")
driver.maximize_window()

#1. scroll down by page by pixcel
driver.execute_script("window.scrollBy(0,1500)","")