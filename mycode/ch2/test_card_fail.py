from cards import Card

def test_equality_fail():
    c1 = Card("Something 1", "Justin")
    c2 = Card("Something 2", "Brian")
    assert c1 == c2

if __name__ == '__main__':
    c1 = Card("Something 1", "Justin")
    c2 = Card("Something 2", "Brian")
    assert c1 == c2
