import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


### Setup ###
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('URL_TO_TEST')
    yield driver
    driver.quit()

def helper_function(browser, input_a, input_b, operation_id):
    browser.find_element(By.ID, "input_a").send_keys(input_a)
    browser.find_element(By.ID, operation_id).click()
    browser.find_element(By.ID, "input_b").send_keys(input_b)
    browser.find_element(By.ID, "calculate").click()
    return browser.find_element(By.ID, "result").text    
    

### Positive Tests ###
def test_addition(browser):
    '''Test case for the addition operator'''
    result = helper_function(browser,'1','2','addition')
    assert result == '3', "Addition test failed!"

def test_subtraction(browser):
    '''Test case for the subtraction operator'''
    result = helper_function(browser,5,3,'subtraction')
    assert result == '2', "Subtraction test failed!"

def test_multiplication(browser):
    '''Test case for the multiplication operator'''
    result = helper_function(browser,2,4,'multiplication')
    assert result == '8', "Multiplication test failed!"

def test_division(browser):
    '''Test case for the division operator'''
    result = helper_function(browser,6,3,'division')
    assert result == '2', "Division test failed!"

def test_decimal_numbers(browser):
    '''Test case for decimal numbers support'''
    result = helper_function(browser,1.2,3.1,'addition')
    assert result == '4.3', "Decimal test failed!"


### Edge cases ###
def test_long_positive_numbers(browser):
    '''Test case for long positive numbers'''
    result = helper_function(browser,999999999,2,'subtraction')
    assert result == "999999997", "Subtraction from large number test failed"

def test_long_negative_numbers(browser):
    '''Boundry Test for long negative numbers'''
    result = helper_function(browser,-5,2,'addition')
    assert result == "-3", "Negative numbers test failed"

def test_addition_by_zero(browser):
    '''Test case for addition by zero'''
    result = helper_function(browser,0,2,'addition')
    assert result == '2', "addition by zero failed"

def test_multiplication_by_zero(browser):
    '''Test case for multiplication by zero'''
    result = helper_function(browser,0,2,'multiplication')
    assert result == '0', "multiplication by zero failed"


### Negative Tests ###
def test_invalid_input(browser):
    '''Test case for invalid input in one of the input fields'''
    result = helper_function(browser,1,'asd','addition')
    assert result == "Invalid Input, input contains invalid characters"

def test_divison_by_zero(browser):
    '''Test case for division by zero'''
    result = helper_function(browser,1,0,'division')
    assert result == "Division by zero is not allowed"

def test_empty_input(browser):
    '''Test case for invalid input in one of the input fields'''
    result = helper_function(browser,1,'','addition')
    assert result == "Input B is empty"
