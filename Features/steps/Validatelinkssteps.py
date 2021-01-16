from behave import *
from selenium import webdriver
import time

@given('start chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/rajashree.devi/Downloads/chromedriver.exe")
    
@when('open GE homepage')
def openhomepage(context):
    context.driver.get("https://www.growthengineering.co.uk/")
    context.driver.maximize_window()

@then('click Our Products link')
def Productslink(context):
    e = context.driver.find_element_by_link_text("Our Products")
    e.send_keys("")
    e.click()
    time.sleep(5)
    e.click()

@then('verify title')
def verify_title(context):
    Actual = context.driver.title
    Expected = "The #1 Learning Management System for Employee Engagement"
    if (Actual == Expected):
        print("Test Passed!")
    else:
        print("Test Failed")

@then('click Our Approach link')
def Productslink(context):
    e = context.driver.find_element_by_link_text("Our Approach")
    e.send_keys("")
    e.click()
    time.sleep(5)
    e.click()


@then('verify page title')
def verify_title(context):
    Actual = context.driver.title
    Expected = "Brain Science - Growth Engineering"
    if (Actual == Expected):
        print("Test Passed!")
    else:
        print("Test Failed")


@then('click Resources link')
def Productslink(context):
    e = context.driver.find_element_by_link_text("Resources")
    e.send_keys("")
    e.click()
    time.sleep(5)
    e.click()

@then('verify ptitle')
def verify_title(context):
    Actual = context.driver.title
    Expected = "Resources | White Papers, Tip Sheets & Infographics - Growth Engineering"
    if (Actual == Expected):
        print("Test Passed!")
    else:
        print("Test Failed")


@then('click About Us link')
def Productslink(context):
    e = context.driver.find_element_by_link_text("About Us")
    e.send_keys("")
    e.click()
    time.sleep(5)
    e.click()

@then('verify titlep')
def verify_title(context):
    Actual = context.driver.title
    Expected = "About Us | Online Learning Superheroes - Growth Engineering"
    if (Actual == Expected):
        print("Test Passed!")
    else:
        print("Test Failed")


@then('click contact link')
def Productslink(context):
    e = context.driver.find_element_by_xpath("//*[@id='contact-button']")
    e.click()
    time.sleep(5)

@then('verify title of page')
def verify_title(context):
    Actual = context.driver.title
    Expected = "Get in Touch | Growth Engineering - The Learning Engagement Experts"
    if (Actual == Expected):
        print("Test Passed!")
    else:
        print("Test Failed")




