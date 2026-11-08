from playwright.sync_api import Page, expect

from pages.login_github_page import LoginPage
from utilities.config import TEST_PASSWORD_GITHUB,TEST_EMAIL_GITHUB


def test_sign_in_to_gmail(page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()

    #signInPage.sighInButton.click()  , more way
    signInPage.clickOnsighInButton()
    signInPage.waitForLoginPageLoad()

    assert TEST_EMAIL_GITHUB is not None
    assert TEST_PASSWORD_GITHUB is not None


    signInPage.emailFiled.fill(TEST_EMAIL_GITHUB)
    signInPage.passwordlFiled.fill(TEST_PASSWORD_GITHUB)
    page.pause()
    expect(signInPage.signInSubmitButton).to_be_visible()
 


