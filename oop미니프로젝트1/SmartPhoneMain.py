from SmartPhone import SmartPhone#파일스마트폰에서 클래스스마트폰가져오기
from Address import CompanyAddr, CustomerAddr#파일Address에서 클래스가져오기
def start():
    phone=SmartPhone()

    while True:
        print("주소관리 메뉴")
        print("1. 연락처 등록(회사)")
        print("2. 연락처 등록(거래처)")
        print("3. 모든 연락처 출력")
        print("4.연락처 검색")
        print("5. 연락처 삭제")
        print("6. 연락처 수정")
        print("7. 프로그램 종료")
        choice=input("원하는 작업을 선택하세요 (1-7) : ")
        if choice=="1":
            print("#연락처 등록(회사)")
            name=input("이름을 입력하세요 : ")
            phone_num=input("전화번호를 입력하세요 : ")
            email=input("이메일을 입력하세요 : ")
            address=input("주소를 입력하세요 : ")
            birthday=input("생일을 입력하세요")
            company_title=input("직급을 입력하세요 : ")
            company_name=input("회사 이름을 입력하세요 : ")
            deft_name=input("부서를 입력하세요 : ")
            new_addr=CompanyAddr(name,phone_num,email,address,"회사",birthday,company_name,deft_name,company_title)#한번에모으기
            phone.add_address(new_addr)#추가하기
            print(f">>>> 데이터가 저장되었습니다.(현재 {len(phone.addr_list)}개)")
        elif choice=="2":
            print("# 연락처 등록 (거래처)")
            name=input("이름을 입력하세요 : ")
            phone_num=input("전화번호를 입력하세요 : ")
            email=input("이메일을 입력하세요 : ")
            address=input("주소를 입력하세요 : ")
            birthday=input("생일을 입력하세요")
            custmer_item=input("거래처아이템을 입력하세요 : ")
            custmer_name=input("거래처 이름을 입력하세요 : ")
            custmer_title=input("거래처 직급을 입력하세요 : ")
            new_addr=CustomerAddr(name,phone_num,email,address,"거래처",birthday,custmer_name,custmer_item,custmer_title)#한번에모으기
            phone.add_address(new_addr)#추가하기
            print(f">>>> 데이터가 저장되었습니다.(현재 {len(phone.addr_list)}개)")
        elif choice=="3":
            phone.show_all_addresses()
        elif choice=="4":
            print("[연락처 검색]")
            search_name=input("이름을 적어주세요:")
            phone.search_address(search_name)
        elif choice=="5":
            name=input("삭제할 이름을 적어주세요 : ")
            phone.delete_address(name)
        elif choice=="6":
            name=input("수정할 이름을 적어주세요 : ")
            new_phone_num=input("수정할 전화번호를 입력하세요 : ")
            new_email=input("수정할 이메일을 입력하세요 : ")
            new_address=input("수정할 주소를 적어주세요 : ")
            new_group=input("수정할 그룹(회사/거래처)을(를) 입력하세요 : ")
            phone.update_address(name,new_phone_num,new_email,new_address,new_group)
        elif choice=="7":
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 번호입니다 1-7숫자를 입력하세요")
if __name__=="__main__":
    start()