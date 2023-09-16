def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    end_times = [[-1, book_time.pop(0)[1]]]

    def cmp_time(end_time, start_time):
        h1, m1 = map(int, end_time.split(':'))
        h2, m2 = map(int, start_time.split(':'))

        m1 += 10

        if m1 > 59:
            h1 += 1
            m1 -= 60
        if h1 != h2:
            return h1 < h2

        return m1 <= m2

    for j, schedule in enumerate(book_time):
        start, end = schedule
        for i, v in enumerate(end_times):
            idx, time = v
            if cmp_time(time, start):
                end_times.pop(i)
                end_times.append([j, end])
                break
        if [j, end] not in end_times:
            end_times.append([j, end])
    return len(end_times)