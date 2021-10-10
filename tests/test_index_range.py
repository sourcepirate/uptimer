import unittest
from uptimer.memory import indexing_range


class TestDB(unittest.TestCase):
    """Tests for `uptimer` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_inrange_index(self):
        index_list = list(range(0, 100, 2))
        values = indexing_range(index_list, 3, 97)
        self.assertListEqual(values, list(range(4, 96, 2)))