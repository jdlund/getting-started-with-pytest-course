from cards import Card

def test_field_access():
    c = Card(summary="Something", owner="Justin", state="todo", id=1)
    assert c.summary == "Something"
    assert c.owner == "Justin"
    assert c.state == "todo"
    assert c.id == 1

def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None

