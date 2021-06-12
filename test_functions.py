"""Test functions for all my functions. I was trying to use
monkeypatch to test my functions but I couldn't figure out
a way it since my functions have no parameters and don't 
return anything.
"""

from functions import start, easy, medium, hard, star, learn_more
    
def test_start():

    assert callable(start)

def test_easy():

    assert callable(easy)
    
def test_medium():

    assert callable(medium)

def test_hard():

    assert callable(hard)
    
def test_star():
    
    assert callable(star)
    assert isinstance(star(3), str)
    assert star(3) == ("🇺🇸🇺🇸🇺🇸")
                 
def test_learn_more():

    assert callable(learn_more)