"""
    Given the scores for a season, get the number of times Maria 
    breaks her record for most and least points scored during the season.

                                    Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

     Returns int[2]: 
        An array with the numbers of times she broke her records. 
        Index 0 is for breaking most points records.
        Indes 1 is for breaking least points records.

    Sample Input:
        3 4 21 36 10 28 35 5 24 42
    Sample Output:
        4 0
"""

def breakingRecords(scores):

    min, total_min = scores[0], 0
    max, total_max = scores[0], 0

    for x in scores:

        if x > max:
            total_max += 1
            max = x
        
        if x < min:
            total_min += 1
            min = x

    return [total_max, total_min]


assert breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]) == [2, 4]
assert breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == [4, 0]