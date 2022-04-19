from grid import Grid
from tile import Tile
from rotations import Rotations

def test_clockwise_rotate():
    g = Grid()
    g.grid[0][1] = Tile(2)
    g.grid[0][2] = Tile(4)
    g.grid[2][3] = Tile(8)
    grid = Rotations.clockwise_turn(g.grid, 4)

    assert grid[1][3].val == 2
    assert grid[2][3].val == 4
    assert grid[3][1].val == 8

def test_anticlockwise_rotate():
    g = Grid()
    g.grid[1][3] = Tile(2)
    g.grid[2][3] = Tile(4)
    g.grid[3][1] = Tile(8)
    grid = Rotations.anticlockwise_turn(g.grid, 4)

    assert grid[0][1].val == 2
    assert grid[0][2].val == 4
    assert grid[2][3].val == 8

def test_full_turn():
    g = Grid()
    g.grid[0][1] = Tile(2)
    g.grid[0][2] = Tile(4)
    g.grid[2][3] = Tile(8)
    grid = Rotations.full_turn(g.grid, 4)

    assert grid[3][2].val == 2
    assert grid[3][1].val == 4
    assert grid[1][0].val == 8