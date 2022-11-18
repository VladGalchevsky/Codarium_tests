from todomvc_test.model import todos


def test_add():
    todos.given_opened()

    # When nothing
    todos.add()
    todos.list_should_be_empty()

    # When
    todos.add('a')
    todos.list_should_be('a')
    # todos.should_have_items_left(1)

    # When
    todos.add('b', 'c')
    todos.list_should_be('a', 'b', 'c')
    # todos.should_have_items_left(3)


def test_edit():
    todos.given_opened('a', 'b', 'c')

    todos.edit('b', 'b edited')

    todos.list_should_be('a', 'b edited', 'c')
    # todos.should_have_items_left(3)


def test_cancel_editing():
    todos.given_opened('a', 'b', 'c')

    todos.cancel_editing('b', 'to be canceled')

    todos.list_should_be('a', 'b', 'c')
    # todos.should_have_items_left(3)


def test_delete_by_edit_to_blank():
    todos.given_opened('a', 'b', 'c')

    todos.edit('b', '')

    todos.list_should_be('a', 'c')
    # todos.should_have_items_left(2)


def test_complete():
    todos.given_opened('a', 'b', 'c')

    todos.toggle('b')

    todos.should_be_completed('b')
    todos.should_be_active('a', 'c')
    # todos.should_have_items_left(2)


def test_clear_completed():
    todos.given_opened('a', 'b', 'c')
    todos.toggle('b')

    todos.clear_completed()

    todos.list_should_be('a', 'c')
    # todos.should_have_items_left(2)


def test_complete_all():
    todos.given_opened('a', 'b', 'c')
    todos.toggle('b')

    todos.toggle_all()

    todos.should_be_active()
    todos.should_be_completed('a', 'b', 'c')


def test_active_all():
    todos.given_opened('a', 'b', 'c')
    todos.toggle_all()

    todos.toggle_all()

    todos.should_be_active('a', 'b', 'c')
    # todos.should_have_items_left(3)


def test_delete():
    todos.given_opened('a', 'b', 'c')

    todos.delete('b')

    todos.list_should_be('a', 'c')
    # todos.should_have_items_left(2)
