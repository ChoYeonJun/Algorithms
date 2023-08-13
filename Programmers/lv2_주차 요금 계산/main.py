from datetime import timedelta
import math

def solution(fees, records):
    dft_min = fees[0]
    dft_cost = fees[1]
    unit_min = fees[2]
    unit_cost = fees[3]

    records = sorted(records, key=lambda x: (x.split()[1], x.split()[0]))
    i = 0
    answer = []
    car_dict = {}

    while i < len(records):
        in_case = records[i].split()
        in_num = in_case[1]

        if i == len(records) - 1 or in_num != records[i + 1].split()[1]:
            out_case = ["23:59", in_num, "OUT"]
            i += 1
        else:
            out_case = records[i + 1].split()
            i += 2

        in_hour = int(in_case[0].split(':')[0])
        in_min = int(in_case[0].split(':')[1])
        out_hour = int(out_case[0].split(':')[0])
        out_min = int(out_case[0].split(':')[1])

        in_time = timedelta(hours=in_hour, minutes=in_min)
        out_time = timedelta(hours=out_hour, minutes=out_min)
        sub_time = out_time - in_time

        total_min = int(str(sub_time).split(':')[0]) * 60 + int(str(sub_time).split(':')[1])

        if in_num in car_dict.keys():
            car_dict[in_num] += total_min
            continue

        car_dict[in_num] = total_min

    for k, v in sorted(car_dict.items()):
        total_min = v

        if total_min < dft_min:
            cost = dft_cost
        else:
            ext_min = total_min - dft_min
            ext_cnt = math.ceil(ext_min / unit_min)
            cost = dft_cost + unit_cost * ext_cnt
        answer.append(cost)

    return answer