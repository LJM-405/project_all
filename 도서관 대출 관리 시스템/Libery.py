#규칙만들기
from abc import ABC, abstractmethod
class LibraryItem(ABC):
    total_items=0
    def __init__(self,title,item_id):
        self.title=title
        self.item_id=item_id
        self.is_loaned=False
        self.borrower=None
        LibraryItem.total_items += 1
#빌릴경우 출력
    def checkout(self,name):
        if self.is_loaned:
            print(f"'{self.title}'은(는) 이미 {self.borrower}님이 대출하였습니다")
            return False
        else:
            self.is_loaned= True
            self.borrower= name
            print(f"{name}님'{self.title}'대출완료!(대출기간{self.loan_period()}일)")
            return True
#반납할 경우 출력
    def return_item(self):
        if not self.is_loaned:
            print("대출 중이 아닙니다")
            return False
        else:
            print(f"{self.borrower}님이 '{self.title}'을(를) 반납하였습니다")
            self.is_loaned=False
            self.borrower=None
    @abstractmethod
    def loan_period(self):
        pass
    @abstractmethod
    def info(self):
        pass
#자식Book만들기
class Book(LibraryItem):
    def __init__(self,title,item_id,author,pages):
        super().__init__(title,item_id)
        self.author=author
        self.pages=pages
    def loan_period(self):
        return "14"
    def info(self):
        return f"[도서]{self.title}/{self.author}/{self.pages}쪽"
#자식dvd만들기
class DVD(LibraryItem):
    def __init__(self, title, item_id,director,minutes):
          super().__init__(title,item_id)
          self.director=director
          self.minutes=minutes
    def loan_period(self):
        return "7"
    def info(self):
        return f"[DVD]{self.title}/{self.director}감독/{self.minutes}분"
#자식메거진만들기
class Magazine(LibraryItem):
    def __init__(self, title, item_id,issue):
          super().__init__(title, item_id)
          self.issue=issue
    def loan_period(self):
        return "3"
    def info(self):
         return f"[매거진]{self.title}/{self.issue}호"
#도서관이라는 따로 만들어 클래스만들기
class Library:
    def __init__(self,name):
        self.name=name
        self.items=[]
    def add(self,item):
        self.items.append(item)
        print(f"'{item.title}'등록완료 (총{len(self.items)}개)")
    def find(self,item_id):
        for item in self.items:
            if item.item_id==item_id:
                return item
        return None
#표만들기
    def show_all(self):
        print("="*56)
        print(f"{self.name:^56}")
        print("="*56)
        print(f"{'ID':<6}{'정보':<32}{'상태':>14}")
        print("-"*56)
        for item in self.items:
            state=f"대출중({item.borrower})"if item.is_loaned else"대출가능"
            print(f"{item.item_id:<6}{item.info():<32}{state:>14}")
#종류별 통계 만들기
    def report(self):
        print("="*56)
        print(f"{'종류별 등록현황':^56}")
        print("-"*56)
        #종류묶을거 만들기
        kinds={}
        #여기에 뭐들어가는지
        for item in self.items:
            class_name=type(item).__name__
            #있으면더하고 없으면 추가하기
            if class_name in kinds:
                kinds[class_name]+=1
            else:
                kinds[class_name]=1
        sorted_kinds=sorted(kinds, key=lambda x: kinds[x],reverse=True)
        for class_name in sorted_kinds:
            print(f"{class_name:<10}{kinds[class_name]:>10}개")
        print("-"*56)
        loned_count= len([item for item in self.items if item.is_loaned])
        print(f"{'대출중':<10}{loned_count:>10}개")
        print(f"{'전체등록':<10}{LibraryItem.total_items:>10}개 (클래스 변수)")
        print("-"*56)
#출력 하였을때 예시
lib=Library("한빛도서관")
lib.add(Book("파이썬 입문","B001","박응용","480"))
lib.add(Book("자료구조","B002","김철수","320"))
lib.add(DVD("인터스텔라","D001","놀란","169"))
lib.add(Magazine("과학동아","M001",9))
is_on=True
while is_on:
    print("1.전체목록 2.통계 3.대출 4.반납. 0종료")
    choice=input("번호를 선택하세요")
    if choice=="1":
        print(lib.show_all())
    elif choice=="2":
        print(lib.report())
    elif choice=="3":
        choice_id=input("대출할 자료 번호:")
        item=lib.find(choice_id)
        if item is None:
            print("없는번호입니다")
            continue
        borrower_name= input("대출자 이름:")
        item.checkout(borrower_name)
    elif choice=="4":
        choice_return=input("대출자 이름:")
        found_item=None
        for item in lib.items:
            if item.is_loaned and item.borrower==choice_return:
                found_item=item
                break
        if found_item is None:
            print("빌린적없거나 대출자이름이 틀렸습니다")
            continue
        found_item.return_item()

    elif choice=="0":
        print("프로그램을 종료합니다")
        is_on=False
    else:
        print("없는 번호입니다")