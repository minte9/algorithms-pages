def selection_sort(X):
    for i in range(len(X)):
        min_index = i

        for j in range(i+1, len(X)):
            if X[j] < X[min_index]: # Look Here
                min_index = j

        X[i], X[min_index] = X[min_index], X[i]

# Example usage:
A = [1, 3, 9, 5, 4, 0]

selection_sort(A)
print("Sorted list =", A)

"""
    [0, 1, 3, 4, 5, 9]
"""