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
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[1]/div[2]/div/div/div[3]/div/ul/li[4]/a/i').click()
time.sleep(5)
#driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[1]/div[2]/div/div/div[3]/div/ul/li[4]/div/form/fieldset/a[2]').click()

#driver.implicitly_wait(20)
#	mail = driver.find_element(By.XPATH,'//*[@id="email-login-storefront"]')
mail = driver.find_element(By.XPATH,'//*[@id="email-login-checkout"]')
#mail = driver.find_element(By.ID,'90f81aff-7635-44c4-886a-93b4ad81d380')
#mail = driver.find_element(By.NAME,"emailAddress")
#mail = driver.find_element_by_css_selector('#\39 0f81aff-7635-44c4-886a-93b4ad81d380') 
mail.clear()##
time.sleep(2)#dps de ecuenta
mail.send_keys('kofiy99717@duetube.com')
time.sleep(10)

"""confirmar_mail = driver.find_element(By.XPATH,'//*[@id="repeat-new-email"]')
confirmar_mail.clear()##
time.sleep(2)#dps de ecuenta
confirmar_mail.send_keys('nixoc35885@bunlets.com')"""

#	pwd = driver.find_element(By.XPATH,'//*[@id="password-login-storefront"]')
pwd = driver.find_element(By.XPATH,'//*[@id="password-login-checkout"]')
pwd.clear()
time.sleep(1)#dps de pwd
#pwd.send_keys('testeO1234')
pwd.send_keys('testeO1234')
time.sleep(10)

"""conf_pwd = driver.find_element(By.XPATH,'//*[@id="repeat-new-password"]')
conf_pwd.clear()##
time.sleep(1)#dps de nombre
conf_pwd.send_keys('testeO1234')"""


#driver.find_element(By.XPATH,'//*[@id="chooseaccountbutton-login-checkout-flyout"]').click()
driver.find_element(By.XPATH,'//*[@id="chooseaccountbutton-login-checkout"]').click()
time.sleep(15)
"""driver.find_element(By.XPATH,'//*[@id="legal-two-newsletter-checkout"]').click()
time.sleep(8)
driver.find_element(By.XPATH,'//*[@id="rp_create_account"]').click()
time.sleep(8)"""

"""driver.get("https://www.nike.com/es/")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/aside/div/div/div/div[1]/button').click()



driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/button').click()
time.sleep(1)

#driver.find_element(By.NAME,'/html/body/div[2]/div[2]/div[4]/div/div/div/div/div[2]/a').click()
#time.sleep(5)

#driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/aside/div/div/div/div[2]/button').click()
#time.sleep(2)

#driver.find_element(By.XPATH,'//*[@id="GeomismatchLanguageOptions"]/li[2]/button').click()
#time.sleep(5)

#driver.implicitly_wait(20)
#mail = driver.find_element(By.XPATH,'//*[@id="90f81aff-7635-44c4-886a-93b4ad81d380"]')
#mail = driver.find_element(By.ID,'90f81aff-7635-44c4-886a-93b4ad81d380')
mail = driver.find_element(By.NAME,"emailAddress")
#mail = driver.find_element_by_css_selector('#\39 0f81aff-7635-44c4-886a-93b4ad81d380') 
mail.clear()##
time.sleep(3)#dps de ecuenta
mail.send_keys('enrique99.acosta@gmail.com')

pwd = driver.find_element(By.NAME,"password")
pwd.clear()
time.sleep(3)#dps de pwd
pwd.send_keys('Kike.pulento99')
time.sleep(3)
driver.find_element_by_xpath('//input[@value="INICIAR SESIÓN"]').submit()
time.sleep(8)"""

driver.close()