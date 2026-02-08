from grade_compute import *


# Validates a single letter grade
def isValidGrade(grade):
    if len(grade) < 1 or len(grade) > 2:
        return False
    letter = grade[0].upper()
    modifier = grade[1] if len(grade) == 2 else ''
    if letter not in "ABCDF":
        return False
    if modifier not in ['', '+', '-']:
        return False
    if letter == 'F' and modifier != '':
        return False
    return True


# Read the grades
def processLine(line):
    parts = line.split('$')
    if len(parts) != 4:
        return None
    grades = []
    for p in parts:
        g = p.strip().upper()
        if not isValidGrade(g):
            return None
        grades.append(g)
    return grades


# Prints a 40-character ASCII summary box
def printAsciiBox(grades, lowest, avg, final_letter):
    width = 40
    horizontal = "-" * (width - 2)

    print(f"|{horizontal}|")
    header = "GRADE REPORT SUMMARY"
    print(f"| {header.center(width - 4)} |")
    print(f"|{horizontal}|")
    print("| Grades Entered: " + ", ".join(grades).ljust(20) + "|")
    print("| Lowest Grade Dropped: ".ljust(26) + lowest.ljust(12) + "|")
    print("| Calculated Average: ".ljust(26) + f"{avg:.2f}".ljust(12) + "|")
    print("| Final Letter Grade: ".ljust(26) + final_letter.ljust(12) + "|")
    print("|" + "-" * 38 + "|")


# Main function
def main():
    user_input = input("Enter 4 letter grades separated by $ (or Q to quit): ").upper()

    # Quit check
    if user_input == 'Q':
        print("Program terminated.")
        return

    # Process input
    grades = processLine(user_input)
    if grades is None:
        print("Invalid input. Please restart the program.")
        return

    # Convert grades to numbers
    numeric_grades = [gradeToNumber(g) for g in grades]

    # Drop lowest grade
    lowest_num = dropLowest(numeric_grades)

    # Compute average
    avg = computeAverage(numeric_grades)

    # Apply curve if needed
    if allBelowBMinus(numeric_grades):
        avg += 0.25

    # Print ASCII summary box
    printAsciiBox(grades, numberToGrade(lowest_num), avg, numberToGrade(avg))


if __name__ == "__main__":
    main()