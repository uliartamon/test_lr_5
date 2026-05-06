import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


def test_demoqa_text_box_smoke():
    os.makedirs("screenshots", exist_ok=True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://demoqa.com/text-box")

        wait.until(EC.visibility_of_element_located((By.ID, "userName"))).send_keys("Ivan Ivanov")
        driver.find_element(By.ID, "userEmail").send_keys("ivan@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Moscow, Test street, 1")
        driver.find_element(By.ID, "permanentAddress").send_keys("Saint Petersburg, Test avenue, 10")

        submit_button = driver.find_element(By.ID, "submit")

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        time.sleep(1)

        driver.save_screenshot("screenshots/before_submit.png")

        submit_button.click()

        output = wait.until(
            EC.visibility_of_element_located((By.ID, "output"))
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", output)
        time.sleep(1)

        assert output.is_displayed()
        assert "Ivan Ivanov" in driver.find_element(By.ID, "name").text
        assert "ivan@example.com" in driver.find_element(By.ID, "email").text

        driver.save_screenshot("screenshots/after_submit.png")

    finally:
        driver.quit()