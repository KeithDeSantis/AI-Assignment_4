class QTable(dict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        if not isinstance(value, list) or len(value) != 4:
            raise ValueError("QTable values must be lists of length 4")
        super().__setitem__(key, value)

    def max_action(self, row, col):
        """
        This gets the index of the maximum action utility for a given space
        """
        action_values = super().__getitem__((row, col))
        return action_values.index(max(action_values))
