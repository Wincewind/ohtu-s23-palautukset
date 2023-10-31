from enum import Enum
from player_reader import PlayerReader

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_by_func(player, sortby: SortBy):
    if sortby.value == 1:
        return player.points
    elif sortby.value == 2:
        return player.goals
    else:
        return player.assists


class StatisticsService:
    def __init__(self, reader: PlayerReader):
        reader = reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sortby: SortBy):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda p: sort_by_func(p, sortby)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
