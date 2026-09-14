from SmartPhone import SmartPhone#파일스마트폰에서 클래스스마트폰가져오기
from Address import Addr#파일Address에서 클래스addr가져오기
def start():
    phone=SmartPhone()
    phone.add_address(Addr("홍길동","010-1234-5678","santacoding@naver.com","서울 종로3가","친구"))
    phone.add_address(Addr("엄마","010-8212-1234","mom@naver.com","고산로123","가족"))
#작동문
    while True:
        print("주소관리 메뉴")
        print("1. 연락처 등록")
        print("2. 모든 연락처 출력")
        print("3.연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 프로그램 종료")
        choice=input("원하는 작업을 선택하세요 (1-6) : ")
        if choice=="1":
            name=input("이름을 입력하세요 : ")
            phone_num=input("전화번호를 입력하세요 : ")
            email=input("이메일을 입력하세요 : ")
            address=input("주소를 입력해주세요 : ")
            group=input("그룹(친구/가족)을 입력하세요 : ")
            new_addr=Addr(name,phone_num,email,address,group)#한번에모으기
            phone.add_address(new_addr)#추가하기
        elif choice=="2":
            phone.show_all_addresses()
        elif choice=="3":
            print("[연락처 검색]")
            search_name=input("이름을 적어주세요:")
            phone.serch_address(search_name)
        elif choice=="4":
            name=input("삭제할 이름을 적어주세요 : ")
            phone.delete_address(name)
        elif choice=="5":
            name=input("수정할 이름을 적어주세요 : ")
            new_phone_num=input("수정할 전화번호를 입력하세요 : ")
            new_email=input("수정할 이메일을 입력하세요 : ")
            new_address=input("수정할 주소를 입력하세요 : ")
            new_group=input("수정할 그룹(친구/가족)을 입력하세요 : ")
            phone.update_address(name,new_phone_num,new_email,new_address,new_group)
        elif choice=="6":
            print("종료합니다")
            break
        else:
            print("잘못된 번호입니다 1-6숫자를 입력하세요")
start()