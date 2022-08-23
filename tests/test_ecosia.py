from selene import have
from selene.support.shared import browser


def test_search():
    browser.open('https://www.ecosia.org/')

    browser.element('[name=q]').type('yashaka selene').press_enter()

    browser.all('.result__link').first.click()

    browser.all('[href="/yashaka/selene"]').should(have.size(3))






