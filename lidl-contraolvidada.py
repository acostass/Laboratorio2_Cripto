import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "./chromedriver_linux64/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location= "/opt/google/chrome/google-chrome"
#driver = webdriver.Chrome(driver_path)
chrome_driver_binary = "./chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

driver.set_window_position(1000,0)
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(1)


#Inicializamos el navegador
driver.get("https://www.lidl.es/")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/dialog/div/div[1]/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[1]/div[2]/div/div/div[3]/div/ul/li[4]/a/i').click()
#time.sleep(5)
#driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[1]/div[2]/div/div/div[3]/div/ul/li[4]/div/form/fieldset/a[2]').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[1]/div[2]/div/div/div[3]/div/ul/li[4]/div/form/fieldset/a[1]').click()


mail = driver.find_element(By.XPATH,'//*[@id="email-remember-general-login"]')
mail.clear()##
time.sleep(1)#dps de email
mail.send_keys('kofiy99717@duetube.com')

time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[3]/div[2]/div/div[2]/div/form/fieldset/div[3]/button').click()
"""driver.get("https://www.nike.com/es/")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/aside/div/div/div/div[1]/button').click()



driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/button').click()
time.sleep(1)

#driver.find_element_by_class_name('nike-unite-component action-link forgotPassword').click()
driver.find_element_by_link_text('¿Has olvidado la contraseña?').click()
time.sleep(5)


mail = driver.find_element(By.NAME,"emailAddress")
#mail = driver.find_element_by_css_selector('#\39 0f81aff-7635-44c4-886a-93b4ad81d380') 
mail.clear()##
time.sleep(2)#dps de ecuenta
mail.send_keys('testeo.udp@gmail.com')

#pwd = driver.find_element(By.NAME,"password")
#pwd.clear()
#time.sleep(1)#dps de pwd
#pwd.send_keys('testeO1234')

driver.find_element_by_xpath('//input[@value="RESTABLECER"]').submit()"""
time.sleep(15)

driver.close()