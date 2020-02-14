class NoFreeCellError(Exception):
    """Error raises when failing to find a free cell """


class NotPossibleActionException(Exception):
    """Exception raised when an action is not possible.

        Attributes:
            action (src.game.Action): the impossible action.
    """

    def __init__(self, action):
        super(NotPossibleActionException, self).__init__(action)
        self.action = action
