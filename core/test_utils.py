from unittest import TestCase

from core.utils import get_frequency_counts


class UtilsTestCase(TestCase):
    def test_get_frequency_counts(self):
        self.assertEqual(
            {"a": 2, "b": 2, "d": 2, "e": 1},
            get_frequency_counts(["a", "a", "b", "d", "d", "b", "e"]),
        )

        self.assertEqual({}, get_frequency_counts([]))

        self.assertEqual(
            {1: 2, 2: 5, 33: 1, 4: 1, 100: 1},
            get_frequency_counts([1, 2, 33, 4, 2, 2, 2, 2, 1, 100]),
        )
