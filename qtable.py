class QTable(dict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        if not isinstance(value, list) or len(value) != 4:
            raise TypeError("QTable values must be lists of length 4")
        super().__setitem__(key, value)
