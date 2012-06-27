#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *
from koans.about_dice_project import DiceSet
from koans.about_scoring_project import score

class Player:

    def __init__(self, name):
        self.name = name

class Game:

    def __init__(self, *players):
        self.players = players
        self.dice = DiceSet()
        self._winner = None

    def play_round(self):
        round_scores = list()
        for player in self.players:
            self.dice.roll(5)
            rolled_score = score(self.dice.values)
            round_scores.append(rolled_score)
        return round_scores

    @property
    def winner(self):
        return self._winner

class AboutExtraCredit(Koan):

    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py

    def test_player_has_name(self):
        p = Player("Pat")
        self.assertEqual(p.name, "Pat")

    def test_game_has_players(self):
        g = Game(Player("Pat"), Player("Patricia"))
        self.assertEqual(2, len(g.players))

    def test_game_play_round_returns_scores(self):
        g = Game(Player("Pat"), Player("Patricia"))
        scores = g.play_round()
        print(scores)
        self.assertIsInstance(scores, list)
        self.assertIsInstance(scores[0], int)

    def test_game_play_round_scores_vary(self):
        g = Game(Player("Pat"), Player("Patricia"))
        all_scores = list()
        for i in range(10):
            all_scores.append(g.play_round())

        unique_pat_scores = set([scores[0] for scores in all_scores])
        self.assertGreater(len(unique_pat_scores), 1)

    def test_game_at_start_has_no_winner(self):
        game = Game(Player("Pat"), Player("Patricia"))
        self.assertIsNone(game.winner)


