import pytest


def test_success_login(admin_page):
    admin_page.login('demo', 'demo')
    assert admin_page.driver.title == 'Dashboard'


def test_negative_login(admin_page):
    admin_page.login('', '')
    admin_page.create_product('new')
    admin_page.logout()
    assert admin_page.driver.title != 'Dashboard'
