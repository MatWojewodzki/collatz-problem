import random

# Function to generate random number ranges
def generate_random_ranges(num_ranges, range_min, range_max):
    ranges = []
    for _ in range(num_ranges):
        start = random.randint(range_min, range_max - 1)
        stop = random.randint(start + 1, range_max)
        ranges.append(f"{start} {stop}")
    return "\n".join(ranges)

# Generate a file with 10 random number ranges (for example)
num_ranges = 1000
range_min = 1
range_max = 10000
random_ranges = generate_random_ranges(num_ranges, range_min, range_max)

# Save the random ranges to a file
file_path = 'random_input.txt'
with open(file_path, 'w') as f:
    f.write(random_ranges)