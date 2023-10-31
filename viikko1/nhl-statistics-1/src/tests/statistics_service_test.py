import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player_found(self):
        stub_semenko = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(str(self.stats.search('Semenko')),str(stub_semenko))

    def test_search_player_not_found(self):
        self.assertEqual(self.stats.search('Wincewind'), None)

    def test_team(self):
        team = self.stats.team('EDM')
        self.assertEqual(len([p for p in team if p.team == 'EDM']), 3)
    
    def test_top_points(self):
        self.assertEqual(self.stats.top(1,SortBy.POINTS)[0].name, 'Gretzky')

    def test_top_goals(self):
        self.assertEqual(self.stats.top(1,SortBy.GOALS)[0].name, 'Lemieux')
    
    def test_top_assists(self):
        self.assertEqual(self.stats.top(1,SortBy.ASSISTS)[0].name, 'Gretzky')