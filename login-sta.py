import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver_path = "./chromedriver_linux64/chromedriver"

#if __name__ == "__main__":
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
#options.add_argument('--disable-extensions')

options.binary_location= "/opt/google/chrome/google-chrome"
#driver = webdriver.Chrome(driver_path)
chrome_driver_binary = "./chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

#driver.set_window_position(1024,1024,windowHandle='current')
driver.set_window_position(1000,0)
driver.maximize_window()
time.sleep(4)

#Inicializamos el navegador
driver.get("https://www.santaisabel.cl/")


#time.sleep(1)
#driver.find_element(By.ID, "login-account-link").click()

time.sleep(4)
#driver.find_element(By.XPATH,'/html/body/app-root/home-index/app-header-container/app-header/div/div/div/div[2]/div/div/a[1]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div[2]/div/div[2]/div[1]/button[2]').click()
time.sleep(6)

mail = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[1]/label/input')
mail.clear()##
time.sleep(2)#dps de email
mail.send_keys('posobe8016@roxoas.com')
time.sleep(4)

pwd = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[2]/label/input')
pwd.clear()
time.sleep(2)#dps de pwd
pwd.send_keys('Muyseguro1')
time.sleep(6)


driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[3]/button[2]').click()

time.sleep(8)

driver.close()