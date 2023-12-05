from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or

class QueryBuilder:
    def __init__(self, matchers=All):
        self._matchers = matchers

    def build(self):
        return self._matchers
    
    def playsIn(self, team):
        return QueryBuilder(And(self._matchers,PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matchers,HasAtLeast(value,attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matchers,HasFewerThan(value,attr)))
    
    def oneOf(self,matchersOne,matchersTwo):
        return QueryBuilder(Or(matchersOne,matchersTwo))