from selene import by, be, have
from selene.support.shared import browser


def test_search():
    browser.open('https://google.com/ncr')

    browser.element(by.name('q')).should(be.blank).type('python selene')\
        .press_enter()

    results = browser.all('#search .g')
    results.should(have.size_greater_than_or_equal(6))
    results.first.should(have.text('Concise API for Selenium'))
    results.first.element('.r>a').click()

    browser.should(have.title_containing('yashaka/selene'))