from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/lior/Downloads/chromedriver_mac64/chromedriver")


def test_scores_service():
    driver.get('http://127.0.0.1:8777/')
    score_element = int(driver.find_element(By.ID, "score").text)
    if 1000 >= score_element >= 1:
        return True
    else:
        return False


def main_function():
    test = test_scores_service()
    if test:
        return 0
    else:
        return -1


main_function()
