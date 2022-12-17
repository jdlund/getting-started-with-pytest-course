import pytest
from cards import Card

def test_equality_fail():
    c1 = Card("Something 1", "Justin")
    c2 = Card("Something 2", "Brian")
    if c1 != c2:
        pytest.fail("Card c1 and Card c2 are not equal!")

def test_equality_fail2():
    c1 = Card("Something 1", "Justin")
    c2 = Card("Something 2", "Brian")
    if c1 != c2:
        raise Exception("Card c1 and Card c2 are not equal!")