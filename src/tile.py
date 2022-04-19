class Tile:
    def __init__(self, val=False) -> None:
        self.val = val

    def __repr__(self) -> str:
        if self.val:
            return str(self.val)
        else:
            return ' '
    
    def disp(self, size) -> str:
        if self.val:
            return str(self.val).center(size)
        else:
            return "[ ]".center(size)
