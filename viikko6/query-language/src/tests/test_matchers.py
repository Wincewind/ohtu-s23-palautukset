import unittest
from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class TestMatchers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        cls.stats = Statistics(reader)

    def test_Not_and_HaveFewer(self):
        matcher_one = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
        )
    
        matcher_two = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
        )
        
        for i,_ in enumerate(self.stats.matches(matcher_one)):
            print(str(self.stats.matches(matcher_one)[i]))
            self.assertEqual(str(self.stats.matches(matcher_one)[i]),
                             str(self.stats.matches(matcher_two)[i]))
            
    def test_All(self):
        filtered_with_all = self.stats.matches(All())
        self.assertEqual(1058,len(filtered_with_all))
        print(len(filtered_with_all))

    def test_Or(self):
        correct_output = [
            'David Pastrnak       BOS          61 + 52 = 113',
            'Tage Thompson        BUF          47 + 47 = 94',
            'Nikita Kucherov      TBL          30 + 83 = 113',
            'Brayden Point        TBL          51 + 44 = 95',
            'Mikko Rantanen       COL          55 + 50 = 105',
            'Leon Draisaitl       EDM          52 + 76 = 128',
            'Connor McDavid       EDM          64 + 89 = 153',
            'Jason Robertson      DAL          46 + 63 = 109',
            'Erik Karlsson        SJS          25 + 76 = 101'

        ]
        matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
        )
        filter_with_or = self.stats.matches(matcher)
        for i,_ in enumerate(filter_with_or):
            self.assertEqual(str(filter_with_or[i]),correct_output[i])

    def test_combination(self):
        correct_output = [
            'Mika Zibanejad       NYR          39 + 52 = 91',
            'Artemi Panarin       NYR          29 + 63 = 92',
            'Adam Fox             NYR          12 + 60 = 72',
            'David Pastrnak       BOS          61 + 52 = 113',
            'Carter Verhaeghe     FLA          42 + 31 = 73',
            'Aleksander Barkov    FLA          23 + 55 = 78',
            'Brandon Montour      FLA          16 + 57 = 73',
            'Matthew Tkachuk      FLA          40 + 69 = 109'
        ]
        matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
        )
        filter_with_combo = self.stats.matches(matcher)
        for i,_ in enumerate(filter_with_combo):
            self.assertEqual(str(filter_with_combo[i]),correct_output[i])