class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.games = dict['games']
        self.points = self.goals+self.assists

    def __str__(self):
        return f"{self.name:24}{self.team}  {self.goals:3} + {self.assists} = {self.points}"
