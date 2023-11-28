class TennisGame:
    SCORE_DESC = {0:'Love',1:'Fifteen',2:'Thirty',3:'Forty'}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        score_as_str = ""

        if self.player1_points == self.player2_points:
            score_as_str = self.__get_even_score()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            score_as_str = self.__get_advantaged_score()
        else:
            score_as_str = f'{self.SCORE_DESC[self.player1_points]}-{self.SCORE_DESC[self.player2_points]}'

        return score_as_str

    def __get_even_score(self):
        """Returns the even, or 'All' description of the score.

        Returns:
            str: description of the score.
        """
        if self.player1_points <= 2:
            return self.SCORE_DESC[self.player1_points]+'-All'
        return "Deuce"

    def __get_advantaged_score(self):
        """Returns the description of the game state, 
        when one player has either an advantage or has won.

        Returns:
            str: description of the score.
        """
        score_as_str = ""
        score_difference = self.player1_points - self. player2_points

        if score_difference == 1:
            score_as_str = "Advantage player1"
        elif score_difference == -1:
            score_as_str = "Advantage player2"
        elif score_difference >= 2:
            score_as_str = "Win for player1"
        else:
            score_as_str = "Win for player2"
        return score_as_str
