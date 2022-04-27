"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [*map(round, student_scores[::-1])]


def count_failed_students(student_scores):
    return sum(score <= 40 for score in student_scores)


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    step = (highest - 40) // 4
    return [41 + i * step for i in range(4)]


def student_ranking(student_scores, student_names):
    return [f'{i}. {name}: {score}'
            for i, (name, score) in enumerate(zip(student_names, student_scores), 1)]


def perfect_score(student_info):
    perfect_scores = [student for student in student_info if student[-1] == 100]
    return perfect_scores and perfect_scores[0]