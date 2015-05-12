"""Tests for the main tournament class."""

import unittest
import axelrod
import logging


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.game = axelrod.Game()
        cls.players = [axelrod.Defector(), axelrod.Defector(), axelrod.Defector()]
        cls.test_name = 'test'

    def test_init(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            noise=0.2)
        self.assertEqual([str(s) for s in tournament.players], ['Defector', 'Defector', 'Defector'])
        self.assertEqual(tournament.game.score(('C', 'C')), (3, 3))
        self.assertEqual(tournament.turns, 200)
        self.assertEqual(tournament.repetitions, 10)
        self.assertEqual(tournament.name, 'test')
        self.assertEqual(tournament._processes, 4)
        self.assertFalse(tournament.prebuilt_cache)
        self.assertIsInstance(tournament._logger, logging.Logger)
        self.assertIsInstance(tournament.result_set, axelrod.ResultSet)
        self.assertEqual(tournament.deterministic_cache, {})
        self.assertEqual(tournament.noise, 0.2)
        anonymous_tournament = axelrod.Tournament(players=self.players)
        self.assertEqual(anonymous_tournament.name, 'axelrod')

    def test_build_cache_required(self):
        # Noisy, no prebuilt cache, deterministic cache empty
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            noise=0.2,
            prebuilt_cache=False)
        self.assertFalse(tournament.build_cache_required)

        # Noisy, with prebuilt cache, deterministic cache empty
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            noise=0.2,
            prebuilt_cache=True)
        self.assertFalse(tournament.build_cache_required)

        # Not noisy, with prebuilt cache, deterministic cache has content
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            prebuilt_cache=True)
        tournament.deterministic_cache = {'test': 100}
        self.assertFalse(tournament.build_cache_required)

        # Not noisy, no prebuilt cache, deterministic cache has content
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            prebuilt_cache=False)
        tournament.deterministic_cache = {'test': 100}
        self.assertTrue(tournament.build_cache_required)

        # Not noisy, with prebuilt cache, deterministic cache is empty
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            prebuilt_cache=True)
        self.assertTrue(tournament.build_cache_required)

        # Not noisy, no prebuilt cache, deterministic cache is empty
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            prebuilt_cache=False)
        self.assertTrue(tournament.build_cache_required)

    def test_serial_play(self):
        pass

    def test_parallel_play(self):
        pass


    def test_tournament(self):
        """Test tournament."""

        outcome = [('Cooperator', [1800, 1800, 1800, 1800, 1800]),
                   ('Defector', [1612, 1612, 1612, 1612, 1612]),
                   ('Go By Majority', [1999, 1999, 1999, 1999, 1999]),
                   ('Grudger', [1999, 1999, 1999, 1999, 1999]),
                   ('Tit For Tat', [1999, 1999, 1999, 1999, 1999])]

        outcome.sort()

        P1 = axelrod.Cooperator()
        P2 = axelrod.TitForTat()
        P3 = axelrod.Defector()
        P4 = axelrod.Grudger()
        P5 = axelrod.GoByMajority()
        tournament = axelrod.Tournament(name='test', players=[P1, P2, P3, P4, P5], game=self.game, turns=200, repetitions=5)
        names = [str(p) for p in tournament.players]
        results = tournament.play().results
        scores = [[sum([r[i] for ir,r in enumerate(res) if ir != ires]) for i in range(5)] for ires,res in enumerate(results)]
        self.assertEqual(sorted(zip(names, scores)), outcome)


if __name__ == '__main__':
    unittest.main()
