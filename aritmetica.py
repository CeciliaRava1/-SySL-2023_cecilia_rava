# Set status
operation_states = {'digit', 'operator'}
init_state = 'digit'
final_state = 'digit'

# Definition of transitions
transitions = {
    ('digit', 'digit'): 'digit',
    ('digit', 'operator'): 'operator',
    ('operator', 'digit'): 'digit',
}

# Input string
string = input('Insert an aritmethic operation: ')

# Definition of transition function
def transition(state, symbol):
    return transitions.get((state, symbol), 'error')

# Definition of the value_string function
def value_string(string):
    actual_state = init_state
    for char in string:
        if char.isdigit():
            actual_state = transition(actual_state, 'digit')
        elif char in {'+', '-', '*', '/'}:
            actual_state = transition(actual_state, 'operator')
        else:
            actual_state = 'error'
            break

    return actual_state

# Main program
result = value_string(string)

if result == final_state and len(string) != 1:
    print("The string is an arithmetic operation")
else:
    print("The string is not an arithmetic operation")

