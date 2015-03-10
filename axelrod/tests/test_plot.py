import unittest
import numpy
import axelrod

matplotlib_installed = True
try:
    import matplotlib.pyplot
except ImportError:
    matplotlib_installed = False


class TestPlot(unittest.TestCase):

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

        cls.expected_boxplot_dataset = [[2.6, 2.8], [3.1, 3.1], [3.2, 3.2]]
        cls.expected_boxplot_xticks_locations = [1, 2, 3, 4]
        cls.expected_boxplot_xticks_labels = ['Player2', 'Player1', 'Player3']
        cls.expected_boxplot_title = 'Mean score per stage game over 5 rounds repeated 2 times (3 strategies)'

    def test_init(self):
        bp = axelrod.Plot(self.test_result_set)
        self.assertEquals(bp.result_set, self.test_result_set)

    def test_boxplot_dataset(self):
        bp = axelrod.Plot(self.test_result_set)
        self.assertTrue(numpy.allclose(bp.boxplot_dataset(), self.expected_boxplot_dataset))

    def test_boxplot_xticks_locations(self):
        bp = axelrod.Plot(self.test_result_set)
        self.assertEquals(bp.boxplot_xticks_locations(), self.expected_boxplot_xticks_locations)

    def test_boxplot_xticks_labels(self):
        bp = axelrod.Plot(self.test_result_set)
        self.assertEquals(bp.boxplot_xticks_labels(), self.expected_boxplot_xticks_labels)

    def test_boxplot_title(self):
        bp = axelrod.Plot(self.test_result_set)
        self.assertEquals(bp.boxplot_title(), self.expected_boxplot_title)

    def test_boxplot(self):
        if matplotlib_installed:
            bp = axelrod.Plot(self.test_result_set)
            self.assertIsInstance(bp.boxplot(), matplotlib.pyplot.Figure)
        else:
            self.skipTest('matplotlib not installed')


if __name__ == '__main__':
    unittest.main()
