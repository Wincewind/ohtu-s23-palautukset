class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class HasFewerThan(HasAtLeast):
    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        if not self._matcher.test(player):
            return True
        return False

#Tämän All tarkoitus jäi hieman epäselväksi.
class All(And):
    def test(self, player=None):
        return True
    
class Or(And):
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False