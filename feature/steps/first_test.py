from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get("http://ya.ru")


#ввести текст
@then("enter text in search field '{text}'")

def step(context, text):
    context.browser.find_element(By.NAME, 'text').send_keys('World')
    #context.browser.find_element(By.NAME, 'text').send_keys(Keys.ENTER)

#Теперь нажмем на кнопку "Найти"
#@then("push button with text '{text}'")
#def step(context, text):
#    WebDriverWait(context.browser, 120).until(
#        EC.element_to_be_clickable((By.XPATH, '//button'))
#    )
 #   context.browser.find_element(By.NAME, 'text').send_keys(' ')
  #  context.browser.find_element(By.NAME, 'text').send_keys(Keys.ENTER)

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(), "%s")]' % text))
    )
    assert context.browser.find_element(By.XPATH,'//*[contains(), "%s")]' % text)
        
    context.browser.quit()
