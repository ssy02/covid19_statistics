def normalize_data(n_cases, n_people, scale):
    # 각 지역별 100만 명당 신규 확진자 수 계산
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm = n / n_people[idx] * scale
        norm_cases.append(norm)
    return norm_cases


regions = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu',
           'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju',
           'Ulsan', 'Jeju', 'Sejong']

n_people = [9550227, 13530519, 3359527, 3322373, 2938429, 2630254, 2393626, 2118183,
            1838353, 1792476, 1597179, 1536270, 1454679, 1441970, 1124459, 675883, 365309]  # 2021-08

n_covid = [644, 529, 38, 29, 148, 28, 41, 62, 23, 27, 27, 33, 16, 40, 20, 5, 4]  # 2021-09-21


# 전체 인구, 전체 신규 확진자 수
sum_people = sum(n_people)
sum_covid = sum(n_covid)

# 100만 명당 확진자 수
norm_covid = normalize_data(n_covid, n_people, 1000000)

# 인구 통계 출력
print('### Korean Population by Region')
print('* Total population:', sum_people)
print()
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = pop / sum_people * 100
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))

print('')

# 신규 확진자 통계 출력
print('### Korean COVID-19 New Cases by Region')
print('* Total new cases:', sum_covid)
print()
print('| Region | New Cases | Ratio (%) | Cases per 1M |')
print('| ------ | --------- | --------- | ------------- |')
for idx, cases in enumerate(n_covid):
    ratio = cases / sum_covid * 100
    print('| %s | %d | %.1f | %.1f |' % (regions[idx], cases, ratio, norm_covid[idx]))
