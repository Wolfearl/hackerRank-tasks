def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            n = grades[i] + 1
            multiple_of_five = n + (5 - n % 5) if n % 5 != 0 else n
            if multiple_of_five - grades[i] < 3:
                grades[i] = multiple_of_five
    return grades


print(gradingStudents([44, 84, 94, 21, 0, 18, 100, 18, 62, 30, 61, 53, 0, 43, 2, 29, 53, 61, 40]))