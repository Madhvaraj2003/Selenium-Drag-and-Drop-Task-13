import pytest 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# pytest fixture to set up and tear down the webdriver for each test
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    yield driver
    driver.quit()

# Positive test case:
# Verfies that the white box (draggable) can be successfully dragged And dropped in to yellow box     
def test_drag_and_drop_positive(driver):
# Switching to the iframe where drag and drop elements are located
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,".demo-frame"))
# Identifying the source (draggable) and target (droppable) elements    
    source = driver.find_element(By.ID,"draggable")
    target = driver.find_element(By.ID,"droppable")
    action = ActionChains(driver)
# Performing the drag and drop operation 
    action.drag_and_drop(source, target).perform()
    time.sleep(2)
# Assertion to confirm that drop was successsful
    assert "Dropped" in target.text

# Negative test case:
# Ensures the test fails as expected while we are trying to interact with incoorect elements     
def test_drag_and_drop_negative(driver):
# Trying to switch to an iframe with indivual selector     
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,".demo-frame"))
    source = driver.find_element(By.ID,"draggable")
    target = driver.find_element(By.ID,"droppable")
    action = ActionChains(driver)
# Tries to drag and drop but fails as expected    
    action.click_and_hold(source).move_by_offset(300, 0).release().perform()
    time.sleep(3)
# using exception handling to get desired outcome the negative test case
    try: 
# Assert returns the below message if condition became false        
        assert "Dropped" in target.text, "element was NOT dropped correctly."
    except AssertionError as e:
        print("Negative test case passed: Drop did not happen as expected.")
        raise e 
# Quits the browser    
    driver.quit()
    
