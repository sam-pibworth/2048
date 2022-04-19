from tile import Tile
from rotations import Rotations
from response_parser import UserInput
import random


class Grid:
    def __init__(self, grid_size=4) -> None:
        self.grid_size = grid_size
        self.grid = [[Tile() for _ in range(grid_size)] for _ in range(grid_size)]
        self.new_tiles = (2, 4)  # generates with uniform probability

    def __repr__(self) -> str:
        return "\n".join([" ".join([t.disp(4) for t in l]) for l in self.grid])

    def setup(self):
        for _ in range(2):
            self.add_new_tiles()

    def add_new_tiles(self):
        g_gen = range(self.grid_size)
        empty_spots = [(i, j) for i in g_gen for j in g_gen if not self.grid[i][j].val]
        u, v = empty_spots[random.randrange(len(empty_spots))]
        new_tile = Tile(self.new_tiles[random.randrange(len(self.new_tiles))])
        self.grid[u][v] = new_tile

    def normalise(self, ins):
        """Normalise grid to a left swipe"""
        func = {"up":Rotations.anticlockwise_turn, "left": False, "down":Rotations.full_turn, "right": Rotations.clockwise_turn}[ins]
        if func:
            return func(self.grid, self.grid_size)
    
    def denormalise(self, ins, grid):
        """Normalise grid to a left swipe"""
        func = {"up":Rotations.clockwise_turn, "left": False, "down":Rotations.full_turn, "right": Rotations.anticlockwise_turn}[ins]
        if func:
            return func(grid, self.grid_size)

    def normal_swipe(self, grid):
        """Performs a left swipe"""
        for i in range(len(grid)):
            line = grid[i]
            new_line = []
            for x in range(len(line)):
                tile = line[x]
                if tile.val:
                    further_tiles = [line[y].val for y in range(x + 1, len(line))]
                    if not any(further_tiles):
                        new_line.append(tile)
                    else:
                        for y in range(x + 1, len(line)):
                            new_tile = line[y]
                            if new_tile.val:
                                if new_tile.val == tile.val:
                                    new_value = tile.val * 2
                                    new_line.append(Tile(new_value))
                                    line[y] = Tile()
                                else:
                                    new_line.append(tile)
                                break

            while len(new_line) < 4:
                new_line.append(Tile())
            grid[i] = new_line
        return grid

    def swipe(self, ins):
        """Normalises to left swipe, performs swipe then denormalises"""
        grid = self.normalise(ins)
        grid = self.normal_swipe(grid)
        self.grid = self.denormalise(ins, grid)
        return True

    def run(self):
        while True:
            print(self)
            resp = UserInput.get_response()
            if self.swipe(resp):
                self.add_new_tiles()
