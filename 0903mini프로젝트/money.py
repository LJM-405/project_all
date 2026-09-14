#step 1
import sys
FILE = "records.txt"
CATEGORIES = ["식비","교통","문화","기타"]
def add_record(date,category,item,amount):
    with open("records.txt","a",encoding="utf-8")as f:
        f.write(f"{date},{category},{item},{amount}\n")
    print(f"기록했습니다.({date} {category} {item} {amount:,}원)")
add_record("2026-08-24","식비","점심 김밥",7000)
#step2
record_list=[]
def load_records():
    with open("records.txt","r",encoding="utf-8")as f:
        for line in f:
            line=line.strip()
            if not line: continue
            date,category,item,amount=line.split(",")
            row_dict={
                "date":date,
                "category":category,
                "item":item,
                "amount": int(amount),
            }
            record_list.append(row_dict)
    return record_list
records=load_records()
print(len(records))
print(records[0])
print(records[0]["amount"]+1000)
#step3
def show_all():
    records=load_records()
    if not records:
        print("아직 기록이 없습니다.")
        return
print("="*46)
print(f"{'용돈기록함':<12}")
print("="*46)
print(f"{'번호':<4}{'날짜':<10}{'분류':^8}{'금액':>9}")
print("-"*46)
for i,r in enumerate(records,1):
    print(f"{i:<5}{r['date']:<12}{r['category']:<7}{r['item']:<13}{r['amount']:>9}")