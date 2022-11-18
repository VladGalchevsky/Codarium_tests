from todomvc_test.model import TodoMvc

todos = TodoMvc()


def test_common_todo_functionality():
    todos.visit()

    todos.add('a', 'b', 'c')
    todos.list_should_be('a', 'b', 'c')

    todos.edit('a', 'a edited')

    todos.delete('a edited')
    todos.list_should_be('b', 'c')

    todos.cancel_editing('c', 'to de canceled')

    todos.toggle('c')
    todos.clear_completed()
    todos.list_should_be('b')



