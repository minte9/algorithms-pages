
def gradingStudents(grades):
    
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        
        reminder = grades[i]%5;
        diff = 5 - reminder;

        if diff < 3:
            grades[i] += 5 - reminder

    return grades

assert gradingStudents([73, 67, 37, 33]) == [75, 67, 37, 33]
assert gradingStudents([76, 68, 38, 43]) == [76, 70, 40, 45]