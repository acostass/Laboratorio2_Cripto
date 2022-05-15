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
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/section[1]/div[2]/div/div/div[3]/div/ul/li[4]/div/form/fieldset/a[2]').click()

#driver.implicitly_wait(20)
mail = driver.find_element(By.XPATH,'//*[@id="enter-new-email"]')
#mail = driver.find_element(By.ID,'90f81aff-7635-44c4-886a-93b4ad81d380')
#mail = driver.find_element(By.NAME,"emailAddress")
#mail = driver.find_element_by_css_selector('#\39 0f81aff-7635-44c4-886a-93b4ad81d380') 
mail.clear()##
time.sleep(2)#dps de ecuenta
mail.send_keys('kofiy99717@duetube.com')

confirmar_mail = driver.find_element(By.XPATH,'//*[@id="repeat-new-email"]')
confirmar_mail.clear()##
time.sleep(2)#dps de ecuenta
confirmar_mail.send_keys('kofiy99717@duetube.com')

pwd = driver.find_element(By.XPATH,'//*[@id="enter-new-password"]')
pwd.clear()
time.sleep(1)#dps de pwd
pwd.send_keys('testeO1234')

conf_pwd = driver.find_element(By.XPATH,'//*[@id="repeat-new-password"]')
conf_pwd.clear()##
time.sleep(1)#dps de nombre
conf_pwd.send_keys('testeO1234')



driver.find_element(By.XPATH,'//*[@id="legal-one-newsletter-checkout"]').click()
time.sleep(8)
driver.find_element(By.XPATH,'//*[@id="legal-two-newsletter-checkout"]').click()
time.sleep(8)
driver.find_element(By.XPATH,'//*[@id="rp_create_account"]').click()
time.sleep(15)

"""apellido = driver.find_element(By.NAME,"lastName")
apellido.clear()##
time.sleep(1)#dps de apellido
apellido.send_keys('Perez Perez')

fecha = driver.find_element(By.NAME,"dateOfBirth")
fecha.clear()##
time.sleep(1)#dps de fecha
fecha.send_keys('16081999')

wait = WebDriverWait(driver, 10)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@data-componentname='gender']//li//span[contains(.,'Hombre')]//preceding::input[1]"))).click()
#driver.find_element(By.NAME,'//*[@id="c9ef684f-c671-4431-8245-6f27e7d99c02"]/input').click() 
#time.sleep(1)
maleBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@data-componentname='gender']//span[text()='Hombre']/preceding::input[@type='button']")))
driver.execute_script("arguments[0].click();", maleBtn)

#driver.find_element(By.NAME,'//*[@id="fbece55f-acd2-4166-ba1d-cc78dcfd4fbf"]').click()

time.sleep(8)

#driver.find_element(By.XPATH('//input[@value="ÚNETE A NOSOTROS"]'));
driver.find_element_by_xpath('//input[@value="ÚNETE A NOSOTROS"]').click()
time.sleep(300)"""

driver.close()