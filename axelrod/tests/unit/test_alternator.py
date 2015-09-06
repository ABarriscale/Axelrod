"""Test for the alternator strategy."""

import axelrod

from .test_player import TestPlayer

C, D = 'C', 'D'


class TestAlternator(TestPlayer):

    name = "Alternator"
    player = axelrod.Alternator
    behaviour = {
        'stochastic': False,
        'memory_depth': 1,
        'inspects_opponent_source': False,
        'updates_opponent_source': False
    }

    def test_strategy(self):
        """Starts by cooperating."""
        self.first_play_test(C)

    def test_effect_of_strategy(self):
        """Simply does the opposite to what the strategy did last time."""
        self.markov_test([D, D, C, C])
        for i in range(10):
            self.responses_test([], [], [C, D] * i)
        self.responses_test([C, D, D, D], [C, C, C, C], [C])
        self.responses_test([C, C, D, D, C], [C, D, C, C, C], [D])
