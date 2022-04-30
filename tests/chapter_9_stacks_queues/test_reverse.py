from datastructures_algorithms.chapter_9_stacks_queues.stacks_queues import reverse


class TestReverse:
    def test_reverse_string(self):
        assert reverse("hello") == "olleh"
