"""
Recommended test structure pattern
    Arrange -> Act -> Assert
    OR
    Given -> When -> Then
"""
from cards import Card


def test_to_dict():
    # Given a card with a know value
    c1 = Card("something", "justin", "todo", 1)
    # When we call to_dict()
    c2 = c1.to_dict()
    # Then we get the expected dictionary
    c2_expected = {"summary": "something",
                   "owner": "justin",
                   "state": "todo",
                   "id": 1
                   }
    assert c2 == c2_expected
