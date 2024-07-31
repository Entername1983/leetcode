if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_scores: list = student_marks[query_name]
    student_sum: float = 0
    for n in student_scores:
        student_sum += n
    print(f"{student_sum/len(student_scores):.2f}")