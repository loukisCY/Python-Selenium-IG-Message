import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Firefox()
    driver.get("http://www.instagram.com")
    assert "Instagram" in driver.title
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)').click()
    driver.find_element(By.CSS_SELECTOR,
                        'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys(
        USERNAME)
    driver.find_element(By.CSS_SELECTOR,
                        'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys(
        PASSWORD)
    driver.find_element(By.CSS_SELECTOR, 'button.sqdOP:nth-child(1)').click()
    # elem = driver.find_element('name', 'q')
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()


if __name__ == '__main__':
    main()
