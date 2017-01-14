from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome('chromedriver')
    driver.get("https://cjh5414.github.io")
    assert driver.title == "jihun's Development blog •"
    driver.quit()
