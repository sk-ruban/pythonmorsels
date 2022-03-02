import math


def percent_to_grade(marks, *, suffix = False, round = False):
    if round:
        marks = normal_round(marks)
    match marks:
        case num if num < 60:
            return "F"
        case num if num < 70:
            return check_suffix(num, "D", suffix)
        case num if num < 80:
            return check_suffix(num, "C", suffix)
        case num if num < 90:
            return check_suffix(num, "B", suffix)
        case _:
            return check_suffix(num, "A", suffix)


def check_suffix(marks, grade, suffix):
    if suffix:
        match marks:
            case num if num == 100:
                 return 'A+'
            case num if num % 10 < 3:
                return grade + '-'
            case num if num % 10 < 7:
                return grade
            case num if num % 10 < 10:
                return grade + '+'
    else:
        return grade


def calculate_gpa(list):
    gpa = 0
    for grades in list:
        match grades:
            case score if score == 'A+':
                gpa += 4.33
            case score if score == 'A':
                gpa += 4
            case score if score == 'A-':
                gpa += 3.67
            case score if score == 'B+':
                gpa += 3.33
            case score if score == 'B':
                gpa += 3
            case score if score == 'B-':
                gpa += 2.67
            case score if score == 'C+':
                gpa += 2.33
            case score if score == 'C':
                gpa += 2
            case score if score == 'C-':
                gpa += 1.67
            case score if score == 'D+':
                gpa += 1.33
            case score if score == 'D':
                gpa += 1
            case score if score == 'D-':
                gpa += 0.67
            case score if score == 'F':
                gpa += 0
    return gpa/len(list)


def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


percent_to_grade(69.4, round=True)
percent_to_grade(69.6, round=True)
percent_to_grade(72.5, suffix=True, round=True)
percent_to_grade(89.6, suffix=True, round=True)

calculate_gpa(['D+', 'C', 'A-', 'B'])
calculate_gpa(['B+', 'A', 'C+', 'F'])






