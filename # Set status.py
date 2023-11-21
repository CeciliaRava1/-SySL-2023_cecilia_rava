# Set status
light_states = {'disconnected', 'connectedd', 'on', 'off', 'red', 'yellow', 'green'}
init_state = 'disconnected'
final_state = 'green'

# Definition of transitions
transitions = {
    ('disconnected', '0'): 'disconnected',
    ('disconnected', '1'): 'connected',
    ('connected', '0'): 'connected',
    ('connected', '1'): 'off',
    ('off', '0'): 'off',
    ('off', '1'): 'on',
    ('on', '0'): 'on',
    ('on', '1'): 'red',
    ('red', '0'): 'red',
    ('red', '1'): 'yellow',
    ('yellow', '0'): 'yellow',
    ('yellow', '1'): 'green',
    ('green', '0'): 'green'
}

# Input string
string = input('Insert a combination of 0 and 1: ')

# Definition of transition function
def transition(state, symbol):
    return transitions.get((state, symbol), 'error')

# Definition of the value_string function
def value_string(string):
    actual_state = init_state
    for i in string:
        actual_state = transition(actual_state, i)

    return actual_state

# Main program
result = value_string(string)

if result == final_state:
    print("The string is accepted")
else:
    print("The string is rejected")


