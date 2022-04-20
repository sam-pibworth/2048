from tile import Tile
from rotations import Rotations
from response_parser import UserInput
import random
import os


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
        func = {"up":Rotations.anticlockwise_turn, "left": False, "down":Rotations.clockwise_turn, "right": Rotations.full_turn}[ins]
        if func:
            return func(self.grid, self.grid_size)
        else:
            return self.grid
    
    def denormalise(self, ins, grid):
        """Normalise grid to a left swipe"""
        func = {"up":Rotations.clockwise_turn, "left": False, "down":Rotations.anticlockwise_turn, "right": Rotations.full_turn}[ins]
        if func:
            return func(grid, self.grid_size)
        else:
            return grid

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

    def compare(self):
        changed_grid = [t.val for line in self.grid for t in line]
        original_grid = [t.val for line in self.original_grid for t in line]
        return not changed_grid == original_grid
    
    def swipe(self, ins):
        """Normalises to left swipe, performs swipe then denormalises"""
        self.original_grid = self.grid.copy()
        normalised_grid = self.normalise(ins)
        swiped_grid = self.normal_swipe(normalised_grid)
        self.grid = self.denormalise(ins, swiped_grid)
        return self.compare()

    def death_check(self):
        size = self.grid_size
        if any([True if not t.val else False for line in self.grid for t in line]):
            return False
        for i in range(size):
            line = self.grid[i]
            for j in range(size):
                t = line[j]
                for u,v in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= u < size and 0 <= v < size:
                        if self.grid[u][v].val == t.val:
                            return False
        return True

    
    def die(self):
        os.system('clear')
        print('you have died :(')
        exit()


    def run(self):
        while True:
            print(self)
            resp = UserInput.get_response()
            if self.swipe(resp):
                self.add_new_tiles()
            if self.death_check():
                self.die()
