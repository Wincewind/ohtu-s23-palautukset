from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players_of_nat = self.reader.players
        players_of_nat = filter(lambda player: player.nationality == nationality, players_of_nat)
        players_of_nat = sorted(players_of_nat, key=lambda player: player.points, reverse=True)
        return players_of_nat