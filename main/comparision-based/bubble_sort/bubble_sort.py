def bubble_sort(X):
    for i in range(len(X)):
        
        for j in range(len(X) -i-1):

            if X[j] > X[j+1]:
                X[j], X[j+1] = X[j+1], X[j]  # Look Here

# Example usage:
A = [1, 3, 9, 5, 4, 0]

bubble_sort(A)
print("Sorted list =", A)

"""
    [0, 1, 3, 4, 5, 9]
"""