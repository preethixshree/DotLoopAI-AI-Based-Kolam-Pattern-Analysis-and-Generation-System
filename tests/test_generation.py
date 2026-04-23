from modules.pattern_generation import generate_basic_kolam

def test_kolam():
    grid = generate_basic_kolam(5)
    assert grid.shape == (5, 5)