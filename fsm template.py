class FSM:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.states = {}

    def add_state(self, state, transitions):
        self.states[state] = transitions

    def transition(self, input):
        if input in self.states[self.current_state]:
            self.current_state = self.states[self.current_state][input]
            return True
        else:
            return False


# Example usage
fsm = FSM('start')
fsm.add_state('start', {'a': 'end', 'b': 'start'})
fsm.add_state('end', {'a': 'end', 'b': 'start'})

print(fsm.transition('a'))  # True
print(fsm.transition('b'))  # True
print(fsm.current_state)  # "end"
