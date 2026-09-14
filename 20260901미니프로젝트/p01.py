print("1번")
answer=37
a=int(input("숫자를 입력하세요(1~100)"))
if a>=answer:
    print("down!더작은 수를 입력하세요")
elif a<=answer:
    print("up!더 큰 수를 입력하세요.")
elif a==answer:
    print("정답입니다!")
print("2번")
answer=37
while True:
    a=int(input("숫자를 입력하세요(1~100)"))
    if a>answer:
        print("down")
    elif a<answer:
        print("up!더 큰 수를 입력하세요.")
    else:
        print("정답")
        break
print("3번")
count=0
c_history=[]
answer=37
while count<5:
    a=int(input(f"[{count}/5] 숫자를 입력하세요"))
    count=count+1
    if a>answer:
        print("down")
    elif a<answer:
        print("up!더 큰 수를 입력하세요.")
    else:
        print(f"{count}번만에 정답입니다")
        break
print("4번")
attempts=0
up_c=0
down_c=0
answer=37
a_count=[]
while True:
    a=int(input("숫자를 입력하세요(1~100)"))
    attempts +=1
    a_count.append(a)
    if a>answer:
        print("down!더 작은 수를 입력하세요")
        down_c +=1
    elif a<answer:
        print("up!더 큰 수를 입력하세요.")
        up_c +=1
    else:
        print("정답")
        break
too_big=[num for num in a_count if num > answer]
too_small=[num for num in a_count if num < answer]
print("="*34)
print(f"{'게임결과':<6}")
print("="*34)
print(f"{'정답':<8}{answer:^8}")
print(f"{'시도 횟수':<8}{attempts:^8}")
print("-"*34)
print(f"{'입력 기록':<8} {str(a_count):^8}")
print(f"{'너무 큰 수':<8}{len(too_big):^8}")
print(f"{'너무 작은 수':<8}{len(too_small):^8}")
print("="*34)