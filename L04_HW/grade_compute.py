#Convert a letter grade to a number
def gradeToNumber(grade):
    value = 0.0
    letter = grade[0]

    if letter == 'A':
        value = 4.0
    elif letter == 'B':
        value = 3.0
    elif letter == 'C':
        value = 3.0
    elif letter == 'D':
        value = 2.0
    elif letter == 'E':
        value = 1.0
    elif letter == 'F':
        value = 0.0

    if len(grade) == 2:
        if grade[1] == '+':
            value += 0.3
        elif grade[1] == '-':
            value -= 0.3
    
    return value

#Convert a number to a letter grade
def numberToGrade(num):
    if num >= 3.85:
        return "A"
    if num >= 3.5:
        return "A-"
    if num >= 3.15:
        return "B+"
    if num >= 2.85:
        return "B"
    if num >= 2.5:
        return "B-"
    if num >= 2.15:
        return "C+"
    if num >= 1.85:
        return "C"
    if num >= 1.5:
        return "C-"
    if num >= 1.15:
        return "D+"
    if num >= 0.85:
        return "D"
    return "F"
    
    
    
