"""Test for the appeaser strategy."""

import axelrod

from .test_player import TestPlayer

C, D = 'C', 'D'


class TestAppeaser(TestPlayer):

    name = "Appeaser"
    player = axelrod.Appeaser
    expected_behaviour = {
        'memory_depth': float('inf'),  # Depends on internal memory.
        'stochastic': False,
        'inspects_opponent_source': False,
        'manipulates_opponent_source': False,
        'manipulates_opponent_state': False
    }

    def test_strategy(self):
        """Starts by cooperating."""
        self.first_play_test(C)

    def test_effect_of_strategy(self):
        P1 = axelrod.Appeaser()
        P2 = axelrod.Cooperator()
        self.assertEqual(P1.strategy(P2), C)

        self.responses_test([C], [C], [C, C, C])
        self.responses_test([C, D, C, D], [C, C, D], [D])
        self.responses_test([C, D, C, D, C], [C, C, D, D], [C])
        self.responses_test([C, D, C, D, C, D], [C, C, D, D, D], [D])

