import unittest
from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query_builder import QueryBuilder

class TestQueryBuilder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        cls.stats = Statistics(reader)

    def test_playsIn_build(self):
        query = QueryBuilder()
        matcher = query.playsIn("NYR").build()
        filter_check = self.stats.matches(PlaysIn("NYR"))
        filtered = self.stats.matches(matcher)
        for i,_ in enumerate(filtered):
            print(filtered[i])
            self.assertEqual(str(filtered[i]),str(filter_check[i]))

    def test_multiple_matcher_build(self):
        correct_output = [
            'Barclay Goodrow      NYR          11 + 20 = 31',
            'Jimmy Vesey          NYR          11 + 14 = 25',
            'Adam Fox             NYR          12 + 60 = 72',
            'Kaapo Kakko          NYR          18 + 22 = 40',
            'Alexis Lafrenière    NYR          16 + 23 = 39'
        ]
        query = QueryBuilder()
        matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()
        filtered = self.stats.matches(matcher)
        for player in filtered:
            print(player)
        self.assertEqual(correct_output,[str(player) for player in filtered])

    def test_Or_matcher_build(self):
        correct_output = [
            'Nick Seeler          PHI          4  + 10 = 14',
            'Rasmus Ristolainen   PHI          3  + 17 = 20',
            'Cam York             PHI          2  + 18 = 20',
            'Tyson Barrie         EDM          13 + 42 = 55',
            'Zach Hyman           EDM          36 + 47 = 83',
            'Ryan Nugent-Hopkins  EDM          37 + 67 = 104',
            'Leon Draisaitl       EDM          52 + 76 = 128',
            'Connor McDavid       EDM          64 + 89 = 153'
        ]
        
        query = QueryBuilder()
        m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
        )

        m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )

        matcher = query.oneOf(m1, m2).build()
        filtered = self.stats.matches(matcher)
        self.assertEqual(correct_output,[str(player) for player in filtered])