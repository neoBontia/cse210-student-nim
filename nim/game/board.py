import random

class Board:
    
    def __init__(self):
        self._piles = []
        self._prepare()

    def apply(self, move):
        """Applies a move to the playing surface. In this case,
        that means removing a number of stones from a pile. The
        apply method accepts one argument, an instance of Move.
        """
        self._piles[move.get_pile()] -= move.get_stones()

    def is_empty(self):
        """Determines if all the stones have been removed from the
        board. It returns True if the board has no stones on it;
        false if otherwise.
        """
        for stones in self._piles:
            if not stones == 0:
                return False
        
        return True

    def to_string(self):
        """Converts the board data to its string representation and
        returns it to the caller.
        """
        data = ""

        for i in range(len(self._piles)):
            line = f"{i}: "
            for _ in range(self._piles[i]):
                line += "O "
            line += "\n"
            data += line

        return data

    def _prepare(self):
        """Sets up the board with a random number of piles (2 - 5)
        containing a random number of stones (1 - 9).
        """
        for _ in range(random.randint(2, 5)):
            stones = random.randint(1, 9)
            self._piles.append(stones)