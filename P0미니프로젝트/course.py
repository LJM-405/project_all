python_list=['김민준','이서연','박도윤','이서연','최지우']
web_list=['이서연','박도윤','한지민','한지민']
#step1 중복제거
python_set=set(python_list)
web_set=set(web_list)
all_students = python_set | web_set
both=python_set & web_set
print(f"파이썬수강신청 {len(python_list)}->실제 {len(python_set)}명")
print(f"웹개발수강신청 {len(web_list)}->실제 {len(web_set)}명")
print(f"둘다수강:{len(both)}명")
print(python_set)
print(web_set)
print(all_students)
#step2 집합 연산으로 비교하기
python_count= len(python_list)
python_people=len(python_set)
only_py=python_set-web_set
only_web=web_set-python_set
one_only=python_set^web_set
print("둘 다 수강 : ",sorted(both))
print("전체 수강상 : ",sorted(all_students))
print("파이선만 : ",sorted(only_py))
print("웹개발만 : ",sorted(only_web))
print("한 과목만 : ",sorted(one_only))
#step3 불리언 판정하기
name='이서연'
print(f"이서연 파이썬 수강?,{name in python_set}")
print(f"이서연 웹개발 수강?,{name in web_set}")
print(f"이서연 둘다 수강?,{name in python_set and name in web_set}")
print(f"이서연 하나라도 수강?,{name in python_set or web_set}")
print(f"이서연 미수강?,{name not in  all_students}")
print(f"교집합이 비었나?,{name not in  both}")
#step4딕셔너리로 정리 리포트 출력
report={
    "python":len(python_set),
    "web":len(web_set),
    "both":len(both),
    "total":len(all_students),
}
dup_rate=report['both']/report['total']*100
print("="*32)
print(f"{'수강현황':^8}")
print("="*32)
print(f"{'파이썬':<14}{report['python']:>10}명")
print(f"{'웹개발':<14}{report['web']:<10}명")
print("="*32)
print(f"{'둘 다 수강':<14}{report['both']:<10}")
print(f"{'전체 인원':<14}{report['total']:<10}")
print("="*32)
print(f"중복 수강률: {dup_rate:.1f}%")