from selenium import webdriver
from selenium.webdriver import FirefoxOptions

def test_example():
    """
    First test
    """
    option = FirefoxOptions()
    wd = webdriver.Firefox(options=option)
    wd.get("https://otus.ru/")
    assert wd.title == 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    wd.quit()
