from datastructures_algorithms.stacks_queues import reverse


class TestStacksAndQueues:
    def test_reverse_string(self):
        assert reverse("hello") == "olleh"
