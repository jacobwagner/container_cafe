class UnrecognizedState(Exception):
    pass


class State(object):
    INITIAL = 0
    CREATED = 1
    STARTED = 2
    RUNNING = 3
    STOPPED = 4
    DESTROYED = 5

    def __init__(self, initial_state=INITIAL):
        self.value = initial_state

    def __str__(self):
        return 'State({})'.format(self.value)

    def set_state(self, state):
        if hasattr(self, state):
            self.value = state
        else:
            raise UnrecognizedState
