import itertools

# Function to generate all permutations
def all_combinations(array):
    permutations = list(itertools.permutations(array))
    return permutations

# Example array
array = [1, 2, 3, 4, 5, 6, 7]

# Generate all permutations
combinations = all_combinations(array)

# Print all permutations
for combination in combinations:
    print(combination)
