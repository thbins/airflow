def python_datetime_dateutil_test():
    from datetime import datetime
    from dateutil import relativedelta

    now = datetime(year=2025, month=11, day=16)
    print('현재시간:' + str(now))
    print('---------------월 연산---------------')
    print(now + relativedelta.relativedelta(months=1)) # 1월로 변경
    print(now.replace(month=1)) # 1월로 변경
    print(now + relativedelta.relativedelta(months=-1)) # 1개월 빼기
    print('---------------일 연산---------------')
    print(now + relativedelta.relativedelta(days=1)) # 1일로 변경
    print(now.replace(day=1)) # 1일로 변경
    print(now + relativedelta.relativedelta(days=-1)) # 1일 빼기
    print('---------------연산 여러 개---------------')
    print(now + relativedelta.relativedelta(months=-1) + relativedelta.relativedelta(days=-1)) # 1개월, 1일 빼기 