class Reward2048:
    """Reward obtained after an action is taken.

        Attributes:
            score (int): the increment score i.e., the sum of merged tiles
            tiles_moved (int): the number of tiles that have moved
    """
    def __init__(self, score, tiles_moved):
        self._score = score
        self._tiles_moved = tiles_moved

    @property
    def score(self):
        return self._score

    @property
    def tiles_moved(self):
        return self._tiles_moved
