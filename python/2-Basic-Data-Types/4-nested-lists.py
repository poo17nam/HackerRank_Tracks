if __name__ == '__main__':

    student_marks = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_marks.append([name,score])
        # marks list should be unique shouldn't contain any duplicate
        # check for duplicate by
        if score not in marks:
        #   marks.append(score)
            marks.append(score)

    marks.sort()

    second_lowest_marks = []
    for each_student in student_marks:
        if each_student[1] == marks[1]:
            second_lowest_marks.append(each_student)

    second_lowest_marks.sort()

    for student_name in second_lowest_marks:
        print(student_name[0])
