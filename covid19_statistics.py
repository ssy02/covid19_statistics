def normalize_data(n_cases, n_people, scale):
    # 인구 대비 확진자 수를 scale 기준으로 정규화
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append(n / n_people[idx] * scale)
    return norm_cases


# 지역별 데이터
regions = ['Seoul']
n_people = [9550227]       # 인구 수
n_covid = [644]            # 신규 확진자 수

# 전체 인구, 전체 신규 확진자 수
sum_people = sum(n_people)
sum_covid = sum(n_covid)

# 인구 백만 명당 확진자 수
norm_covid = normalize_data(n_covid, n_people, 1_000_000)


# -------------------------------
# 인구 통계 출력
# -------------------------------
print('## Korean Population by Region')
print('* Total population:', sum_people)
print()
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')

for idx, pop in enumerate(n_people):
    ratio = pop / sum_people * 100
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))

print()


# -------------------------------
# 신규 확진자 통계 출력
# -------------------------------
print('## Korean COVID-19 New Cases by Region')
print('* Total new cases:', sum_covid)
print()
print('| Region | New Cases | Ratio (%) | Cases per 1M |')
print('| ------ | --------- | --------- | ------------ |')

for idx, cases in enumerate(n_covid):
    ratio = cases / sum_covid * 100
    print('| %s | %d | %.1f | %.1f |' % (regions[idx], cases, ratio, norm_covid[idx]))
