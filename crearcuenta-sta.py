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
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div[2]/div/div[2]/div[1]/button[1]').click()
time.sleep(6)

nombre = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[1]/label/input')
nombre.clear()##
time.sleep(4)#dps de nombre
nombre.send_keys('Juan')
time.sleep(6)
apellido = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[2]/label/input')
apellido.clear()##
time.sleep(4)#dps de apellido
apellido.send_keys('Perez')
time.sleep(6)
mail = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/label/input')
mail.clear()##
time.sleep(2)#dps de email
mail.send_keys('posobe8016@roxoas.com')
time.sleep(6)

driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[5]/label/div/input').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[3]/button[2]').click()
time.sleep(4)



pwd = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[2]/div/div[1]/label/input')
pwd.clear()
time.sleep(2)#dps de pwd
pwd.send_keys('Muyseguro1')
time.sleep(6)

pwd1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/div/div[2]/div/div[2]/label/input')
pwd1.clear()
time.sleep(2)#dps de pwd
pwd1.send_keys('Muyseguro1')
time.sleep(6)

driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[3]/div/button[1]').click()
time.sleep(20)



driver.close()