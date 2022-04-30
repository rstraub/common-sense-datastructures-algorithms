from datastructures_algorithms.chapter_9_stacks_queues.queue import Queue


class TestQueue:
    def test_read_should_return_none_given_no_elements(self):
        queue = Queue()

        assert queue.read() is None

    def test_enqueue_should_add_element_to_end(self):
        queue = Queue()

        queue.enqueue("henk")
        queue.enqueue("jan")

        assert queue.read() == "henk"

    def test_dequeue_should_remove_front_element(self):
        queue = Queue()

        queue.enqueue("henk")
        queue.enqueue("jan")

        assert queue.dequeue() == "henk"
        assert queue.read() == "jan"

    def test_dequeue_should_return_non_given_empty_queue(self):
        queue = Queue()

        assert queue.dequeue() is None

    def test_exercise_3(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.read() == 3
