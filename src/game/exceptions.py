class NotPossibleActionException(Exception):
    """Exception raised when an action is not possible.

        Attributes:
            action (src.game.Action): the impossible action.
    """
    def __init__(self, action):
        self.action = action
