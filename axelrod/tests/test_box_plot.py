import unittest
import numpy
import axelrod


class TestBoxPlot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        players = ('Player1', 'Player2', 'Player3')
        results = [
            [[0, 0], [10, 10], [21, 21]],
            [[10, 8], [0, 0], [16, 20]],
            [[16, 16], [16, 16], [0, 0]]]
        cls.test_result_set = axelrod.ResultSet(players, 5, 2)
        cls.test_result_set.results = results
        cls.test_result_set.init_output()

        cls.expected_dataset = [[2, 2], [3, 3], [3, 3]]
        cls.expected_xticks = ([1, 2, 3, 4], ['Player2', 'Player1', 'Player3'])
        cls.expected_title = 'Mean score per stage game over 5 rounds repeated 2 times (3 strategies)'

    def test_init(self):
        bp = axelrod.BoxPlot(self.test_result_set)
        self.assertEquals(bp.result_set, self.test_result_set)

    def test_dataset(self):
        bp = axelrod.BoxPlot(self.test_result_set)
        self.assertTrue(numpy.allclose(bp.dataset(), self.expected_dataset))
        # self.assertEqual(bp.dataset(), self.expected_dataset)

    def test_xticks(self):
        bp = axelrod.BoxPlot(self.test_result_set)
        self.assertEquals(bp.xticks(), self.expected_xticks)

    def test_title(self):
        bp = axelrod.BoxPlot(self.test_result_set)
        self.assertEquals(bp.title(), self.expected_title)

if __name__ == '__main__':
    unittest.main()
