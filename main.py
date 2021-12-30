import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_element(dr, el):
    return WebDriverWait(dr, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, el))
    )


def click_element_by_text(dr, el):
    el = "//*[text()='" + el + "']"
    elem = WebDriverWait(dr, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, el))
    )
    dr.execute_script("arguments[0].click();", elem)


def main():
    f = open("CONFIG.txt", "r")
    cr = []
    for item in f:
        cr.append(item.removesuffix('\n'))
    USERNAME = cr[0]
    PASSWORD = cr[1]
    TARGET = cr[2]
    MESSAGE = cr[3]
    driver = webdriver.Firefox()
    driver.get("http://www.instagram.com")
    assert "Instagram" in driver.title

    # click not now
    elem = get_element(driver, 'button.aOOlW:nth-child(2)')
    elem.click()

    # insert username
    elem = get_element(driver, 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    elem.send_keys(USERNAME)

    # insert password
    elem = get_element(driver, 'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    elem.send_keys(PASSWORD)

    # press login
    click_element_by_text(driver, 'Log In')

    # not now notifications
    click_element_by_text(driver, 'Not Now')

    # get page for target
    driver.get('http://www.instagram.com/' + TARGET)

    click_element_by_text(driver, "Message")

    # not now notifications
    click_element_by_text(driver, 'Not Now')

    elem = get_element(driver, '.ItkAi > textarea:nth-child(1)')
    elem.send_keys(MESSAGE)

    click_element_by_text(driver, 'Send')

    driver.close()


if __name__ == '__main__':
    main()
