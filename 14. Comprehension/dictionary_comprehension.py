students_list = ['태연', '진우', '정연', '하늘', '성진']

students_dict = {
    f'{number + 1}번': name for number, name in enumerate(students_list)
}

print(students_dict)

scores_list = [85, 92, 78, 90, 100]

scores_dict = {
    student: score for student, score in zip(students_list, scores_list)
}

print(scores_dict)
