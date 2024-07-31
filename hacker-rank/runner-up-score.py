if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_score: int = -100
    runner_up: int = -100
    for score in arr:
        if score > max_score and score > runner_up:
            runner_up = max_score
            max_score = score
        if runner_up < score < max_score:
            runner_up = score
    print(runner_up)