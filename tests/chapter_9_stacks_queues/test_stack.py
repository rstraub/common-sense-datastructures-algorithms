from datastructures_algorithms.chapter_9_stacks_queues.stack import Stack


class TestStack:
    def test_push_should_add_element_to_top(self):
        stack = Stack()

        stack.push("a")
        stack.push("l")

        assert stack.read() == "l"

    def test_pop_should_remove_and_return_top_element(self):
        stack = Stack()

        stack.push("a")
        stack.push("l")

        assert stack.pop() == "l"
        assert stack.read() == "a"

    def test_pop_should_return_none_given_empty_stack(self):
        stack = Stack()

        assert stack.pop() is None

    def test_read_should_return_none_given_empty_stack(self):
        stack = Stack()

        assert stack.read() is None

    def test_exercise_2(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)

        assert stack.pop() == 6
        assert stack.pop() == 5
