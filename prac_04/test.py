FILENAME = "subject_data.txt"
def read_data(FILENAME):
    """Read data from a file and return it as a list of lists."""
    data = []

    with open(FILENAME, 'r') as file:
        for line in file:
            # Split the line into individual pieces of data
            parts = line.strip().split(',')
            # Convert the third element to an integer
            parts[2] = int(parts[2])
            # Append the parts to the data list
            data.append(parts)

    return data

# Example usage

result = read_data(FILENAME)
print(result)