from src.grid import Grid
from src.tile import Tile

def test_init():
    g = Grid()
    values = [g.grid[i][j].val for i in range(g.grid_size) for j in range(g.grid_size) if g.grid[i][j].val]
    assert len(values) == 0
    g.setup()
    values = [g.grid[i][j].val for i in range(g.grid_size) for j in range(g.grid_size) if g.grid[i][j].val]
    assert len(values) == 2

def test_normalswipe_simple():
    g = Grid()
    g.grid[0][1] = Tile(2)
    g.grid = g.normal_swipe(g.grid)

    assert g.grid[0][0].val == 2
    assert not g.grid[0][1].val 


def test_normalswiple():
    g = Grid()
    g.grid[1][1] = Tile(2)
    g.grid[1][2] = Tile(2)
    g.grid[1][3] = Tile(4)
    
    g.grid = g.normal_swipe(g.grid)
    assert g.grid[1][0].val == 4
    assert g.grid[1][1].val == 4
    assert not g.grid[1][2].val

    g.grid = g.normal_swipe(g.grid)
    assert g.grid[1][0].val == 8

# if __name__ == '__main__':
#     test_clockwise_rotate()