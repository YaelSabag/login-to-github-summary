from playwright.sync_api import Locator, Page


from pages.base_page import BasePage
from utilities import config
import re


class LoginPage(BasePage):
    PATH = config.GITHUB_URL


    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def sighInButton(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")

    @property
    def emailFiled(self) -> Locator:
        return self.page.get_by_role("textbox", name="Username or email address")
    
    @property
    def passwordlFiled(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")

    @property
    def signInSubmitButton(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in", exact=True)


    def clickOnsighInButton(self) -> Locator:
        self.sighInButton.click()

    def waitForLoginPageLoad(self) -> None:
        self.page.wait_for_url("**/login")