from tile import Tile
from response_parser import UserInput

class Grid:
    def __init__(self, grid_size=4) -> None:
        self.grid = [[Tile() for _ in range(grid_size)] for _ in range(grid_size)]

    def __repr__(self) -> str:
        return '\n'.join([' '.join([t.disp(4) for t in l]) for l in self.grid])

    def swipe():
        pass
    
    def run(self):
        while True:
            print(self)
            resp = UserInput.get_response()
            