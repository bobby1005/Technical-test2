from collections import Counter

def nth_most_rate(arr, n):
    # Use Counter to count occurrences of each element
    counts = Counter(arr)

    # Sort elements based on their counts and values
    sorted_items = sorted(counts.items(), key=lambda x: (x[1], x[0]))

    # Check if n is within a valid range
    if 1 <= n <= len(sorted_items):
        return sorted_items[n-1][0]  # Return the nth-rarest item
    else:
        return None  # Invalid value of n

# Example usage:
arr = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = 2
result = nth_most_rate(arr, n)

print(f"The {n}nd rarest item is: {result}")
