"""
    Given the array of bird sightings (birds ids), determine the id
    of the most frequently sighted type. If more than 1 type has been spotted 
    than the maximum ammount return the smallest of their ids.
"""

def migratoryBirds(arr):
    ids = {}

    for m in range(len(arr)):
        key = arr[m]

        if key not in ids:
            ids[key] = 1
        else:
            ids[key] += 1

    min = arr[0] # smallest id
    for key in ids:

        if ids[key] > ids[min]:
               min = key

        if ids[key] == ids[min]:
            if key < min:
                min = key
            
    return min

assert migratoryBirds([1,1,2,2,3]) == 1
assert migratoryBirds([1,4,4,4,5,3]) == 4