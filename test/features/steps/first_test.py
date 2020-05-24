from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@given('website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)

@then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()

@then("push button with num '{text}'")
def step(context, text):
    context.browser.find_element_by_id(text).click()
    
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    context.browser.quit()
    
@then("values element by id '{elem_id}' = '{value}'")
def step(context, elem_id, value):
    res = context.browser.find_element_by_id(elem_id).get_attribute("value")
    if res=="": res = "0"      
    assert (float(res)==float(value))
    context.browser.quit()