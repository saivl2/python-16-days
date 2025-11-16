states_of_america = ['Delaware', 'Pennsylania', 'Texas', 'Kansas', 'Massachusetts']

print(states_of_america[2])
print(states_of_america[-1])

# Changing items in the list
states_of_america[2] = 'Florida'
print(states_of_america)

# Add item to the end of the list
states_of_america.append('Hawaii')
print(states_of_america)

states_of_america.extend(['California', 'Ohio'])
print(states_of_america)

# remove the last element
states_of_america.pop()
print(states_of_america)