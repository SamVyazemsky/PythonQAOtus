import pytest
from selenium import webdriver
from pages.adminpage import AdminLoginPage


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def admin_page(browser):
    page = AdminLoginPage(browser)
    page.go_to()
    return page
