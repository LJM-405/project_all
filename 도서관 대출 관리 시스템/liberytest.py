#규칙만들기
from abc import ABC, abstractmethod
class LibraryItem(ABC):
    total_items=0
    def __init__(self,title,item_id):
        self.title=title
        self.item_id=item_id
        self.r=None
        LibraryItemis_loaned=False
        self.borrowe.total_items += 1
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
        sorted_kinds=sorted(kinds, key=lambda x  : kinds[x],reverse=True)
        for class_name in sorted_kinds:
            print(f"{kinds[class_name]:<6}{kinds[class_name]:>10}개")
            print("-"*56)
            loned_count= len([item for item in self.items if item.is_loaned])
            print(f"{'대출중':<10}{loned_count:>10}개")
            print(f"{'전체등록':<10}{LibraryItem.total_items:>10}개 (클래스 변수)")
            print("-"*56)
#출력 하였을때 예시
b=Book("파이썬 입문","B001","박응용","480")
print(b.info())
print(b.loan_period())
print(b.is_loaned)
d=DVD("인터스텔라","D001","놀란","169")
print(d.info())
m=Magazine("과학동아","M001",9)
print(m.loan_period())
print(m.info())
b.checkout("김민준")
b.checkout("이서연")
d.checkout("이서연")
b.return_item()
lib=Library("한빛도서관")
lib.add(Book("파이썬 입문","B001","박응용","480"))
lib.find("B001").info()
print(lib.find("X999"))
#show_all을 프린트하기 위한 준비물
lib1=Library("한빛도서관")
lib1.add(Book("파이썬 입문","B001","박응용","480"))
lib1.add(Book("자료구조","B002","김철수","320"))
lib1.add(DVD("인터스텔라","D001","놀란","169"))
lib1.add(Magazine("과학동아","M001",9))
lib1.find("B001").checkout("김민준")
lib1.find("D001").checkout("이서연")
lib1.show_all()
lib1.report()