from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import allure


def test_example_1(login_page, page) -> None:
    login_page.navigate()
    login_page.expect_login_credentials_visible()

    login_page.type_username("locked_out_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
    attach_screenshot(page, "Screenshot test_exampe_1")



def test_example_2(page: Page, login_page_with_login) -> None:

    expect(page.locator("[data-test=\"login-credentials\"]")).to_be_visible()

    page.locator("[data-test=\"username\"]").press_sequentially("abcabc", delay=100)
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    attach_screenshot(page, "Screenshot test_exampe_2")


def attach_screenshot(page, name):
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
