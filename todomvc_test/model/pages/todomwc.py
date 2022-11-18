from selene import have, command
from selene.support.shared import browser


class TodoMvc:
    def __init__(self):
        self.collection = browser.all('#todo-list>li')
        self.browser = browser

    def visit(self):
        self.browser.open('http://todomvc4tasj.herokuapp.com/') \
            .should(have.js_returned(
            True,
            'return ($._data($("#clear-completed").get(0), "events")'
            '.hasOwnProperty("click") && '
            '(Object.keys(require.s.contexts._.defined).length === 39))'))
        return self

    def given_opened(self, *todos: str):
        self.visit()
        self.add(*todos)
        return self

    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').set_value(todo).press_enter()
        return self

    def list_should_be(self, *todos):
        self.collection.should(have.exact_texts(*todos))
        return self

    def list_should_be_empty(self):
        self.collection.should(have.size(0))
        return self

    def start_editing(self, todo, new_text):
        self.collection.element_by(have.exact_text(todo)).double_click()
        return browser.element('.editing').element('.edit') \
            .perform(command.js.set_value(new_text))

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def delete(self, text):
        self.collection.element_by(have.text(text)).hover() \
            .element('.destroy').click()
        return self

    def cancel_editing(self, todo, new_text):
        self.start_editing(todo, new_text).press_escape()
        return self

    def toggle(self, todo):
        self.collection.element_by(have.text(todo)) \
            .element('.toggle').click()
        return self

    def toggle_all(self):
        self.browser.element('#toggle-all').click()
        return self

    def should_be_completed(self, *todos: str):
        self.collection.filtered_by(have.css_class('completed')) \
            .should(have.exact_texts(*todos))
        return self

    def should_be_active(self, *todos: str):
        self.collection.filtered_by(have.css_class('active')) \
            .should(have.exact_texts(*todos))
        return self

    def clear_completed(self):
        self.browser.element('#clear-completed').click()
        return self

    def should_have_items_left(self, amount):
        self.browser.element('#todo-count>strong') \
            .should(have.exact_texts(str(amount)))
        return self
